########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
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

__author__ = 'idanmo'

from cloudify.decorators import operation


NON_EXISTING_OPERATIONS = ['testmockoperations.non_existent']

INSTALLED_PLUGINS = []


@operation
def install(ctx, plugin, **kwargs):
    print '###########', plugin, '#####################'
    global INSTALLED_PLUGINS
    ctx.logger.info("in plugin_installer.install --> "
                    "installing plugin {0}".format(plugin))
    INSTALLED_PLUGINS.append(plugin['name'])


@operation
def get_installed_plugins(**kwargs):
    return INSTALLED_PLUGINS