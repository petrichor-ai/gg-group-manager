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
        schema.Optional('Functions'): list,
        schema.Optional('Resources'): [
            {
                "Id": str,
                "Name": str,
                "Container": dict
            }
        ],
        schema.Optional('Loggers'): [
            {
                "Component": str,
                "Id": str,
                "Level": str,
                schema.Optional("Space"): int,
                "Type": str
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


def funcsSchema(use=json.load):
    return schema.Schema(schema.And(schema.Use(use), {
        'Functions': [
            {
                'Id': str,
                'Version': str,
                'PackageDir': str,
                'BucketName': str,
                'BucketKey': str,
                'Handler': str,
                'Runtime': str,
                'Alias': str
            }
        ]
    }))
