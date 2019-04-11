import boto3
import json
import logging

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('SubscriptionDefinition')
log.setLevel(logging.DEBUG)



class SubscriptionDefinition(object):

    SHADOW_TOPICS = [
        {
            "Id": "{thingName}_shadow_update",
            "Source": "{thingArn}",
            "Subject": "$aws/things/{thingName}/shadow/update",
            "Target": "GGShadowService"
        },
        {
            "Id": "{thingName}_shadow_update_accepted",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/update/accepted",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_update_delta",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/update/delta",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_update_rejected",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/update/rejected",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_get",
            "Source": "{thingArn}",
            "Subject": "$aws/things/{thingName}/shadow/get",
            "Target": "GGShadowService"
        },
        {
            "Id": "{thingName}_shadow_get_accepted",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/get/accepted",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_get_rejected",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/get/rejected",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_delete",
            "Source": "{thingArn}",
            "Subject": "$aws/things/{thingName}/shadow/delete",
            "Target": "GGShadowService"
        },
        {
            "Id": "{thingName}_shadow_delete_accepted",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/delete/accepted",
            "Target": "{thingArn}"
        },
        {
            "Id": "{thingName}_shadow_delete_rejected",
            "Source": "GGShadowService",
            "Subject": "$aws/things/{thingName}/shadow/delete/rejected",
            "Target": "{thingArn}"
        }
    ]

    def __init__(self, s):

        self._gg  = s.client('greengrass')
        self._iot = s.client('iot')


    def formatDefinition(self, config, cfntmp):
        ''' Format a Cloudformation Greengrass Group Subscription Definition.
        '''
        subscriptions = []

        for device in config['Devices']:
            thingName = device['thingName']
            thingArn  = self.fetchThingArn(thingName)

            for shadow_topic in self.SHADOW_TOPICS:
                sub = {}
                sub["Id"]      = shadow_topic["Id"].format(thingName=thingName)
                sub["Subject"] = shadow_topic["Subject"].format(thingName=thingName)

                if shadow_topic["Source"] == "GGShadowService":
                    sub["Source"] = shadow_topic["Source"]
                    sub["Target"] = shadow_topic["Target"].format(thingArn=thingArn)
                else:
                    sub["Target"] = shadow_topic["Target"]
                    sub["Source"] = shadow_topic["Source"].format(thingArn=thingArn)
                subscriptions.append(sub)

        cfntmp.format(subscriptions=json.dumps(subscriptions))


    def fetchThingArn(self, thingName):
        ''' Fetch a Thing's Arn.
        '''
        response = self._iot.describe_thing(
            thingName=thingName
        )
        return response['thingArn']
