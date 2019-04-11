import string
import json


class GroupCfnTmp(object):

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



CFN_TEMPLATE_BODY = \
'''
{
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
    }
}
'''

