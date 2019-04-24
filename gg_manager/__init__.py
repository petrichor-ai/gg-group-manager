import fire

from gg_manager.coresCommands import CoresCommands
from gg_manager.groupCommands import GroupCommands
from gg_manager.thingCommands import ThingCommands


def main():
    fire.Fire({
        'cores': CoresCommands,
        'group': GroupCommands,
        'thing': ThingCommands
    })
