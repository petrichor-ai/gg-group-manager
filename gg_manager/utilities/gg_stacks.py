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
        ''' Create a Cloudformation Greengrass Resource Stack.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('thingName', None):
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('Alias', None):
            funcsName = config['Alias']
            stackName = '{}-Funcs-Stack'.format(funcsName)
            stackCaps = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']

        response = self._cfn.create_stack(
            StackName=stackName,
            TemplateBody=cfntmp.json_dump(),
            Capabilities=stackCaps
        )


    def update(self, config, cfntmp):
        ''' Update a Cloudformation Greengrass Resource Stack.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('thingName', None):
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('Alias', None):
            funcsName = config['Alias']
            stackName = '{}-Funcs-Stack'.format(funcsName)
            stackCaps = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']

        response = self._cfn.update_stack(
            StackName=stackName,
            TemplateBody=cfntmp.json_dump(),
            Capabilities=stackCaps
        )


    def delete(self, config, cfntmp):
        ''' Delete a Cloudformation Greengrass Resource Stack.
        '''

        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('thingName', None):
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('Alias', None):
            funcsName = config['Alias']
            stackName = '{}-Funcs-Stack'.format(funcsName)
            stackCaps = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']

        response = self._cfn.delete_stack(
            StackName=stackName
        )


    def output(self, config):
        ''' Retreive a Cloudformation Greengrass Resource Stack Output.
        '''
        if config.get('Group', None):
            groupName = config['Group']['Name']
            stackName = '{}-GG-Stack'.format(groupName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('thingName', None):
            thingName = config['thingName']
            stackName = '{}-Thing-Stack'.format(thingName)
            stackCaps = ['CAPABILITY_IAM']

        if config.get('Alias', None):
            funcsName = config['Alias']
            stackName = '{}-Funcs-Stack'.format(funcsName)
            stackCaps = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']

        response = self._cfn.describe_stacks(
            StackName=stackName
        )
        outputs = response['Stacks'][0].get('Outputs', [])
        return {out['OutputKey']: out['OutputValue'] for out in outputs}

