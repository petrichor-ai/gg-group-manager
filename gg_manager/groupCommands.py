import boto3
import fire
import json
import logging

from botocore.exceptions import ClientError

from definitions.connector import ConnectorDefinition
from definitions.core import CoreDefinition
from definitions.device import DeviceDefinition
from definitions.function import FunctionDefinition
from definitions.group import GroupDefinition
from definitions.logger import LoggerDefinition
from definitions.resource import ResourceDefinition
from definitions.subscription import SubscriptionDefinition

from utilities.group_config import GroupConfig
from utilities.group_stacks import GroupStack
from utilities.group_cfntmp import CFNTemplate, CFN_TEMPLATE_BODY



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

        self._stack   = GroupStack(s)
        self._config  = GroupConfig()


    def create(self, configJson='', configFile=''):
        ''' Create a Greengrass Group.
        '''
        if configJson:
            self._config.load_from_json(configJson)
        else:
            self._config.load_from_file(configFile)

        cfntmp = CFNTemplate(CFN_TEMPLATE_BODY)

        self._grupDef.formatDefinition(self._config, cfntmp)
        self._coreDef.formatDefinition(self._config, cfntmp)
        self._devcDef.formatDefinition(self._config, cfntmp)
        self._funcDef.formatDefinition(self._config, cfntmp)
        self._loggDef.formatDefinition(self._config, cfntmp)
        self._rsrcDef.formatDefinition(self._config, cfntmp)
        self._subsDef.formatDefinition(self._config, cfntmp)

        self._stack.create(self._config, cfntmp)


    def update(self, configJson='', configFile=''):
        ''' Update a Greengrass Group.
        '''
        if configJson:
            self._config.load_from_json(configJson)
        else:
            self._config.load_from_file(configFile)

        cfntmp = CFNTemplate(CFN_TEMPLATE_BODY)

        self._grupDef.formatDefinition(self._config, cfntmp)
        self._coreDef.formatDefinition(self._config, cfntmp)
        self._devcDef.formatDefinition(self._config, cfntmp)
        self._funcDef.formatDefinition(self._config, cfntmp)
        self._loggDef.formatDefinition(self._config, cfntmp)
        self._rsrcDef.formatDefinition(self._config, cfntmp)
        self._subsDef.formatDefinition(self._config, cfntmp)

        output = self._stack.output(self._config)

        groupId = output['Id']
        self._grupDef.resetDefinition(groupId)

        self._stack.update(self._config, cfntmp)


    def deploy(self, configJson='', configFile=''):
        ''' Deploy a Greengrass Group.
        '''
        if configJson:
            self._config.load_from_json(configJson)
        else:
            self._config.load_from_file(configFile)

        cfntmp = CFNTemplate(CFN_TEMPLATE_BODY)

        output = self._stack.output(self._config)

        groupId        = output['Id']
        groupVersionId = output['LatestVersion']
        self._grupDef.deployDefinition(groupId, groupVersionId)


    def remove(self, configJson='', configFile=''):
        ''' Remove a Greengrass Group.
        '''
        if configJson:
            self._config.load_from_json(configJson)
        else:
            self._config.load_from_file(configFile)

        cfntmp = CFNTemplate(CFN_TEMPLATE_BODY)

        output = self._stack.output(self._config)

        groupId = output['Id']
        self._grupDef.resetDefinition(groupId)

        self._stack.delete(self._config, cfntmp)



def main():
    fire.Fire(GroupCommands())



if __name__ == '__main__':
    main()
