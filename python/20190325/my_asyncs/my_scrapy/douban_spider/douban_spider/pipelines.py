# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .settings import mongo_db_collection, mongo_host, mongo_db_name, mongo_port


class DoubanSpiderPipeline(object):
    # 初始化mongoDB
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        # 创建mongoDB client
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.post = db[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
