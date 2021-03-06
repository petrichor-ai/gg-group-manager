import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ResourceDefinition')
log.setLevel(logging.DEBUG)



class ResourceDefinition(object):


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Resource Definition.
        '''
        resources = []

        for resource in config.get('Resources', []):
            resourceId        = resource['Id']
            resourceName      = resource['Name']
            resourceContainer = resource['Container']

            resources.append({
                "Id": resourceId,
                "Name": resourceName,
                "ResourceDataContainer": resourceContainer
            })

        cfntmp.format(resources=json.dumps(resources))
