import os
import json
import logging


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupState')
log.setLevel(logging.DEBUG)



class GroupState(object):

    def __init__(self, fileName='state.json', localPath='.gg', S3Bucket='', S3Key=''):

        self._fileName  = fileName
        self._localPath = localDest
        self._S3Bucket  = S3Bucket
        self._S3Key     = S3Key

        if not os.path.exists(self._localPath):
            os.mkdir(self._localPath)

        self.data = {}


    def load(self):

        statePath = os.path.join(self._localPath, self._fileName)
        if not os.path.exists(statePath):
            log.warn('State file not found. Assume new group')
            self.data = {}
        else:
            with open(statePath, 'r') as f:
                self.data = json.load(f)
            log.info('State file loaded')


    def save(self):

        statePath = os.path.join(self._localPath, self._fileName)
        with open(statePath, 'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)
        log.info('State file saved')


    def push(self):
        pass


    def scrub(self, state_obj={}):

        for k, v in state_obj.iteritems():
            if type(v) == dict:
                state_obj[k] = state_scrub(v)
            else:
                if type(v) == list:
                    state_obj[k] = []
                else:
                    state_obj[k] = ''
        return state_obj

