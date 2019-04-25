import json
import schema


class Schema(object):

    def __init__(self, func, use):
        self.func = func(use)



def groupSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'Group': {
            'Name': str
        },
        'Cores': [
            {
                'thingName': str,
                'SyncShadow': bool
            }
        ],
        'Devices': [
            {
                'thingName': str,
                'SyncShadow': bool
            }
        ],
        schema.Optional('Functions'): [
            {
                "FunctionName": str,
                "FunctionAlias": str,
                "EncodingType": str,
                "Executable": str,
                "MemorySize": int,
                "Pinned": bool,
                "Timeout": int,
                "Environment": dict
            }
        ],
        schema.Optional('Resources'): [
            {
                "Id": str,
                "Name": str,
                "ResourceDataContainer": {
                    "LocalDeviceResourceData": {
                        "GroupOwnerSetting": {
                            "AutoAddGroupOwner": bool
                        },
                        "SourcePath": str
                    }
                }
            }
        ]
    }))


def thingSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'Devices': [
            {
                'thingName': str,
                'Attributes': dict
            }
        ]
    }))


def coresSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'remote_user': str,
        'hosts': str,
        schema.Optional('extra_vars'): dict
    }))

