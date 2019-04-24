from distutils.core import setup

setup(
    name='gg_group_manager',
    version='1.0.0',
    description='AWS Greengrass Group Manager',
    packages=[
        'gg_manager',
        'gg_manager.definitions',
        'gg_manager.playbooks',
        'gg_manager.utilities'
    ],
    install_requires=[
        'fire==0.1.3',
        'boto3==1.9.98',
        'botocore==1.12.98',
        'schema==0.7.0',
        'ansible==2.7.10'
    ],
    entry_points={
        'console_scripts': [
            'gg-manager=gg_manager:main'
        ],
    },
    include_package_data=True
)
