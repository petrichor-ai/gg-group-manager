import boto3
import json
import logging
import os

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('ThingDefinition')
log.setLevel(logging.DEBUG)



class ThingDefinition(object):


    def __init__(self, s):

        self._region         = s.region_name
        self._sts            = s.client('sts')
        self._accountId      = self._sts.get_caller_identity().get('Account')
        self._gg             = s.client('greengrass')
        self._iot            = s.client('iot')
        self._exportPath     = os.path.join(os.getcwd(), 'gg_certs')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation IoT Thing Definition.
        '''
        thingName      = config['thingName']
        certificateArn = config['certificateArn']

        cfntmp.format(
            accountId=self._accountId,
            region=self._region,
            thingName=thingName,
            certificateArn=certificateArn
        )


    def generate_key_certs(self, thingName):

        response = self._iot.create_keys_and_certificate(
            setAsActive=True
        )

        if not os.path.isdir(self._exportPath):
            os.mkdir(self._exportPath)

        pemFilePath = os.path.join(self._exportPath, '{}.pem'.format(thingName))
        crtFilePath = os.path.join(self._exportPath, '{}.crt'.format(thingName))
        keyFilePath = os.path.join(self._exportPath, '{}.key'.format(thingName))

        with open(pemFilePath, 'w') as f:
            f.write(response['certificatePem'])

        with open(crtFilePath, 'w') as f:
            f.write(response['keyPair']['PrivateKey'])

        with open(keyFilePath, 'w') as f:
            f.write(response['keyPair']['PublicKey'])

        return response['certificateArn']
