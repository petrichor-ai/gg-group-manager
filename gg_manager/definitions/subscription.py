import boto3
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('SubscriptionDefinition')
log.setLevel(logging.DEBUG)



class SubscriptionDefinition(object):


    def __init__(self, s, state):

        self._state = state

        self._gg    = s.client('greengrass')
        self._iot   = s.client('iot')


    def create(self, name, subscriptions, tags={}):
        ''' Create a Greengrass Group Subscription Definition.
        '''
        response = {}
        try:
            response = self._gg.create_subscription_definition(
                InitialVersion={
                    'Subscriptions': subscriptions
                },
                Name=name,
                tags=tags
            )
        except ClientError as e:
            log.error('Create Greengrass Subscription Definition failed', exc_info=True)
            return response
        else:
            log.info('Create Greengrass Subscription Definition successful')
            return response
        finally:
            pass


    def fetch(self, definitionId):
        ''' Fetch a Greengrass Group Subscription Definition.
        '''
        response = client.get_subscription_definition(
            SubscriptionDefinitionId=definitionId
        )
        return response


    def remove(self, definitionId):
        ''' Remove a Greengrass Group Subscription Definition.
        '''
        response = client.delete_subscription_definition(
            SubscriptionDefinitionId=definitionId
        )
        return response


    def update(self, definitionId):
        ''' Update a Greengrass Group Subscription Definition.
        '''
        response = client.update_subscription_definition(
            SubscriptionDefinitionId=definitionId
        )
        return response


