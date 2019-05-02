import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('LambdaDefinition')
log.setLevel(logging.DEBUG)



class LambdaDefinition(object):


    def __init__(self, s):

        self._cfn = s.client('cloudformation')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation SAM Lambda Definition.
        '''
        name    = config['Id']
        codeUri = config['CodeUri']
        handler = config['Handler']
        runtime = config['Runtime']
        alias   = config['Alias']

        cfntmp.format(
            name=name,
            codeUri=codeUri,
            handler=handler,
            runtime=runtime,
            alias=alias
        )
