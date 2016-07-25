# -*- coding: utf-8 -*-
import json
import time
import random
from datetime import datetime

import scrapy

from ..conf.config import LOGIN_COOKIES
from ..conf.base import BaseConfig
from ..items import XueqiuBigvItem
from ..extractor.extractor import UserExtractor
from bigv_users.bigv_users import CrawlerBigvUsers


class XqBigvSpider(scrapy.Spider):
    name = "xq_bigv"
    allowed_domains = ["xueqiu.com"]

    mongo = BaseConfig()

    def __init__(self):
        self.bigv_id = self.mongo.get_users_id
        super(XqBigvSpider, self).__init__()
        self.cube_url = 'https://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=%s&count=50&page=%s'

    def start_requests(self):
        """
        先请求一次雪球网， 保存Cookie
        :return: Scrapy Request instance
        """
        yield self.make_requests_from_url('https://xueqiu.com/')

    def parse(self, response):
        """
        数据库里有雪球大V的id, 不必再去请求雪球网站，减少请求量
        :return: Scrapy Request instance
        """
        for user_id in self.bigv_id:
            url = 'https://xueqiu.com/cubes/list.json?user_id={user_id}&_={ts}'
            yield scrapy.Request(
                url=url.format(user_id=user_id, ts=int(time.time() * 1000)),
                callback=self.user_info,
                meta={'user_id': user_id}
            )
            # print url.format(user_id=user_id, ts=int(time.time() * 1000))

    def user_info(self, response):
        user_info, cubes = UserExtractor(response.meta['user_id'], response.body_as_unicode()).user_cubes

        # 跟新雪球大V信息
        user_obj_id = self.mongo.user.find_one({'usr_id': user_info['usr_id']}, {'_id': 1})

        if user_obj_id:
            self.mongo.user.remove({'_id': user_obj_id['_id']})
        self.mongo.insert2mongo(self.mongo.user, user_info)

        for cube in cubes:
            yield scrapy.FormRequest(
                url=self.cube_url % (cube['cube_id'], 1),
                callback=self.parse_cubes,
                meta={'cube': cube, 'usr_id': response.meta['user_id']},
                cookies=CrawlerBigvUsers._get_cookie(random.choice(LOGIN_COOKIES))
            )

    def parse_cubes(self, response):
        cube = response.meta['cube']
        cube['usr_id'] = response.meta['usr_id']
        pre_cubu_data = response.meta.get('pre_cubu_data', [])

        python_data = json.loads(response.body_as_unicode())
        page = python_data.get('page', 1)
        total_count = python_data.get('totalCount', 50)
        pre_cubu_data.extend(self.get_cube_data(python_data))

        if total_count <= 50 * page:
            yield XueqiuBigvItem(rebalance_list=pre_cubu_data, cubes=cube)
        else:
            yield scrapy.FormRequest(
                url=self.cube_url % (cube['cube_id'], page + 1),
                callback=self.parse_cubes,
                meta={'cube': cube, 'pre_cubu_data': pre_cubu_data, 'usr_id': response.meta['usr_id']},
                cookies=CrawlerBigvUsers._get_cookie(random.choice(LOGIN_COOKIES))
            )

    @staticmethod
    def get_cube_data(data):
        rebalancing = []

        for rebalance in data['list']:
            for each in rebalance['rebalancing_histories']:
                timestrap = int(each['created_at'] / 1000)
                t = datetime.fromtimestamp(timestrap).strftime('%Y-%m-%d %H:%M:%S')
                rebalancing.append({
                    't': t,
                    'stock_name': each['stock_name'],
                    'stock_symbol': each['stock_symbol'],
                    'target_weight': each['target_weight'],
                    'prev_weight_adjusted': each['prev_weight_adjusted']
                })
        return rebalancing

    @staticmethod
    def close(spider, reason):
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)

        XqBigvSpider.mongo.close()



