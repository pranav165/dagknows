import os
import yaml

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

config_yml_file_name = 'setup_config.yml'
config_yml_path = (os.path.join(PROJECT_ROOT, config_yml_file_name))
with open(config_yml_path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Config(object):
    """"
    Contains the configuration settings
    """
    app = "app"
    app_local = "app_local"
    if "LOCALHOST" in os.environ:
        app = app_local
    app_url = cfg[app]['url']
    email = cfg[app]['email']
    password = cfg[app]['password']
