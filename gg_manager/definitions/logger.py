import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('LoggerDefinition')
log.setLevel(logging.DEBUG)



class LoggerDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, loggers, tags={}):
        ''' Create a Greengrass Group Logger Definition.
        '''
        response = {}
        try:
            response = self._gg.create_logger_definition(
                InitialVersion={
                    'Loggers': loggers
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Loggers Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Loggers Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Logger Definition.
        '''
        response = self._gg.get_logger_definition(
            LoggerDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Logger Definition.
        '''
        response = self._gg.delete_logger_definition(
            LoggerDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Logger Definition.
        '''
        response = self._gg.update_logger_definition(
            LoggerDefinitionId=definitionId
        )
        return response
