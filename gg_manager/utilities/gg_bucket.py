import boto3
import io
import logging
import os
import zipfile

from botocore.exceptions import ClientError


logging.basicConfig(
    format='%(asctime)s|%(name).10s|%(levelname).5s: %(message)s',
    level=logging.WARNING
)

log = logging.getLogger('GroupBucket')
log.setLevel(logging.DEBUG)



class Bucket(object):


    def __init__(self, s):

        self._region = s.region_name
        self._s3     = s.client('s3')


    def create(self, config, cfntmp):
        ''' Create an S3 Bucket.
        '''
        pass


    def upload(self, config):
        ''' Update an S3 Object.
        '''
        packageDir = config['PackageDir']
        bucketName = config['BucketName']
        bucketKey  = config['BucketKey']

        zip_buff = io.BytesIO()
        with zipfile.ZipFile(zip_buff, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for root, dirs, files, in os.walk(packageDir, topdown=True):
                for fn in files:
                    absfn = os.path.join(root, fn)
                    zfn   = absfn[len(packageDir)+len(os.sep):]
                    zip_file.write(filename=absfn, arcname=zfn)

        response = self._s3.put_object(
            ACL='private',
            Body=zip_buff.getvalue(),
            Bucket=bucketName,
            Key=bucketKey
        )
        return 'https://s3-{}.amazonaws.com/{}/{}'.format(
            self._region, bucketName, bucketKey
        )


    def delete(self, config):
        ''' Delete an S3 object.
        '''
        pass
