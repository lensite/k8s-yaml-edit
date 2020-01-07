import tornado.web
from common.editYaml import Deployment
from common.appInfo import AppInfo


class APPBaseInfo(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        app_name = self.get_argument('app_name')
        namespace = self.get_argument('namespace')
        replicas = self.get_argument('replicas')
        status = self.get_argument('status')
        print(status)
        par_list = {"app_name": app_name,
                    "namespace": namespace,
                    "replicas": int(replicas)}
        Deployment().app_base_info(par_list)
        self.redirect('containers_info.html')


class ContainersInfo(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        image_name = self.get_argument('image_name')
        image_tag = self.get_argument('image_tag')
        containerPort = self.get_argument('containerPort')
        par_list = {"image_name": image_name,
                    "image_tag": image_tag,
                    "containerPort": int(containerPort)}
        Deployment().containers_info(par_list)
        self.write('The application is created')


class AppList(tornado.web.RequestHandler):
    def get(self):
        applist = AppInfo().get_app_list()
        self.render("app_list.html", applist=applist)
