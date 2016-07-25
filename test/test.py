from xueqiu_bigV import settings

from scrapy.crawler import CrawlerProcess
# from scrapy.core.downloader.webclient import
from xueqiu_bigV.spiders.bigv_spider import XqBigvSpider

_settings = {_attr: getattr(settings, _attr) for _attr in dir(settings) if not _attr.startswith('_')}

crawler = CrawlerProcess(_settings)
crawler.crawl(XqBigvSpider)
crawler.start()


