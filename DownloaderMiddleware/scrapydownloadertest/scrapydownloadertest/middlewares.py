import random

class RandomUserAgent(object):
    def __init__(self):
        self.user_agents = [
            "AAAAA", "BBBBB", "CCCCC", "DDDDD"
        ]

    def process_request(self, request, spider):
        """
            Request被Scrapy引擎调度给Downloader之前,process_requests()方法就会被调用,
        也就是Request从队列里调度出来到Downloader下载执行之前,都可以用process_request()
        方法对Request进行处理
        :param request:  Request对象,被处理的Request
        :param spider:   Spider对象,此Request对应的Request
        :return:  返回值需要是以下几种类型
        None：                         Scrapy将继续处理该Request,接着执行其它DownloaderMiddlewares的process_request()方法,
        一直到Downloader把Request执行后得到Response才结束。这个过程其实就是修改Request的过程。不同的Downloader Middleware
        按照设置的优先级顺序依次对Request进行修改,最后送至Downloader执行.


        Response对象：                 当返回为Reqponse对象时,更低优先级的DownloaderMiddleware的process_request()和
        process_exception()方法就不会被继续调用,每个DownloaderMiddleWare的process_response()方法转而被依次调用。
        调用完毕后,直接将Response对象发送给Spider来处理。


        Request对象之一：              当返回为Request对象时,更低优先级的DownloaderMiddleware的process_request()方法会停止
        执行。这个Request会重新放到调度队列里,其实他就是一个全新的Request,等待被调度。如果被Scheduler调度了,那么所有的
        DownloaderMiddleware的process_request()方法会被重新按照顺序执行。


        IgnoreRequest异常：             如果IgnoreRequest异常抛出,则所有的Downloader Middleware的process_exception()方法会
        依次执行。如果没有一个方法处理这个异常,那么Request的errorback()方法就会回调。如果该异常还没有被处理,便会被忽略。
        """
        request.headers["USER-AGENT"] = random.choice(self.user_agents)


    def process_response(self,request,response,spider):
        """
             Downloader执行Request下载之后,会得到对应的Response.    Scrapy引擎便会将Respponse发送给Spider进行解析.在发送之前,
        都可以用process_response()方法对Response进行处理.方法的返回值必须为



        :param request:          Request对象,此响应对应的Request
        :param response:         Response对象,此被处理的Response
        :param spider:           Spider对象,此Response对应的Spider
        :return:  下面三个中的一种




        Request对象：            当返回为Request对象时,更低优先级的DownloaderMiddleware的process_response()方法不会继续调用。
        该Request对象会重新放到调度队列里等待被调度,它相当于一个全新的Request。然后,该Request会被process_request()依次处理。




        Response对象：           当返回为Response对象时,更低优先级的DownloaderMiddleware的process_response()方法会继续调用,
        继续对该Response对象进行处理。



        IgnoreRequest异常：      如果IgnoreRequest异常抛出,则Request的errorback()方法会回调。如果该异常还没有被处理,那么他便
        会被忽略。
        """


        response.status = 201  # 这里不能乱写 一定要是StatusCode里面有的
        # 被修改的Response就会被发送到Spider
        return response