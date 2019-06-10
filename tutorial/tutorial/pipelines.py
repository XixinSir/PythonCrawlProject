from scrapy.exceptions import DropItem
import pymongo

class TextPipeline(object):
    def __init__(self):
        # 限制长度为50
        self.limit = 50

    """每次Spider生成的Item都会作为参数传递过来
    启用Item Pipeline后,Item Pipeline会自动调用这个方法
    process_item()方法必须返回包含数字的字典或者Item对象,或者抛出DropItem异常"""
    def process_item(self, item, spider):
        if item["text"]:
            if len(item["text"]) > self.limit:
                item["text"] = item["text"][0:self.limit].rstrip() + "......"
            return item
        else:
            return DropItem("Missing Text")

class MongoPipeline(object):
    def __init__(self, mongo_host, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db

    """类方法,用@classmethod标识,是一种依赖注入的方式,它的参数就是crawler
    此方法主要是用来获取settings.py中的配置"""
    @classmethod
    def from_crawler(cls, crawler):
        """通过crawler可以拿到全局配置的每个配置信息:   拿到在settings.py中定义的两个量"""
        return cls(
            mongo_host=crawler.settings.get("MONGO_HOST"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        """当spider开启时,这个方法被调用....这里主要进行了一些初始化操作"""
        self.client = pymongo.MongoClient(self.mongo_host)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        """执行数据插入操作"""
        # 这里也可以直接在settings中定义好表名,在open_spider方法中调用
        name = item.__class__.__name__
        self.db[name].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        """当spider关闭时,这个方法会调用....这里主要将数据库连接关闭"""
        self.client.close()

