import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ResourceDefinition')
log.setLevel(logging.DEBUG)



class ResourceDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, resources, tags={}):
        ''' Create a Greengrass Group Resource Definition.
        '''
        response = {}
        try:
            response = self._gg.create_resource_definition(
                InitialVersion={
                    'Resources': resources
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Resource Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Resource Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Resource Definition.
        '''
        response = self._gg.get_resource_definition(
            ResourceDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Resource Definition.
        '''
        response = self._gg.delete_resource_definition(
            ResourceDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Resource Definition.
        '''
        response = self._gg.update_resource_definition(
            ResourceDefinitionId=definitionId
        )
        return response
