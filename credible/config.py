import os
import yaml


def get_config(filepath=None):
    # get config
    if filepath is not None:
        _filepath = filepath
    else:
        _filepath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../config.yaml"))

    # load config
    with open(_filepath, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.Loader)

    return config
