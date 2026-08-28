from setuptools import find_packages, setup

package_name = 'turtlesim_ctr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jack',
    maintainer_email='jp.alvial.araya@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'listener_ctrl = turtlesim_ctr.listener_ctr:main',
            'listener2_ctrl = turtlesim_ctr.listener_ctr:main',
            'pose_ctrl = turtlesim_ctr.position_ctr:main',
        ],
    },
)
