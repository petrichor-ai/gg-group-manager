import fire

from gg_manager.coresCommands import CoresCommands
from gg_manager.funcsCommands import FuncsCommands
from gg_manager.groupCommands import GroupCommands
from gg_manager.thingCommands import ThingCommands


def main():
    ''' Command-line cli entrypoint.
    '''
    fire.Fire({
        'cores': CoresCommands,
        'funcs': FuncsCommands,
        'group': GroupCommands,
        'thing': ThingCommands
    })
