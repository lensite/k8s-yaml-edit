import tornado.ioloop
import tornado.web
import os
import main
from controller.appHandler import *


def make_app():
    return tornado.web.Application(
        [(r"/.*.html", main.Index),
         (r"/", main.Index),
         (r"/app_base", APPBaseInfo),
         (r"/containers_info",ContainersInfo),
         (r"/app_list", AppList)
         ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"))
