import os
import yaml


def get_config(filepath=None):
    """
    Get the config fie and returns it as dictionary.
    """
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


def find(d, tag):
    """
    Finds given tag from a dictionary.
    Thnaks to Apollo2020, https://stackoverflow.com/a/37626981
    """
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, tag):
                yield i


def get_value(tag):
    """
    Returns the first occurance of the tag.
    """
    settings = get_config()
    return [i for i in find(settings, tag)][0]
