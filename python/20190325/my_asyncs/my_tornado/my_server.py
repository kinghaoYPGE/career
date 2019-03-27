import tornado.ioloop
import tornado.web
import time
from tornado import gen


class MainHandler(tornado.web.RequestHandler):
    # @gen.coroutine
    async def get(self):
        print(time.time())
        # yield from gen.sleep(3)
        await gen.sleep(3)
        self.write("Hello, world")
        print(time.time())


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    print('server start on 8080...')
    tornado.ioloop.IOLoop.current().start()
