import boto3
import json
import logging
import os

from botocore.exceptions import ClientError

from gg_manager.utilities.gg_ansible import Playbook
from gg_manager.utilities.gg_config  import Config
from gg_manager.utilities.gg_schema  import Schema, coresSchema


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('CoresCommands')
log.setLevel(logging.DEBUG)



class CoresCommands(object):

    def __init__(self):
        super(CoresCommands, self).__init__()

        s = boto3.session.Session()
        if not s.region_name:
            raise Exception("AWS Credentials and Region must be setup")

        self._config  = Config()
        self._playbk  = Playbook()


    def initialize(self, configJson='', configFile=''):
        ''' Configure Device with AWS Greengrass Software.
        '''
        if configJson:
            schema = Schema(coresSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(coresSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        playbook = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'playbooks',
            'cores_init.yml')

        self._playbk.execute(
            remote_user=self._config['remote_user'],
            sources=self._config['hosts'],
            playbook=playbook,
            extra_vars=self._config.get('extra_vars', {})
        )


    def configure(self, configJson='', configFile=''):
        ''' Configure Device with AWS Greengrass Artifacts.
        '''
        if configJson:
            schema = Schema(coresSchema, use=json.loads)
            self._config.load_from_json(configJson, schema)
        else:
            schema = Schema(coresSchema, use=json.load)
            self._config.load_from_file(configFile, schema)

        playbook = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'playbooks',
            'cores_conf.yml')

        self._playbk.execute(
            remote_user=self._config['remote_user'],
            sources=self._config['sources'],
            playbook=playbook,
            extra_vars=self._config.get('extra_vars', {})
        )
