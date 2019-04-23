import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupStack')
log.setLevel(logging.DEBUG)



class Stack(object):


    def __init__(self, s):

        self._cfn = s.client('cloudformation')
        self._gg  = s.client('greengrass')


    def create(self, config, cfntmp):
        ''' Create a Cloudformation Greengrass Group Stack.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
        else:
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)

        response = self._cfn.create_stack(
            StackName=stackName,
            TemplateBody=cfntmp.json_dump(),
            Capabilities=['CAPABILITY_IAM']
        )


    def update(self, config, cfntmp):
        ''' Update a Cloudformation Greengrass Group Stack.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
        else:
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)

        response = self._cfn.update_stack(
            StackName=stackName,
            TemplateBody=cfntmp.json_dump(),
            Capabilities=['CAPABILITY_IAM']
        )


    def delete(self, config, cfntmp):
        ''' Delete a Cloudformation Greengrass Group Stack.
        '''

        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
        else:
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)

        response = self._cfn.delete_stack(
            StackName=stackName
        )


    def output(self, config):
        ''' Retreive a Cloudformation Greengrass Group Stack Output.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
        else:
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)

        response = self._cfn.describe_stacks(
            StackName=stackName
        )
        outputs = response['Stacks'][0]['Outputs']
        outputs = {out['OutputKey']: out['OutputValue'] for out in outputs}

        response = self._gg.get_group(
            GroupId=outputs['groupId']
        )
        return response
