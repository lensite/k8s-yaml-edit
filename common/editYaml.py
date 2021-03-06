import yaml


class Deployment:
    def __init__(self, file_name="yaml_file/deployment.yml"):
        self.file_name = file_name

    def read_file(self):
        file_name = self.file_name
        with open(file_name, 'r') as yaml_file:
            yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        return yaml_data

    def write_file(self, par_list):
        file_name = self.file_name
        yaml_data = self.read_file()
        with open(file_name, 'w') as yaml_file:
            yaml_data['metadata']['name'] = par_list['app_name']
            yaml_data['metadata']['labels']['app'] = par_list['app_name']
            yaml_data['metadata']['namespace'] = par_list['namespace']
            yaml_data['spec']['replicas'] = par_list['replicas']
            yaml_data['spec']['selector']['matchLabels']['app'] = par_list['app_name']
            yaml_data['spec']['template']['metadata']['labels']['app'] = par_list['app_name']
            containers_list = yaml_data['spec']['template']['spec']['containers']
            for i in containers_list:
                i['name'] = par_list['app_name']
            yaml.dump(yaml_data, yaml_file)

    def app_base_info(self, par_list):
        file_name = self.file_name
        yaml_data = self.read_file()
        with open(file_name, 'w') as yaml_file:
            yaml_data['metadata']['name'] = par_list['app_name']
            yaml_data['metadata']['labels']['app'] = par_list['app_name']
            yaml_data['metadata']['namespace'] = par_list['namespace']
            yaml_data['spec']['replicas'] = par_list['replicas']
            yaml_data['spec']['selector']['matchLabels']['app'] = par_list['app_name']
            yaml_data['spec']['template']['metadata']['labels']['app'] = par_list['app_name']
            yaml.dump(yaml_data, yaml_file)

    def containers_info(self, par_list):
        file_name = self.file_name
        yaml_data = self.read_file()
        with open(file_name, 'w') as yaml_file:
            containers_list = yaml_data['spec']['template']['spec']['containers']
            for i in containers_list:
                i['name'] = yaml_data['metadata']['name']
                for j in i['ports']:
                    j['containerPort']=par_list['containerPort']
                i['image'] = "%s:%s" % (par_list['image_name'], par_list['image_tag'])
            yaml.dump(yaml_data, yaml_file)

if __name__ == '__main__':
    yaml_data=Deployment("../yaml_file/nginx.yml").read_file()
    print(yaml_data)