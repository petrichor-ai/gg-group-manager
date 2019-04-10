import boto3
import fire
import json
import logging

from botocore.exceptions import ClientError

from definitions.connector import ConnectorDefinition
from definitions.core import CoreDefinition
from definitions.device import DeviceDefinition
from definitions.function import FunctionDefinition
from definitions.logger import LoggerDefinition
from definitions.resource import ResourceDefinition

from utilities.state import GroupState



class GroupCommands(object):

    def __init__(self):
        super(GroupCommands, self).__init__()

        s = boto3.session.Session()
        if not s.region_name:
            raise Exception("AWS Credentials and Region must be setup")

        self._state = GroupState()

        self._connectorDef = ConnectorDefinition(s, self._state)
        self._coreDef      = CoreDefinition(s, self._state)
        self._deviceDef    = DeviceDefinition(s, self._state)
        self._functionDef  = FunctionDefinition(s, self._state)
        self._loggerDef    = LoggerDefinition(s, self._state)
        self._resourceDef  = ResourceDefinition(s, self._state)


    def create(self):
        self._state.load()


    def update(self):
        self._state.load()


    def deploy(self):
        self._state.load()


    def remove(self):
        self._state.load()



def main():
    fire.Fire(GroupCommands())



if __name__ == '__main__':
    main()
