import json
import requests
import datetime
import yaml
import json
from urllib.parse import urljoin


class AppInfo:
    def __init__(self, K8S_URL='http://192.168.12.22:8080'):
        self.K8S_URL = K8S_URL

    def get_app_list(self):
        app_list = []
        app_id = 0
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
        api_path = '/apis/apps/v1/namespaces/default/deployments'
        req = requests.get(urljoin(self.K8S_URL, api_path))
        req_json = json.loads(req.text)
        items = req_json['items']
        for i in items:
            app_id += 1
            app_name = i['metadata']['name']
            creationTime = i['metadata']['creationTimestamp']
            utcTime = datetime.datetime.strptime(creationTime, UTC_FORMAT)
            create_time = utcTime + datetime.timedelta(hours=8)
            labels = i['metadata']['labels']
            replicas = i['spec']['replicas']
            image = i['spec']['template']['spec']['containers'][0]['image']
            app_list.append({'app_id': app_id, 'app_name': app_name,
                             'create_time': str(create_time),
                             'labels': labels,
                             'replicas': replicas,
                             'image': image})
        return app_list

    def create_app(self, yaml_data):
        headers = {"Content-Type": "application/yaml"}
        api_path = '/apis/extensions/v1beta1/namespaces/default/deployments'
        req = requests.post(urljoin(self.K8S_URL, api_path), data=yaml_data, headers=headers)
        res = json.loads(req.text)
        return res


if __name__ == '__main__':
    f = open('../yaml_file/deployment.yml')
    y = yaml.load(f, Loader=yaml.FullLoader)
    yYaml = yaml.dump(y)
    AppInfo().create_app(yYaml)
