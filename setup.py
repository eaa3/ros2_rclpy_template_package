from setuptools import setup

package_name = 'ros2_rclpy_template_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Ermano Arruda',
    author_email='ermano.arruda@gmail.com',
    maintainer='Ermano Arruda',
    maintainer_email='ermano.arruda@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A simple template for an rclpy package',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = ros2_rclpy_template_package.simple_publisher:main',
        ],
    },
)
