import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupThings')
log.setLevel(logging.DEBUG)



class GroupThings(object):


    def __init__(self, s):

        self._iot = s.client('iot')


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
