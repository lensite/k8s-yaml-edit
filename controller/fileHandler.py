import tornado.web
from controller.edit_yaml import yaml_ctrl


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
        yaml_ctrl().write_file(par_list)
        self.redirect('form_basic.html')
