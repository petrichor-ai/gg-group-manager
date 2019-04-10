import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('FunctionDefinition')
log.setLevel(logging.DEBUG)



class FunctionDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, functions, tags={}):
        ''' Create a Greengrass Group Function Definition.
        '''
        response = {}
        try:
            response = self._gg.create_function_definition(
                InitialVersion={
                    'Functions': functions
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Function Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Function Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Function Definition.
        '''
        response = self._gg.get_function_definition(
            FunctionDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Function Definition.
        '''
        response = self._gg.delete_function_definition(
            FunctionDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Function Definition.
        '''
        response = self._gg.update_function_definition(
            FunctionDefinitionId=definitionId
        )
        return response
