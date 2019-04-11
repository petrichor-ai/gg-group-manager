import json

from schema import Schema, And, Use, Optional


groupSchema = Schema(And(Use(json.load), {
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
    'Functions': [
        {
            "FunctionName": basestring,
            "Handler":      basestring,
            "Runtime":      basestring,
            "Package":      basestring,
            "Alias":        basestring,
            "Configuration": {
				"EncodingType": basestring,
                "Executable": basestring,
                "MemorySize": int,
                "Pinned": bool,
                "Timeout": int
			}
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
