import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ConnectorDefinition')
log.setLevel(logging.DEBUG)



class ConnectorDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, connectors, tags={}):
        ''' Create a Greengrass Group Connector Definition.
        '''
        response = {}
        try:
            response = self._gg.create_connector_definition(
                InitialVersion={
                    'Connectors': connectors
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Connector Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Connector Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Connector Definition.
        '''
        response = self._gg.get_connector_definition(
            ConnectorDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Connector Definition.
        '''
        response = self._gg.delete_connector_definition(
            ConnectorDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Connector Definition.
        '''
        response = self._gg.update_connector_definition(
            ConnectorDefinitionId=definitionId
        )
        return response

