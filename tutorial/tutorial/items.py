# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
"""Item是保存爬取数据的容器,它的使用方法和字典类似。不过,Item多了额外的保护机制,可以避免拼写错误或者定义字段错误"""


"""这个类的名字可以 自定义"""
class QuoteItem(scrapy.Item):
    """
    Item可以理解为一个字典  不过在声明的时候需要实例化
    然后依次用刚才解析的结果赋值Item的每一个字段,最后将Item返回即可。
    """
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
