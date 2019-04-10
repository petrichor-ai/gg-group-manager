import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('DeviceDefinition')
log.setLevel(logging.DEBUG)



class DeviceDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, devices, tags={}):
        ''' Create a Greengrass Group Device Definition.
        '''
        response = {}
        try:
            response = self._gg.create_device_definition(
                InitialVersion={
                    'Devices': devices
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Devices Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Devices Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Device Definition.
        '''
        response = self._gg.get_device_definition(
            DeviceDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Device Definition.
        '''
        response = self._gg.delete_device_definition(
            DeviceDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Device Definition.
        '''
        response = self._gg.update_device_definition(
            DeviceDefinitionId=definitionId
        )
        return response


