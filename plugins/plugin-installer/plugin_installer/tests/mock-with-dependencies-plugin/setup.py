# **************************************************************************
# * Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *       http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
# **************************************************************************/

from setuptools import setup

setup(
    name='mock-with-dependencies-plugin',
    version='3.2rc',
    author='elip',
    author_email='elip@gigaspaces.com',
    packages=['mock_with_dependencies_for_test'],
    license='LICENSE',
    description='Mock plugin for test',
    install_requires=[
        # Just some dependency.
        # we assert for this name in the tests code.
        'simplejson'
    ]
)
