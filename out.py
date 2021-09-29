import pymongo
import os

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

articles_db = client['Acticles']

articles_col = articles_db['articles']

for article in articles_col.find():
    print(article['title'])
    file_name = article['title']
    file_content = article['content']

    with open('./files/{}.md'.format(file_name), 'w', encoding='utf-8') as f:
        f.write(file_content)
        f.close()