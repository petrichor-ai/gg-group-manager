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
from utilities.group_cfntmp import GroupCfnTmp, CFN_TEMPLATE_BODY
from utilities.group_stacks import GroupStack




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


    def create(self, configPath):
        config = GroupConfig(configPath)
        cfntmp = GroupCfnTmp(CFN_TEMPLATE_BODY)

        self._grupDef.formatDefinition(config, cfntmp)
        self._coreDef.formatDefinition(config, cfntmp)
        self._devcDef.formatDefinition(config, cfntmp)
        self._funcDef.formatDefinition(config, cfntmp)
        self._loggDef.formatDefinition(config, cfntmp)
        self._rsrcDef.formatDefinition(config, cfntmp)
        self._subsDef.formatDefinition(config, cfntmp)

        print(cfntmp)
        self._stack.create(config, cfntmp)


    def update(self, configPath):
        config = GroupConfig(configPath)
        cfntmp = GroupCfnTmp(CFN_TEMPLATE_BODY)


    def deploy(self, configPath):
        config = GroupConfig(configPath)
        cfntmp = GroupCfnTmp(CFN_TEMPLATE_BODY)


    def remove(self, configPath):
        config = GroupConfig(configPath)
        cfntmp = GroupCfnTmp(CFN_TEMPLATE_BODY)



def main():
    fire.Fire(GroupCommands())



if __name__ == '__main__':
    main()
