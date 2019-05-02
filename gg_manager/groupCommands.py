import boto3
import json
import logging

from botocore.exceptions import ClientError

from gg_manager.definitions.connector    import ConnectorDefinition
from gg_manager.definitions.core         import CoreDefinition
from gg_manager.definitions.device       import DeviceDefinition
from gg_manager.definitions.function     import FunctionDefinition
from gg_manager.definitions.group        import GroupDefinition
from gg_manager.definitions.logger       import LoggerDefinition
from gg_manager.definitions.resource     import ResourceDefinition
from gg_manager.definitions.subscription import SubscriptionDefinition

from gg_manager.utilities.gg_stacks import Stack
from gg_manager.utilities.gg_config import Config
from gg_manager.utilities.gg_schema import Schema, groupSchema
from gg_manager.utilities.gg_cfntmp import CFNTemplate, CFN_GROUP_TEMPLATE_BODY


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupCommands')
log.setLevel(logging.DEBUG)



class GroupCommands(object):

    def __init__(self):
        super(GroupCommands, self).__init__()

        s = boto3.session.Session()
        if not s.region_name:
            raise Exception("AWS Credentials and Region must be setup")

        self._connDef = ConnectorDefinition(s)
        self._coreDef = CoreDefinition(s)
        self._devcDef = DeviceDefinition(s)
        self._funcDef = FunctionDefinition(s)
        self._grupDef = GroupDefinition(s)
        self._loggDef = LoggerDefinition(s)
        self._rsrcDef = ResourceDefinition(s)
        self._subsDef = SubscriptionDefinition(s)

        self._stack   = Stack(s)
        self._config  = Config()
        self._cfntmp  = CFNTemplate()


    def create(self, configJson='', configFile=''):
        ''' Create an AWS Greengrass Group.
        '''
        if configJson:
            schema = Schema(groupSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(groupSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        self._cfntmp.load_body(CFN_GROUP_TEMPLATE_BODY)

        self._grupDef.formatDefinition(self._config, self._cfntmp)
        self._coreDef.formatDefinition(self._config, self._cfntmp)
        self._devcDef.formatDefinition(self._config, self._cfntmp)
        self._funcDef.formatDefinition(self._config, self._cfntmp)
        self._loggDef.formatDefinition(self._config, self._cfntmp)
        self._rsrcDef.formatDefinition(self._config, self._cfntmp)
        self._subsDef.formatDefinition(self._config, self._cfntmp)

        self._stack.create(self._config, self._cfntmp)


    def update(self, configJson='', configFile=''):
        ''' Update an AWS Greengrass Group.
        '''
        if configJson:
            schema = Schema(groupSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(groupSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        self._cfntmp.load_body(CFN_GROUP_TEMPLATE_BODY)

        self._grupDef.formatDefinition(self._config, self._cfntmp)
        self._coreDef.formatDefinition(self._config, self._cfntmp)
        self._devcDef.formatDefinition(self._config, self._cfntmp)
        self._funcDef.formatDefinition(self._config, self._cfntmp)
        self._loggDef.formatDefinition(self._config, self._cfntmp)
        self._rsrcDef.formatDefinition(self._config, self._cfntmp)
        self._subsDef.formatDefinition(self._config, self._cfntmp)

        output  = self._stack.output(self._config)
        groupId = output['groupId']
        self._grupDef.resetDefinition(groupId)

        self._stack.update(self._config, self._cfntmp)


    def deploy(self, configJson='', configFile=''):
        ''' Deploy an AWS Greengrass Group.
        '''
        if configJson:
            schema = Schema(groupSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(groupSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        output         = self._stack.output(self._config)
        group          = self._grupDef.fetchGroup(output['groupId'])
        groupId        = group['Id']
        groupVersionId = group['LatestVersion']
        self._grupDef.deployDefinition(groupId, groupVersionId)


    def remove(self, configJson='', configFile=''):
        ''' Remove an AWS Greengrass Group.
        '''
        if configJson:
            schema = Schema(groupSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(groupSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        output  = self._stack.output(self._config)
        group   = self._grupDef.fetchGroup(output['groupId'])
        groupId = group['Id']
        self._grupDef.resetDefinition(groupId)

        self._stack.delete(self._config, self._cfntmp)
