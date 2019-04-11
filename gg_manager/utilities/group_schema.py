import json

from schema import Schema, And, Use, Optional, Regex


groupSchema = Schema(And(Use(json.load), {
    'Group': {
        'Name': Regex('[a-zA-Z][-a-zA-Z0-9]*')
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
