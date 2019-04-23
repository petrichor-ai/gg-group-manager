import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupDefinition')
log.setLevel(logging.DEBUG)



class GroupDefinition(object):


    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Group Definition.
        '''
        groupName = config['Group']['Name']
        cfntmp.format(groupName=groupName)


    def deployDefinition(self, groupId, groupVersionId):
        self._gg.create_deployment(
            GroupId=groupId,
            GroupVersionId=groupVersionId,
            DeploymentType='NewDeployment'
        )


    def resetDefinition(self, groupId):
        self._gg.reset_deployments(
            GroupId=groupId,
            Force=True
        )


    def fetchGroup(self, groupId):

        response = self._gg.get_group(
            GroupId=groupId
        )
        return response
