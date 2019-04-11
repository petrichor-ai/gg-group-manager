import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('FunctionDefinition')
log.setLevel(logging.DEBUG)



class FunctionDefinition(object):


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Function Definition.
        '''
        functions = []

        for function in config['Functions']:
            functionName       = device['functionName']

            functions.append({
                "Id": functionName,
                "FunctionArn": functionArn,
                "FunctionConfiguration": functionConfiguration
            })

        cfntmp.format(functions=json.dumps(functions))


    def fetchFunctionArn(self, functionName):
        response = client.get_function(
            FunctionName=functionName
        )
