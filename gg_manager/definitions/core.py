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


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Core Definition.
        '''
        thingName       = config['Cores'][0]['thingName']
        thingSyncShadow = config['Cores'][0]['SyncShadow']
        thingArn        = self.fetchThingArn(thingName)
        thingCertArn    = self.fetchThingCertArn(thingName)

        coreTemplate = \
        '''
        [
            {{
                \"Id\": \"{thingName}\",
                \"ThingArn\": \"{thingArn}\",
                \"CertificateArn\": \"{certArn}\",
                \"SyncShadow\": \"{syncShadow}\"
            }}
        ]
        '''.format(
            thingName=thingName,
            thingArn=thingArn,
            certArn=thingCertArn,
            syncShadow=thingSyncShadow
        )
        cfntmp.format(cores=coreTemplate)


    def fetchThingArn(self, thingName):

        response = self._iot.describe_thing(
            thingName=thingName
        )
        return response['thingArn']


    def fetchThingCertArn(self, thingName):

        response = self._iot.list_thing_principals(
            thingName=thingName
        )
        return response['principals'][0]
