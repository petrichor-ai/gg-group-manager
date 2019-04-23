import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ConnectorDefinition')
log.setLevel(logging.DEBUG)



class ConnectorDefinition(object):


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Connector Definition.
        '''
        connectors = []

        cfntmp.format(connectors=json.dumps(conectors))
