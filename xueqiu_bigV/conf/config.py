# -*- coding: utf-8 -*-
from __future__ import unicode_literals

BIGV_HOST = '192.168.100.20'
BIGV_PORT = 27017
BIGV_DB = 'py_crawl'
BIGV_CUBES = 'bigv_cubes'
BIGV_USR = 'bigv_user'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'xueqiu.com',
    'Upgrade-Insecure-Requests': '1'
 }

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    u'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
    u'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
    u'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    u'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    u'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    u'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)',
    u'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    u'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607)',
    u'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
    u'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0',
    u'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0',
    u'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20100101 Firefox/4.0b7',
    u'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b6pre) Gecko/20100903 Firefox/4.0b6pre',
]

ANON_COOKIES = [
    # google
    's=2p3511x82d; bid=08c8b3f3ccb957b64793063dd80578ed_iqx700yc; xq_a_token=112e1f7801e730f33e1fe31c8bda1de0935db9b2; '
    'xq_r_token=0fd1c5ad06a1272407d710720be1d6eb2a0d6472; Hm_lvt_1db88642e346389874251b5a1eded6e3=1469096680; '
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1469179847',

    # google

    # IE

    # Firefox

    # Firefox

]


LOGIN_COOKIES = [
    's=2p3511x82d; bid=08c8b3f3ccb957b64793063dd80578ed_iqx700yc; Hm_lvt_1db88642e346389874251b5a1eded6e3=1469096680; '
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1469181268; xq_a_token=0430697aecf0146bbd9794fb500eeab21f6d4acb; '
    'xqat=0430697aecf0146bbd9794fb500eeab21f6d4acb; xq_r_token=39297820ea0f678d35cc9698ff5e82903e1b7a77; '
    'xq_is_login=1; u=1248804871; xq_token_expire=Tue%20Aug%2016%202016%2017%3A54%3A55%20GMT%2B0800%20(CST)',
]

BIGV_NAMES = [
    '小小辛巴',
    '梁宏',
    '东博老股民',
    '弱弱的投资者',
    'DAVID自由之路',
    '释老毛',
    '路过十八次',
    '不明真相的群众',
    '那一水的鱼',
    'GT周',
    '昆山法律',
    'Dean_丁丁',
    '重力加速度',
    '亿利达',
    '雷公资本',
    '国老',
    '水晶苍蝇拍',
]
