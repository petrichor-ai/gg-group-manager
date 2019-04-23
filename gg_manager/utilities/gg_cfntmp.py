import string
import json


class CFNTemplate(object):

    def __init__(self, template):
        self.template = string.Template(template)
        self.partial_substituted_str = None


    def __repr__(self):
        return self.template.safe_substitute()


    def format(self, *args, **kws):
        self.partial_substituted_str = self.template.safe_substitute(*args, **kws)
        self.template = string.Template(self.partial_substituted_str)
        return self.__repr__()


    def json_dump(self):
        output = self.template.template
        output = output.replace(' ', '').replace('\n', '').replace('\t', '').replace('\\', '')
        output = json.loads(output)
        return json.dumps(output)



CFN_GROUP_TEMPLATE_BODY = \
'''
{
    \"AWSTemplateFormatVersion\": \"2010-09-09\",
    \"Description\": \"AWS IoT Greengrass Group Stack\",
    \"Resources\": {
        \"CoreDefinition\": {
            \"Type\": \"AWS::Greengrass::CoreDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-CoreDefinition\"
            }
        },
        \"CoreDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::CoreDefinitionVersion\",
            \"Properties\": {
                \"CoreDefinitionId\": {
                    \"Ref\": \"CoreDefinition\"
                },
                \"Cores\": ${cores}
            }
        },
        \"DeviceDefinition\": {
            \"Type": \"AWS::Greengrass::DeviceDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-DeviceDefinition\"
            }
        },
        \"DeviceDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::DeviceDefinitionVersion\",
            \"Properties\": {
                \"DeviceDefinitionId\": {
                    \"Ref\": \"DeviceDefinition\"
                },
                \"Devices\": ${devices}
            }
        },
        \"FunctionDefinition\": {
            \"Type\": \"AWS::Greengrass::FunctionDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-FunctionDefinition\"
            }
        },
        \"FunctionDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::FunctionDefinitionVersion\",
            \"Properties\": {
                \"FunctionDefinitionId\": {
                    \"Ref\": \"FunctionDefinition\"
                },
                \"DefaultConfig\": {
                    \"Execution\": {
                        \"IsolationMode\": \"GreengrassContainer\"
                    }
                },
                \"Functions\": ${functions}
            }
        },
        \"LoggerDefinition\": {
            \"Type\": \"AWS::Greengrass::LoggerDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-LoggerDefinition\"
            }
        },
        \"LoggerDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::LoggerDefinitionVersion\",
            \"Properties\": {
                \"LoggerDefinitionId\": {
                    \"Ref\": \"LoggerDefinition\"
                },
                \"Loggers\": ${loggers}
            }
        },
        \"ResourceDefinition\": {
            \"Type\": \"AWS::Greengrass::ResourceDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-ResourceDefinition\"
            }
        },
        \"ResourceDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::ResourceDefinitionVersion\",
            \"Properties\": {
                \"ResourceDefinitionId\": {
                    \"Ref\": \"ResourceDefinition\"
                },
                \"Resources\": ${resources}
            }
        },
        \"SubscriptionDefinition\": {
            \"Type\": \"AWS::Greengrass::SubscriptionDefinition\",
            \"Properties\": {
                \"Name\": \"${groupName}-SubscriptionDefinition\"
            }
        },
        \"SubscriptionDefinitionVersion\": {
            \"Type\": \"AWS::Greengrass::SubscriptionDefinitionVersion\",
            \"Properties\": {
                \"SubscriptionDefinitionId\": {
                    \"Ref\": \"SubscriptionDefinition\"
                },
                \"Subscriptions\": ${subscriptions}
            }
        },
        \"Role\": {
            \"Type\": \"AWS::IAM::Role\",
            \"Properties\": {
                \"AssumeRolePolicyDocument\": {
                    \"Version\": \"2012-10-17\",
                    \"Statement\": [{
                        \"Effect\": \"Allow\",
                        \"Principal\": {
                            \"Service\": [
                                \"greengrass.amazonaws.com\"
                            ]
                        },
                        \"Action\": [
                            \"sts:AssumeRole\"
                        ]
                    }]
                },
                \"Path\": \"/\",
                \"Policies\": [{
                    \"PolicyName\": \"${groupName}-Policy\",
                    \"PolicyDocument\": {
                        \"Version\" : \"2012-10-17\",
                        \"Statement\": [{
                            \"Effect\": \"Allow\",
                            \"Action\": \"*\",
                            \"Resource\": \"*\"
                        }]
                    }
                }]
            }
        },
        \"Group\": {
            \"Type\": \"AWS::Greengrass::Group\",
            \"Properties\": {
                \"Name\": \"${groupName}\",
                \"RoleArn\": {
                    \"Fn::GetAtt\" : [\"Role\", \"Arn\"]
                },
                \"InitialVersion\": {
                    \"CoreDefinitionVersionArn\": {
                        \"Ref\": \"CoreDefinitionVersion\"
                    },
                    \"DeviceDefinitionVersionArn\": {
                        \"Ref\": \"DeviceDefinitionVersion\"
                    },
                    \"FunctionDefinitionVersionArn\": {
                        \"Ref\": \"FunctionDefinitionVersion\"
                    },
                    \"SubscriptionDefinitionVersionArn\": {
                        \"Ref\": \"SubscriptionDefinitionVersion\"
                    },
                    \"LoggerDefinitionVersionArn\": {
                        \"Ref\": \"LoggerDefinitionVersion\"
                    },
                    \"ResourceDefinitionVersionArn\": {
                        \"Ref\": \"ResourceDefinitionVersion\"
                    }
                }
            }
        }
    },
    \"Outputs\": {
        \"groupName\": {
            \"Description\": \"Name of Greengrass Group\",
            \"Value\": {
                \"Fn::GetAtt\": [\"Group\", \"Name\"]
            },
            \"Export\": {
                \"Name\": \"groupName\"
            }
        },
        \"groupId\": {
            \"Description\": \"Id of Greengrass Group\",
            \"Value\": {
                \"Fn::GetAtt\": [\"Group\", \"Id\"]
            },
            \"Export\": {
                \"Name\": \"groupId\"
            }
        },
        \"groupArn\": {
            \"Description\": \"Arn of Greengrass Group\",
            \"Value\": {
                \"Fn::GetAtt\": [\"Group\", \"Arn\"]
            },
            \"Export\": {
                \"Name\": \"groupArn\"
            }
        },
        \"groupLatestVersionArn\": {
            \"Description\": \"LatestVersionArn of Greengrass Group\",
            \"Value\": {
                \"Fn::GetAtt\": [\"Group\", \"LatestVersionArn\"]
            },
            \"Export\": {
                \"Name\": \"groupLatestVersionArn\"
            }
        }
    }
}
'''


