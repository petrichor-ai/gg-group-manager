import boto3
import json
import logging

from botocore.exceptions import ClientError

from gg_manager.definitions.thing import ThingDefinition

from gg_manager.utilities.gg_stacks import Stack
from gg_manager.utilities.gg_config import Config
from gg_manager.utilities.gg_schema import Schema, thingSchema
from gg_manager.utilities.gg_cfntmp import CFNTemplate, CFN_THING_TEMPLATE_BODY


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

        self._thngDef = ThingDefinition(s)

        self._stack   = Stack(s)
        self._config  = Config()
        self._cfntmp  = CFNTemplate()


    def create(self, configJson='', configFile=''):
        ''' Create an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        for thing in self._config.get('Devices', []):

            self._cfntmp.load_body(CFN_THING_TEMPLATE_BODY)

            thing['certificateArn'] = self._thngDef.generate_key_certs(
                thing['thingName']
            )
            self._thngDef.formatDefinition(thing, self._cfntmp)

            self._stack.create(thing, self._cfntmp)


    def update(self, configJson='', configFile=''):
        ''' Update an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        for thing in self._config.get('Devices', []):

            self._cfntmp.load_body(CFN_THING_TEMPLATE_BODY)

            self._stack.update(thing, self._cfntmp)


    def remove(self, configJson='', configFile=''):
        ''' Remove an AWS IoT Thing.
        '''
        if configJson:
            schema = Schema(thingSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(thingSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        for thing in self._config.get('Devices', []):

            self._stack.delete(thing, self._cfntmp)

