# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import mongo_db_collection, mongo_db_name, mongo_host, mongo_port
import pymongo

class MySpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class LouSpiderPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection_name = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.post = db[collection_name]

    def process_item(self, item, spider):
        self.post.insert(dict(item))
        with open('courses.txt', 'a') as f:
            line = 'course name: {0}, learned count: {1}, image link: {2}'.format(
                item['name'],
                item['learned'],
                item['image']
            )
            f.write(line+'\n')
        return item
