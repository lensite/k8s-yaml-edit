import tornado.web
from common.editYaml import Deployment
from common.appInfo import AppInfo
import yaml


class APPBaseInfo(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        app_name = self.get_argument('app_name')
        namespace = self.get_argument('namespace')
        replicas = self.get_argument('replicas')
        status = self.get_argument('status')
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
        yaml_data = Deployment().read_file()
        app_res=AppInfo().create_app(yaml.dump(yaml_data))
        if app_res["status"] != "Failure":
            self.redirect("/app_list")
        else:
            self.write(app_res["message"])


class AppList(tornado.web.RequestHandler):
    def get(self):
        applist = AppInfo().get_app_list()
        self.render("app_list.html", applist=applist)
