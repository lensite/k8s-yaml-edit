import tornado.web
from common.editYaml import Deployment


class FileHandler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(200)

    def post(self, *args, **kwargs):
        app_name = self.get_argument('app_name')
        namespace = self.get_argument('namespace')
        replicas = self.get_argument('replicas')
        par_list = {"app_name": app_name,
                    "namespace": namespace,
                    "replicas": int(replicas)}
        Deployment().write_file(par_list)
        self.redirect('containers_info.html')
