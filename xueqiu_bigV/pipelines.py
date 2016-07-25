# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

from .conf.base import BaseConfig


class XueqiuBigvPipeline(object):
    def open_spider(self, spider):
        self.mongo = BaseConfig()
        self.mongo.create_unique_index(self.mongo.cubes, 'cube_id')

    def close_spider(self, spider):
        self.mongo.close()

    def process_item(self, item, spider):
        data = item['cubes']
        data['crt'] = datetime.now()
        cube_find = self.mongo.cubes.find_one({'cube_id': data['cube_id']})

        if cube_find:
            self.mongo.cubes.remove({'cube_id': data['cube_id']})

        data['rebalancing_histories'] = item['rebalance_list']
        self.mongo.insert2mongo(self.mongo.cubes, data)
        return item