CFN_THING_TEMPLATE_BODY = \
'''
{
    \"AWSTemplateFormatVersion\": \"2010-09-09\",
    \"Resources\": {
        \"deviceThing\": {
            \"Type\": \"AWS::IoT::Thing\",
            \"Properties\": {
                \"ThingName\": \"${thingName}\",
                \"AttributePayload\": {
                    \"Attributes\": {
                        \"myAttributeA\": {
                            \"Ref\": \"MyAttributeValueA\"
                        }
                    }
                }
            }
        },
        \"devicePolicy\": {
            \"Type\": \"AWS::IoT::Policy\",
            \"Properties\": {
                \"PolicyDocument\": \"{
                    \\\"Version\\\":\\\"2012-10-17\\\",
                    \\\"Statement\\\": [
                        {
                            \\\"Effect\\\": \\\"Allow\\\",
                            \\\"Action\\\": [
                                \\\"iot:Connect\\\"
                            ],
                            \\\"Resource\\\": [
                                \\\"arn:aws:iot:${region}:${accountId}:client/${thingName}\\\"
                            ],
                            \\\"Condition\\": {
                                \\\"Bool\\\": {
                                    \\\"iot:Connection.Thing.IsAttached\\\": [
                                        \\\"true\\\"
                                    ]
                                }
                            }
                        },
                        {
                            \\\"Effect\\\": \\\"Allow\\\",
                            \\\"Action\\\": [
                                \\\"iot:GetThingShadow\\\",
                                \\\"iot:UpdateThingShadow\\\",
                                \\\"iot:DeleteThingShadow\\\"
                            ],
                            \\\"Resource\\\": [
                                \\\"arn:aws:iot:${region}:${accountId}:thing/${thingName}\\\"
                            ]
                        },
                        {
                            \\\"Effect\\\": \\\"Allow\\\",
                            \\\"Action\\\": [
                                \\\"iot:Publish\\\",
                                \\\"iot:Subscribe\\\",
                                \\\"iot:Receive\\\"
                            ],
                            \\\"Resource\\\": [
                                \\\"arn:aws:iot:${region}:${accountId}:topic/$aws/things/${thingName}/shadow/#\\\",
                                \\\"arn:aws:iot:${region}:${accountId}:topicfilter/$aws/things/${thingName}/shadow/#\\\"
                            ]
                        },
                        {
                            \\\"Effect\\\": \\\"Allow\\\",
                            \\\"Action\\\": [
                                \\\"greengrass:*\\\"
                            ],
                            \\\"Resource\\\": [
                                \\\"*\\\"
                            ]
                        }
                    ]
                }\"
            }
        },
        \"devicePolicyPrincipal\": {
            \"Type\": \"AWS::IoT::PolicyPrincipalAttachment\",
            \"Properties\": {
                \"PolicyName\": {
                    \"Ref\": \"devicePolicyPrincipal\"
                },
                \"Principal\": \"${certificateArn}\"
            }
        },
        \"deviceThingPrincipal\": {
            \"Type\": \"AWS::IoT::ThingPrincipalAttachment\",
            \"Properties\": {
                \"ThingName\": {
                    \"Ref\": \"deviceThing\"
                },
                \"Principal\": \"${certificateArn}\"
            }
        }
    }
}
'''
