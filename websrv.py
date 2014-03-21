
import tornado.ioloop
import tornado.web
import time


class MainHandler(tornado.web.RequestHandler):

    def get(self, fname):
        try:
            self.write("hello " + fname + "\n")

        except Exception, msg:
            print msg
            self.set_status(404)
            self.write("ERROR HERE")

    def post(self, fname):
        self.set_header('Cache-Control', 'no-cache')
#        data = self.get_argument('ak', 'No data received')
#        self.write(data + "\n")
        self.write(self.request.body + "\n")


application = tornado.web.Application([
    (r"/pt/(.*)", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

