import json

from functools import wraps

from .group_schema import groupSchema



def handle_config_error(func):
    """
        This define a decorator to format the HTTP response of the lambda:
        - a status code
        - the body of the response as a string
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            print(e)
            return {}

    return wrapped_func



class GroupConfig(dict):

    def __init__(self):
        pass


    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        return val


    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)


    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)


    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v


    @handle_config_error
    def load_from_json(self, payload):

        conf = groupSchema(use=json.loads).validate(payload)
        self.update(conf)


    @handle_config_error
    def load_from_file(self, payload):

        with open(payload, 'r') as f:
            conf = groupSchema(use=json.load).validate(f)
            self.update(conf)
