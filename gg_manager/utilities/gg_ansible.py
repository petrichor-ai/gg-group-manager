#!/usr/bin/env python

import json
import shutil

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase

import ansible.constants as C


# since API is constructed for CLI it expects certain options to always be set,
# named tuple 'fakes' the args parsing options object

Options = namedtuple(
    'Options',
    [
        'connection',
        'module_path',
        'forks',
        'remote_user',
        'become',
        'become_method',
        'become_user',
        'verbosity',
        'check',
        'diff',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax'
    ]
)



class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """
    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))



class Playbook(object):

    def __init__(self):

        # initialize needed objects
        self.loader    = DataLoader()
        self.options   = Options(
            connection='ssh',
            module_path=None,
            forks=10,
            remote_user=None,
            become=None,
            become_method='su',
            become_user='root',
            verbosity=None,
            check=False,
            diff=False,
            listhosts=False,
            listtasks=False,
            listtags=False,
            syntax=False
        )
        self.passwords = dict(vault_pass='secret')


    def execute(self, remote_user, sources, playbook, extra_vars={}):
        options = self.options._replace(
            remote_user=remote_user
        )
        inventory = InventoryManager(
            loader=self.loader,
            sources=sources
        )
        variable_manager = VariableManager(
            loader=self.loader,
            inventory=inventory
        )
        variable_manager.extra_vars = extra_vars

        executor = PlaybookExecutor(
            playbooks=[playbook],
            inventory=inventory,
            variable_manager=variable_manager,
            loader=self.loader,
            options=options,
            passwords=self.passwords
        )

        executor.run()
