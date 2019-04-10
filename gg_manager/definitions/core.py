import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('CoreDefinition')
log.setLevel(logging.DEBUG)



class CoreDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, cores, tags={}):
        ''' Create a Greengrass Group Core Definition.
        '''
        response = {}
        try:
            response = self._gg.create_core_definition(
                InitialVersion={
                    'Cores': cores
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Core Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Core Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Core Definition.
        '''
        response = self._gg.get_core_definition(
            CoreDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Core Definition.
        '''
        response = self._gg.delete_core_definition(
            CoreDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Core Definition.
        '''
        response = self._gg.update_core_definition(
            CoreDefinitionId=definitionId
        )
        return response
