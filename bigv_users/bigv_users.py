# -*- coding: utf-8 -*-
import re
import urllib
import json
import time
from random import choice

import requests

from xueqiu_bigV.conf.base import BaseConfig
from xueqiu_bigV.conf.config import ANON_COOKIES, HEADERS, USER_AGENT, BIGV_NAMES


class CrawlerBigvUsers(object):
    def __init__(self):
        self.mongo = BaseConfig()
        self.mongo.create_unique_index(self.mongo.user, 'usr_id')

        self.url = 'https://xueqiu.com/u?q={user}&page=1'
        self.user_rule = re.compile(r'SNB\.data\.searchUser = (?P<users_list>{.*?});', re.S)

    @staticmethod
    def _get_cookie(cookie_str):
        cookie_list = []

        for s in cookie_str.split(';'):
            item = s.strip()
            cookie_list.append(item.split('=', 1))
        return dict(cookie_list)

    def get_html(self, url, headers=None, cookies=None, **kwargs):
        required_headers = headers or HEADERS
        required_headers.update({'User-Agent': choice(USER_AGENT)})
        required_cookie = cookies or self._get_cookie(choice(ANON_COOKIES))

        for _ in range(3):
            try:
                response = requests.get(url, headers=required_headers, cookies=required_cookie, timeout=30, **kwargs)
                return response.content
            except Exception as e:
                print("Get html error: type <{}>, msg <{}>".format(e.__class__, e))
        return ''

    @staticmethod
    def get_user(user_verbose):
        verbose_rule = re.compile(r'<.*?>|\s+', re.S)
        return verbose_rule.sub('', user_verbose)

    def crawl_users(self):
        for user_name in BIGV_NAMES:
            user_info = {'name': user_name}
            url = self.url.format(user=urllib.quote_plus(user_name.encode('u8')))
            m_obj = self.user_rule.search(self.get_html(url))
            users_list = m_obj.groupdict()['users_list']
            users_python = json.loads(users_list)

            for user in users_python['users']:
                if user_name == self.get_user(user['screen_name']):
                    user_info['usr_id'] = str(user['id'])
                    self.mongo.insert2mongo(self.mongo.user, user_info)
            time.sleep(2)
        self.mongo.close()


if __name__ == '__main__':
    CrawlerBigvUsers().crawl_users()




