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


from testenv import TestCase
from testenv.utils import get_resource as resource
from testenv.utils import deploy_application as deploy


class TestMultiInstanceApplication(TestCase):

    def test_deploy_multi_instance_application(self):
        dsl_path = resource("dsl/multi_instance.yaml")
        deployment, _ = deploy(dsl_path)
        machines = set(self.get_plugin_data(
            plugin_name='cloudmock',
            deployment_id=deployment.id
        )['machines'])
        self.assertEquals(2, len(machines))
        apps_state = self.get_plugin_data(
            plugin_name='testmockoperations',
            deployment_id=deployment.id
        )['state']
        machines_with_apps = set([])
        for app_state in apps_state:
            host_id = app_state['capabilities'].keys()[0]
            machines_with_apps.add(host_id)
        self.assertEquals(machines, machines_with_apps)

    def test_deploy_multi_instance_many_different_hosts(self):
        dsl_path = resource('dsl/multi_instance_many_different_hosts.yaml')
        deployment, _ = deploy(dsl_path)
        machines = set(self.get_plugin_data(
            plugin_name='cloudmock',
            deployment_id=deployment.id
        )['machines'])
        self.assertEquals(15, len(machines))

        self.assertEquals(5, len(filter(lambda ma: ma.startswith('host1'),
                                        machines)))
        self.assertEquals(5, len(filter(lambda ma: ma.startswith('host2'),
                                        machines)))
        self.assertEquals(5, len(filter(lambda ma: ma.startswith('host3'),
                                        machines)))
