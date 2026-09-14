import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 1. Pendaftaran Launch File agar terbaca oleh ROS 2
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AchmadJRafi',
    maintainer_email='achmadjamaluddinrafi@mail.ugm.ac.id',
    description='Modul 2 ROS 2 Communication Architecture',
    license='TODO: License declaration',
    tests_require=['pytest'],
    # 2. Pendaftaran Node / Executable ROS 2
    entry_points={
        'console_scripts': [
            'sensor_publisher = lab_comm.sensor_publisher:main',
            'processing_node = lab_comm.processing_node:main',
            'reset_service = lab_comm.reset_service:main',
            'motion_action_server = lab_comm.motion_action_server:main',
        ],
    },
)
