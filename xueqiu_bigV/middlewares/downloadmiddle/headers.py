import random
from bigv_users.bigv_users import CrawlerBigvUsers

from ...conf.config import USER_AGENT, HEADERS, LOGIN_COOKIES


class UserAgentMiddleWare(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT)

        if user_agent:
            request.headers.update({'User-Agent': user_agent})
        request.headers.update(HEADERS)

        if request.meta.get('login_cookie') is True:
            # request.cookies = CrawlerBigvUsers._get_cookie(random.choice(LOGIN_COOKIES))
            # print request.cookies
            pass


