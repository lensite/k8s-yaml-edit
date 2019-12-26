import tornado.ioloop
import tornado.web
import urls

class Index(tornado.web.RequestHandler):
    def get(self):
        path = self.request.path
        print(path)
        if path == '/':
            self.render('index.html')
        else:
            self.render(path.strip('/'))
if __name__ == "__main__":
    app = urls.make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
