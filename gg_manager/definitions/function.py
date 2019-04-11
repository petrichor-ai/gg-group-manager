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

        self._gg     = s.client('greengrass')
        self._iot    = s.client('iot')
        self._lambda = s.client('lambda')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Function Definition.
        '''
        functions = []

        for function in config['Functions']:
            functionName  = function['FunctionName']
            functionAlias = function['FunctionAlias']
            functionArn   = self.fetchFunctionArn(functionName, functionAlias)
            functionConfiguration = \
            {
                "MemorySize":   function['MemorySize'],
                "Pinned":       function['Pinned'],
                "Timeout":      function['Timeout'],
                "EncodingType": function['EncodingType'],
                "Executable":   function['Executable'],
                "Environment":  function['Environment']
            }

            functions.append({
                "Id": functionName,
                "FunctionArn": functionArn,
                "FunctionConfiguration": functionConfiguration
            })

        cfntmp.format(functions=json.dumps(functions))


    def fetchFunctionArn(self, functionName, functionAlias):
        response = self._lambda.get_alias(
            FunctionName=functionName,
            Name=functionAlias
        )
        return response['AliasArn']
