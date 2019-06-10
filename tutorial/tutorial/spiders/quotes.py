# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem
class QuotesSpider(scrapy.Spider):
    """每个项目唯一的名字, 用来区分不同的的Spider"""
    name = 'quotes'
    """允许爬取的域名,如果初始或后续的请求链接不是这个域名下的,则请求链接会被过滤掉"""
    allowed_domains = ['quotes.toscrape.com']
    """包含了Spider在启动时爬取的url列表,初始请求由它来定义"""
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        """
        Spider的一个方法。默认情况下,被调用时start_urls里面的链接构成的请求完成下载执行后,返回的响应
    就会作为唯一的参数传递给这个函数。该方法负责解析返回的响应、提取数据或者进一步生成要处理的请求。
        :param response:
        :return:
        """
        quotes = response.css(".quote")
        for quote in quotes:
            """如此一来,首页的所有内容被解析出来,并被赋值成了一个个QuoteItem"""
            item = QuoteItem()
            item["text"] = quote.css(".text::text").extract_first()
            item["author"] = quote.css(".author::text").extract_first()
            item["tags"] = quote.css(".tags .tag::text").extract()
            yield item

        """得到下一页的链接 并调用这个函数进行解析"""
        next = response.css(".next a::attr('href')").extract_first()
        """if    next='/page/2'      url =http://quotes.toscrape.com/page/2    
        urljoin()方法是把start_urls和next一起构造为一个决定路径"""
        url = response.urljoin(next)
        """回调函数  当指定了该回调函数的请求完成之后,获取到响应,引擎会将该响应作为参数传递给这个回调函数
        回调函数进行解析或生成下一个请求   回调函数即是parse()
        
        会处理第二页、第三页   这样爬虫就进入了一个循环,直到最后一页"""
        yield scrapy.Request(url=url, callback=self.parse)