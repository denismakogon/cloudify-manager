########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup


setup(
    name='cloudify-windows-plugin-installer-plugin',
    version='3.3a1',
    author='elip',
    author_email='elip@gigaspaces.com',
    packages=['windows_plugin_installer'],
    license='LICENSE',
    description='Plugin for installing plugins into an '
                'existing celery windows worker',
    zip_safe=False,
    install_requires=[
        "cloudify-plugins-common==3.3a1"
    ],
    tests_require=[
        "nose"
    ]
)
