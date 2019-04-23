import json
import schema


class Schema(object):

    def __init__(self, func, use):
        self.func = func(use)



def groupSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'Group': {
            'Name': basestring
        },
        'Cores': [
            {
                'thingName': basestring,
                'SyncShadow': bool
            }
        ],
        'Devices': [
            {
                'thingName': basestring,
                'SyncShadow': bool
            }
        ],
        schema.Optional('Functions'): [
            {
                "FunctionName": basestring,
                "FunctionAlias": basestring,
                "EncodingType": basestring,
                "Executable": basestring,
                "MemorySize": int,
                "Pinned": bool,
                "Timeout": int,
                "Environment": dict
            }
        ],
        schema.Optional('Resources'): [
            {
                "Id": basestring,
                "Name": basestring,
                "ResourceDataContainer": {
                    "LocalDeviceResourceData": {
                        "GroupOwnerSetting": {
                            "AutoAddGroupOwner": bool
                        },
                        "SourcePath": basestring
                    }
                }
            }
        ]
    }))


def thingSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'Devices': [
            {
                'thingName': basestring,
                'Attributes': dict
            }
        ]
    }))

