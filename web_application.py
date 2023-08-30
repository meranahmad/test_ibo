import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, World! meran test done. edited at git hub</h1><h2>test test</h2>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    print("Server started at http://localhost:8080/")
    tornado.ioloop.IOLoop.current().start()

