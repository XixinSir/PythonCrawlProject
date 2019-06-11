# -*- coding: utf-8 -*-
import scrapy
"""
本项目想修改User-Agent,实现方法有两种:
1、直接在settings.py里面添加User-Agent的定义即可
2、通过middlewares设置


如果要对Response进行处理的话,就用process_response()方法
"""

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        # 添加日志输出
        self.logger.debug(response.text)
        self.logger.debug("Status Code: " + str(response.status))


