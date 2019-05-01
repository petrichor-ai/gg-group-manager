import boto3
import json
import logging

from botocore.exceptions import ClientError

from gg_manager.utilities.gg_stacks import Stack
from gg_manager.utilities.gg_bucket import Bucket
from gg_manager.utilities.gg_config import Config
from gg_manager.utilities.gg_schema import Schema, funcsSchema
from gg_manager.utilities.gg_cfntmp import CFNTemplate, CFN_FUNCS_TEMPLATE_BODY


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('FuncsCommands')
log.setLevel(logging.DEBUG)



class FuncsCommands(object):

    def __init__(self):
        super(FuncsCommands, self).__init__()

        s = boto3.session.Session()
        if not s.region_name:
            raise Exception("AWS Credentials and Region must be setup")

        self._stack  = Stack(s)
        self._bucket = Bucket(s)
        self._config = Config()
        self._cfntmp = CFNTemplate()


    def create(self, configJson='', configFile=''):
        ''' Create an AWS IoT Function (Lambda).
        '''
        if configJson:
            schema = Schema(funcsSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(funcsSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('create')


    def upload(self, configJson='', configFile=''):
        ''' Upload an AWS IoT Function (Lambda).
        '''
        if configJson:
            schema = Schema(funcsSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(funcsSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        functions = []
        for func in self._config.get('Functions', []):
           codeUri = self._bucket.upload(func)

           tmp = {'CodeUri': codeUri}
           tmp.update(func)
           functions.append(tmp)
        return functions


    def deploy(self, configJson='', configFile=''):
        ''' Deploy an AWS IoT Function (Lambda).
        '''
        if configJson:
            schema = Schema(funcsSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(funcsSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('deploy')


    def remove(self, configJson='', configFile=''):
        ''' Remove an AWS IoT Function (Lambda).
        '''
        if configJson:
            schema = Schema(funcsSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(funcsSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('remove')
