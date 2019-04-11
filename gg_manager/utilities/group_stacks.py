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
        self._gg  = s.client('greengrass')


    def create(self, config, cfntmp):
        ''' Create a Cloudformation Greengrass Group Stack.
        '''
        groupName = config['Group']['Name']

        response = self._cfn.create_stack(
            StackName='{}-GG-Stack'.format(groupName),
            TemplateBody=cfntmp.json_dump(),
            Capabilities=['CAPABILITY_IAM']
        )


    def update(self, config, cfntmp):
        ''' Update a Cloudformation Greengrass Group Stack.
        '''
        groupName = config['Group']['Name']

        response = self._cfn.update_stack(
            StackName='{}-GG-Stack'.format(groupName),
            TemplateBody=cfntmp.json_dump(),
            Capabilities=['CAPABILITY_IAM']
        )


    def delete(self, config, cfntmp):
        ''' Delete a Cloudformation Greengrass Group Stack.
        '''
        groupName = config['Group']['Name']

        response = self._cfn.delete_stack(
            StackName='{}-GG-Stack'.format(groupName)
        )


    def output(self, config):
        ''' Retreive a Cloudformation Greengrass Group Stack Output.
        '''
        groupName = config['Group']['Name']

        response = self._cfn.describe_stacks(
            StackName='{}-GG-Stack'.format(groupName)
        )
        outputs = response['Stacks'][0]['Outputs']
        outputs = {out['OutputKey']: out['OutputValue'] for out in outputs}

        response = self._gg.get_group(
            GroupId=outputs['groupId']
        )
        return response
