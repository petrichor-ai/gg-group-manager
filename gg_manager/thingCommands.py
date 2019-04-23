import boto3
import json
import logging

from botocore.exceptions import ClientError

from utilities.gg_stacks import Stack
from utilities.gg_config import Config
from utilities.gg_schema import Schema, thingSchema
from utilities.gg_cfntmp import CFNTemplate, CFN_THING_TEMPLATE_BODY


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ThingCommands')
log.setLevel(logging.DEBUG)



class ThingCommands(object):

    def __init__(self):
        super(ThingCommands, self).__init__()

        s = boto3.session.Session()
        if not s.region_name:
            raise Exception("AWS Credentials and Region must be setup")

        self._stack  = Stack(s)
        self._config = Config()


    def create(self, configJson='', configFile=''):
        ''' Create an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('Thing Create')


    def update(self, configJson='', configFile=''):
        ''' Update an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('Thing Update')


    def remove(self, configJson='', configFile=''):
        ''' Remove an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)
        print('Thing Remove')
