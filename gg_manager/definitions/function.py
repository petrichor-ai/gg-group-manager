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

        for function in config.get('Functions', []):
            functionName     = function['Id']
            functionAlias    = function['Alias']
            functionConfig   = function['Configuration']
            functionAliasArn = self.fetchFunctionArn(
                functionName, functionAlias
            )

            functions.append({
                "Id": functionName,
                "FunctionArn": functionAliasArn,
                "FunctionConfiguration": functionConfig
            })

        cfntmp.format(functions=json.dumps(functions))


    def fetchFunctionArn(self, functionName, functionAlias):
        response = self._lambda.get_alias(
            FunctionName=functionName,
            Name=functionAlias
        )
        return response['AliasArn']
