# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:53:16 2021

@author: Entropy
"""
import sys
import hashlib
import markdown
import pymongo
import datetime
import os
from pymongo.errors import ConnectionFailure
from ui.sign_ui import Ui_Sign
from ui.main_ui import Ui_MainWindow
from ui.preview_ui import Ui_Preview
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QPixmap, QImage, QTextCursor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QLineEdit, QListWidgetItem
        
markdown_list = ['markdown.extensions.extra', 'markdown.extensions.abbr', 'markdown.extensions.attr_list',\
                 'markdown.extensions.def_list', 'markdown.extensions.fenced_code', 'markdown.extensions.footnotes',\
                 'markdown.extensions.tables', 'markdown.extensions.admonition', 'markdown.extensions.codehilite',\
                 'markdown.extensions.meta', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists',\
                 'markdown.extensions.smarty', 'markdown.extensions.toc', 'markdown.extensions.wikilinks']
########################################################################################################
class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
########################################################################################################
# Preview window    
class Preview(QWidget, Ui_Preview):
    def __init__(self, title = ''):
        super(Preview, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title + ' - Preview')
        self.can_close = False
        self.preview_text_browser.setReadOnly(True)
        self.preview_text_browser.setText('')
        
    def set_html(self, html):
        # Update the html-text.
        self.preview_text_browser.setText(html)
        self.preview_text_browser.moveCursor(QTextCursor.End)
        
    def set_close(self, flag):
        self.can_close = flag
        
    def closeEvent(self, event):
        # If can colse it, then colse; else just hide it. 
        if self.can_close:
            event.accept()
        else:
            self.hide()
########################################################################################################
# Main window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('The back-stage management')
        self.setFixedSize(1000, 800)
        self.setWindowIcon(QIcon('D:/blog-a/icon.icon'))

        # Create the preview window but not show
        self.edit_preview = Preview('edit')
        self.new_preview = Preview('new')
        
        self.main_stacked_widget.setCurrentIndex(0)
        self.set_widget(False)
        self.mesg_board_text_browser.setReadOnly(True)

        self.statusbar.showMessage('Connect to database...')
        
        self.slot_init() # Init the slot functions
        # Use the mongodb
        self.connected_to_database = False
        try:
            self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        except ConnectionFailure as e:
            print(e)
            self.mesg_box('ERROR', e)
            self.connected_to_database = False
            self.statusbar.showMessage(e)
        else:
            self.articles_db = self.client['Acticles']
            self.articles_col = self.articles_db['articles']
            self.mesg_db = self.client['MesgBoard']
            self.mesg_col = self.mesg_db['liuyans']
            self.connected_to_database = True
            self.statusbar.showMessage('Connect to database success.', 5000)
        
        self.has_edited = False
        self.now_open = -1;
        self.articles_dict_list = []
        self.read_articles()
        self.update_mesg_board()
        
    def set_widget(self, flag):
        self.edit_title_line_edit.setReadOnly(bool(1 - flag))
        self.edit_text_edit.setReadOnly(bool(1 - flag))
        self.edit_preview_btn.setEnabled(flag)
        self.edit_issue_btn.setEnabled(flag)
        self.edit_delete_btn.setEnabled(flag)
        self.edit_out_btn.setEnabled(flag)
        
    def slot_init(self):
        # Set the stack-widgt current index
        self.home_page_btn.clicked.connect(lambda: self.set_stack_page_fun(0))
        self.edit_page_btn.clicked.connect(lambda: self.set_stack_page_fun(1))
        self.new_page_btn.clicked.connect(lambda: self.set_stack_page_fun(2))
        self.board_page_btn.clicked.connect(lambda: self.set_stack_page_fun(3))
        # edit article
        self.edit_preview_btn.clicked.connect(lambda: self.preview_window_fun('edit'))
        self.edit_issue_btn.clicked.connect(lambda: self.edit_issue_fun('edit'))
        self.edit_delete_btn.clicked.connect(self.delete_article_fun)
        self.edit_out_btn.clicked.connect(lambda: self.out_article_fun('edit'))
        
        self.new_preview_btn.clicked.connect(lambda: self.preview_window_fun('new'))
        self.new_issue_btn.clicked.connect(lambda: self.edit_issue_fun('new'))
        self.new_save_btn.clicked.connect(lambda: self.out_article_fun('new'))
        self.new_open_btn.clicked.connect(self.new_open_fun)
        self.new_clear_btn.clicked.connect(self.new_clear_fun)
        # If the text-edit's text be changed, then update the private-window's text
        self.edit_text_edit.textChanged.connect(lambda: self.set_preview_text_fun('edit'))
        self.new_text_edit.textChanged.connect(lambda: self.set_preview_text_fun('new'))
        
        
        self.mesg_board_btn.clicked.connect(self.refresh_fun)
        
        self.edit_list_widget.doubleClicked.connect(self.artic_show_fun)
        
    def read_articles(self):
        for article in self.articles_col.find():
            self.articles_dict_list.insert(0, article)
        self.update_articles_edit_widget()
        
    def update_articles_edit_widget(self):
        for article in self.articles_dict_list:
            article_title = article['title'] + '\n\t' + article['release_time'].strftime('%Y-%m-%d')
            self.edit_list_widget.addItem(QListWidgetItem(article_title))
        
    def set_stack_page_fun(self, index):
        self.main_stacked_widget.setCurrentIndex(index)
        
    def preview_window_fun(self, model):
        if model == 'edit':
            self.edit_preview.show()
        elif model == 'new':
            self.new_preview.show()
        else:
            return
        
    def edit_issue_fun(self, model):
        if model == 'edit':
            res = self.mesg_box('WARNING', 'Are you sure to issue it?')
            if res == QMessageBox.Yes:
                new_title = self.edit_title_line_edit.text()
                new_content = self.edit_text_edit.toPlainText()
                if new_title == '' or new_content == '':
                    self.mesg_box('ERROR', 'Please input title and content.')
                    return
                
                index = self.now_open
                if -1 != index:
                    query = { '_id' : self.articles_dict_list[index]['_id'] }
                    new_val = {'$set':{'title' : new_title, 'content' : new_content, 'edit_time': datetime.datetime.utcnow()}}
                    try:
                        self.articles_col.update_one(query, new_val)
                    except: # If error
                        self.mesg_box('ERROR', 'Update failure.')
                        return
                    else: # Success, update the self.articles_dict_list
                        self.mesg_box('INFO', 'Update successfully!')
                        self.articles_dict_list[index]['title'] =  new_title
                        self.articles_dict_list[index]['content'] =  new_content
                        article_title = self.articles_dict_list[index]['title'] + '\n\t' + self.articles_dict_list[index]['release_time'].strftime('%Y-%m-%d')
                        item = self.edit_list_widget.item(index) # Update the item.
                        item.setText(article_title)
            else:
                return
            
        elif model == 'new':
            title_text = self.new_title_line_edit.text()
            content_text = self.new_text_edit.toPlainText()
            time_text = datetime.datetime.utcnow()
            if title_text == '' or content_text == '':
                self.mesg_box('ERROR', 'Please input title and content.')
                return
            
            article = {
                'title' : title_text,
                'content' : content_text,
                'release_time' : time_text,
                'edit_time' : time_text
                }
            try:
                self.articles_col.insert_one(article)
            except: # If error...
                self.mesg_box('ERROR', 'Insert failure.')
                return
            else: # Success, update the self.articles_dict_list, the self.edit_list_widget and the new_text.
                self.mesg_box('INFO', 'Insert successfully!')
                self.new_title_line_edit.clear()
                self.new_text_edit.clear()
                self.articles_dict_list.insert(0, article)
                article_title = article['title'] + '\n\t' + article['release_time'].strftime('%Y-%m-%d')
                self.edit_list_widget.insertItem(0, QListWidgetItem(article_title))
            return
        else:
            return
        
    def delete_article_fun(self):
        # Delete a has been showed article.
        res = self.mesg_box('WARNING', 'Are you sure to delete it?')
        if res == QMessageBox.Yes:
            index = self.now_open
            if -1 != index:
                query = { '_id' : self.articles_dict_list[index]['_id'] }
                try:
                    self.articles_col.delete_one(query)
                except: # If error...
                    self.mesg_box('ERROR', 'Delete failure.')
                    return
                else: # Success, update the self.articles_dict_list, the self.edit_list_widget and the edit_text.
                    self.mesg_box('INFO', 'Delete successfully!')
                    self.articles_dict_list.pop(index)
                    item = self.edit_list_widget.item(index)
                    self.edit_list_widget.takeItem(self.edit_list_widget.row(item))
                    self.edit_title_line_edit.clear()
                    self.edit_text_edit.clear()
                    self.set_widget(False)
        else:
            return
        
    def out_article_fun(self, model):
        file_name = ''
        file_content = ''
        if model == 'edit':
            file_name = self.edit_title_line_edit.text()
            file_content = self.edit_text_edit.toPlainText()
        elif model == 'new':
            file_name = self.new_title_line_edit.text()
            file_content = self.new_text_edit.toPlainText()
        else:
            return
            
        if file_name == '' or file_content == '':
            self.mesg_box('ERROR', 'Please input title and content.')
            return
        file_path = QFileDialog.getSaveFileName(self,
                                                    'Choose Save Path',
                                                    file_name + '.md',
                                                    'MD FILES(*.md)')
        if file_path[0] == '':
            return

        with open(file_path[0], 'w') as f:
            f.write(file_content)
            f.close()
        
    def mesg_box(self, kind, text):
        if kind == 'ERROR':
            res = QMessageBox.critical(self, kind, text, QMessageBox.Ok, QMessageBox.Ok);
            return res
        elif kind == 'INFO':
            res = QMessageBox.information(self, kind, text, QMessageBox.Ok, QMessageBox.Ok)
            return res
        elif kind == 'WARNING':
            res = QMessageBox.warning(self, kind, text, QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            return res
        else:
            return
        
    def set_preview_text_fun(self, model):
        # Open the preview window.
        if model == 'edit':
            html = markdown.markdown(self.edit_text_edit.toPlainText(), extensions = markdown_list)
            # print(html)
            self.edit_preview.set_html(html)
        elif model == 'new':
            html = markdown.markdown(self.new_text_edit.toPlainText(), extensions = markdown_list)
            # print(html)
            self.new_preview.set_html(html)
            
    def new_open_fun(self):
        res = self.mesg_box('WARNING', 'Are you sure to open an new file?')
        if res == QMessageBox.Yes:
            file = QFileDialog.getOpenFileName(self,
                                               'Choose MD',
                                               'D:/blog-a/tmp/',
                                               'MD FILES(*.md)') # ;; ALL FILES(*.*)')
            if file[0] == '':
                # If no choose any file...
                return

            fi = QFileInfo(file[0])
            with open(file[0] , 'r') as f:
                self.new_text_edit.setText(f.read())
                f.close()
            self.new_title_line_edit.setText(fi.fileName().split('.')[0])
            
        else:
            return

    def new_clear_fun(self):
        # Clear the buffer.
        res = self.mesg_box('WARNING', 'Are you sure to clear it?')
        if res == QMessageBox.Yes:
            self.new_title_line_edit.clear()
            self.new_text_edit.clear()
        else:
            return
    
    def artic_show_fun(self):
        # Show the article.
        self.set_widget(True)
        index = self.edit_list_widget.currentRow()
        self.now_open = index
        self.edit_title_line_edit.setText(self.articles_dict_list[index]['title'])
        self.edit_text_edit.setText(self.articles_dict_list[index]['content'])
        
    def refresh_fun(self):
        self.mesg_board_text_browser.clear()
        self.update_mesg_board()
        
    def update_mesg_board(self):
        for mesg in self.mesg_col.find():
            mesg_str = '[' + mesg['send_time'].strftime('%Y-%m-%d') + ']\n'\
                       + mesg['nickname'] + ':\n\t' + mesg['message'] + '\n'
            self.mesg_board_text_browser.insertPlainText(mesg_str)
            self.mesg_board_text_browser.moveCursor(QTextCursor.Start)
        
    def closeEvent(self, event):
        # If close self, close the preview-window before.
        self.edit_preview.set_close(True)
        self.new_preview.set_close(True)
        self.edit_preview.close()
        self.new_preview.close()
        event.accept()

########################################################################################################
# Sign window.     
class SignIn(QWidget, Ui_Sign):

    def __init__(self, qssStyle):
        super(SignIn, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sign in')
        self.setFixedSize(400, 300)
        
        self.pw_line.setEchoMode(QLineEdit.Password)
        
        self.quit_btn.clicked.connect(self.quit_fun)
        self.sign_btn.clicked.connect(self.sign_fun)
        # Set the user name and the password
        self.user_name = '67671a2f53dd910a8b35840edb6a0a1e751ae5532178ca7f025b823eee317992'
        self.pass_word = '5a4fa827928578a1a491cf3f56f5f164e94b6f65e55a4c774afcfef8329a39a8'

        self.style = qssStyle
        
    def quit_fun(self):
        self.close()
        
    def sign_fun(self):
        name = self.name_line.text()
        pw = self.pw_line.text()
        
        if name == '' or pw == '':
            QMessageBox.critical(self, "ERROR", "Please input name and  password.",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok);
            return
        
        # The user name has hashed(sha256) once while the pass word hashed(sha256) twice.
        hs = hashlib.sha256()
        hs.update(name.encode('utf8'))
        name_val = hs.hexdigest()
        
        hs.update(pw.encode('utf8'))
        pw_val = hs.hexdigest()
        hs.update(pw_val.encode('utf8'))
        pw_val = hs.hexdigest()
        
        if name_val != self.user_name or pw_val != self.pass_word:
            QMessageBox.critical(self, "ERROR", "Name or password is not ture.",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok);
            return
        # If match open the back-stage window.
        self.m = MainWindow()
        self.m.setStyleSheet(self.style)
        self.m.show()
        self.close()

########################################################################################################
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    styleFile = './res/style.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    s = SignIn(qssStyle)
    s.show()
    s.setStyleSheet(qssStyle)
    sys.exit(app.exec_())
