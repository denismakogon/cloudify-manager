#########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.


class Config(object):

    def __init__(self):
        self._db_address = 'localhost'
        self._db_port = 9200
        self._amqp_address = 'localhost'
        self._file_server_root = None
        self._file_server_base_uri = None
        self._file_server_blueprints_folder = None
        self._file_server_uploaded_blueprints_folder = None
        self._file_server_resources_uri = None
        self._rest_service_log_path = None
        self._test_mode = False
        self._securest_secret_key = None
        self._securest_authentication_methods = []
        self._securest_userstore_driver = None
        self._securest_userstore_identifier_attribute = None

    @property
    def db_address(self):
        return self._db_address

    @db_address.setter
    def db_address(self, value):
        self._db_address = value

    @property
    def db_port(self):
        return self._db_port

    @db_port.setter
    def db_port(self, value):
        self._db_port = value

    @property
    def amqp_address(self):
        return self._amqp_address

    @amqp_address.setter
    def amqp_address(self, value):
        self._amqp_address = value

    @property
    def file_server_root(self):
        return self._file_server_root

    @file_server_root.setter
    def file_server_root(self, value):
        self._file_server_root = value

    @property
    def file_server_base_uri(self):
        return self._file_server_base_uri

    @file_server_base_uri.setter
    def file_server_base_uri(self, value):
        self._file_server_base_uri = value

    @property
    def file_server_blueprints_folder(self):
        return self._file_server_blueprints_folder

    @file_server_blueprints_folder.setter
    def file_server_blueprints_folder(self, value):
        self._file_server_blueprints_folder = value

    @property
    def file_server_uploaded_blueprints_folder(self):
        return self._file_server_uploaded_blueprints_folder

    @file_server_uploaded_blueprints_folder.setter
    def file_server_uploaded_blueprints_folder(self, value):
        self._file_server_uploaded_blueprints_folder = value

    @property
    def file_server_resources_uri(self):
        return self._file_server_resources_uri

    @file_server_resources_uri.setter
    def file_server_resources_uri(self, value):
        self._file_server_resources_uri = value

    @property
    def rest_service_log_path(self):
        return self._rest_service_log_path

    @rest_service_log_path.setter
    def rest_service_log_path(self, value):
        self._rest_service_log_path = value

    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, value):
        self._test_mode = value

    @property
    def securest_secret_key(self):
        return self._securest_secret_key

    @securest_secret_key.setter
    def securest_secret_key(self, value):
        self._securest_secret_key = value

    @property
    def securest_authentication_methods(self):
        return self._securest_authentication_methods

    @securest_authentication_methods.setter
    def securest_authentication_methods(self, value):
        self._securest_authentication_methods = value

    @property
    def securest_userstore_driver(self):
        return self._securest_userstore_driver

    @securest_userstore_driver.setter
    def securest_userstore_driver(self, value):
        self._securest_userstore_driver = value

    @property
    def securest_userstore_identifier_attribute(self):
        return self._securest_userstore_identifier_attribute

    @securest_userstore_identifier_attribute.setter
    def securest_userstore_identifier_attribute(self, value):
        self._securest_userstore_identifier_attribute = value

_instance = Config()


def reset(configuration=None):
    global _instance
    if configuration is not None:
        _instance = configuration
    else:
        _instance = Config()


def instance():
    return _instance
