import json

from schema import Schema, And, Use, Optional, Regex


groupSchema = Schema(And(Use(json.load), {
    'Group': {
        'Name': basestring
    },
    'Cores': [
        {
            'thingName': basestring,
            'SyncShadow': bool,
            'useExistingThing': bool
        }
    ],
    'Devices': [
        {
            'thingName': basestring,
            'SyncShadow': bool,
            'useExistingThing': bool
        }
    ],
    'Functions': [
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
    'Resources': [
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
