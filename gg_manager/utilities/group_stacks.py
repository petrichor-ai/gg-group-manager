import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupStack')
log.setLevel(logging.DEBUG)



class GroupStack(object):


    def __init__(self, s):

        self._cfn = s.client('cloudformation')


    def create(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Connector Definition.
        '''
        response = self._cfn.create_stack(
            StackName='TestStack',
            TemplateBody=cfntmp.json_dump(),
            Capabilities=['CAPABILITY_IAM']
        )
