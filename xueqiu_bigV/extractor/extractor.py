# -*- coding: utf-8 -*-
import re
import time
import json
from datetime import datetime

from bigv_users.bigv_users import CrawlerBigvUsers


class UserExtractor(object):
    def __init__(self, user_id, user_info):
        """
        :param user_id: 用户ID
        :param user_info: 用户基本信息和他的组合
        """
        try:
            self._user = json.loads(user_info)['list']
        except (IndexError, ValueError):
            self._user = {}

        self._user_id = user_id

    @property
    def user_cubes(self):
        cubes = []
        owner_flag = True
        user = {'usr_id': self._user_id, 'crt': datetime.now()}

        for cube in self._user:
            if owner_flag and cube.get('owner'):
                owner_flag = False
                owner = cube['owner']
                user['blog'] = owner.get('url')
                user['discuss'] = owner.get('status_count', 0)
                user['desc'] = owner.get('description', '')
                user['fans'] = owner.get('followers_count', 0)
            cubes.append({'cube_id': cube['symbol'], 'cube_name': cube['name'], 'total_gain': cube['total_gain']})

        user.update(**self.other_info)
        return user, cubes

    @property
    def weibo(self):
        weibo_id = None
        url = 'https://xueqiu.com/account/oauth/user/show.json?source=sina&userid={user}&_={ts}'

        if self._user_id:
            ts = int(time.time() * 1000)
            url = url.format(user=self._user_id, ts=ts)
            js_data = CrawlerBigvUsers().get_html(url) or '{}'

            weibo_id = json.loads(js_data).get('id')
        return weibo_id

    @property
    def stock_ability(self):
        data = {}
        url = 'https://xueqiu.com/%s' % self._user_id
        response = CrawlerBigvUsers().get_html(url)

        stock_rule = re.compile(r'SNB\.profileUser = (.*?)</script>', re.S)
        ability_rule = re.compile(r'<div class="item_content discuss_stock_list">(.*?)</div>', re.S)
        stock_js_data = stock_rule.findall(response)
        ability_html = ability_rule.findall(response)

        if stock_js_data:
            python_data = json.loads(stock_js_data[0])
            data['stocks'] = python_data.get('stocks_count')

        if ability_html:
            data['ability'] = re.compile(r'<.*?>|\s+', re.S).sub('', ability_html[0])

        return data

    @property
    def other_info(self):
        weibo_id = self.weibo
        weibo_url = 'http://weibo.com/%s' % weibo_id if weibo_id else None

        stock_ability = self.stock_ability

        stock_ability.update(weibo=weibo_url)
        return stock_ability
