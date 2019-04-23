import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('DeviceDefinition')
log.setLevel(logging.DEBUG)



class DeviceDefinition(object):


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Device Definition.
        '''
        devices = []

        for device in config['Devices']:
            thingName        = device['thingName']
            thingSyncShadow  = device['SyncShadow']
            thingUseExisting = device['useExistingThing']

            if thingUseExisting:
                thingArn        = self.fetchThingArn(thingName)
                thingCertArn    = self.fetchThingCertArn(thingName)

                devices.append({
                    "Id": thingName,
                    "ThingArn": thingArn,
                    "CertificateArn": thingCertArn,
                    "SyncShadow": thingSyncShadow
                })

        cfntmp.format(devices=json.dumps(devices))


    def fetchThingArn(self, thingName):
        ''' Fetch a Thing's Arn.
        '''
        response = self._iot.describe_thing(
            thingName=thingName
        )
        return response['thingArn']


    def fetchThingCertArn(self, thingName):
        ''' Fetch a Thing's Certificate Arn.
        '''
        response = self._iot.list_thing_principals(
            thingName=thingName
        )
        return response['principals'][0]
