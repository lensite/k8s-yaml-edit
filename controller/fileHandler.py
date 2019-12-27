import tornado.web
from common.editYaml import Deployment


class APPBaseInfo(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        if self.get_argument('app_name'):
            app_name = self.get_argument('app_name')
            namespace = self.get_argument('namespace')
            replicas = self.get_argument('replicas')
            par_list = {"app_name": app_name,
                        "namespace": namespace,
                        "replicas": int(replicas)}
            Deployment().app_base_info(par_list)
            self.redirect('containers_info.html')
        elif self.get_argument('image_name'):
            image_name = self.get_argument('image_name')
            image_tag = self.get_argument('image_tag')
            res_limit = self.get_argument('res_limit')
            par_list = {"image_name": image_name,
                        "image_tag": image_tag,
                        "res_limit": res_limit}
            Deployment().containers_info(par_list)
            self.write('The application is created')


class ContainersInfo(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        image_name = self.get_argument('image_name')
        image_tag = self.get_argument('image_tag')
        res_limit = self.get_argument('res_limit')
        par_list = {"image_name": image_name,
                    "image_tag": image_tag,
                    "res_limit": res_limit}
        Deployment().containers_info(par_list)
        self.write('The application is created')
