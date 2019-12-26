import tornado.ioloop
import tornado.web
import os
import main
from controller.fileHandler import FileHandler


def make_app():
    return tornado.web.Application(
        [(r"/.*.html", main.Index),
         (r"/yaml", FileHandler),
         ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"))
