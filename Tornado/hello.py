import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.write("<br />")
        self.write("jesse")

def init_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        debug=True
    )

if __name__ == "__main__":
    app = init_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
