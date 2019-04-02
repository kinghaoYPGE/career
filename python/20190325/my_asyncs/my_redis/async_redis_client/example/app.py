# -*- coding:utf-8 -*-

from asyncredis import Client
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.gen
import logging


logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        c = Client()
        # 从 Redis 数据库中获取键值
        async_redis = yield tornado.gen.Task(c.get, "async_redis")
        self.set_header("Content-Type", "text/html")
        self.render("template.html", title="Simple demo", async_redis=async_redis)


application = tornado.web.Application([
    (r'/', MainHandler),
])


# 设置键 async_redis 的值
@tornado.gen.coroutine
def create_test_data():
    c = Client()
    yield c.select(0)
    yield c.set("async_redis", "redis异步客户端")


if __name__ == '__main__':
    create_test_data()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8089)
    print("Demo is run at 0.0.0.0:8080")
    tornado.ioloop.IOLoop.instance().start()
