import fire

from groupCommands import GroupCommands
from thingCommands import ThingCommands


def main():
    fire.Fire({
        'group': GroupCommands,
        'thing': ThingCommands
    })
