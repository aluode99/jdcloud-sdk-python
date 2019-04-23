# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateRdsDatabaseRequest(JDCloudRequest):
    """
    根据给定的信息，创建指定RDS实例的数据库
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateRdsDatabaseRequest, self).__init__(
            '/regions/{regionId}/rds_instances/{instId}/databases', 'POST', header, version)
        self.parameters = parameters


class CreateRdsDatabaseParameters(object):

    def __init__(self, regionId, instId, database):
        """
        :param regionId: 地域ID
        :param instId: RDS实例ID
        :param database: 创建RDS实例的数据库信息
        """

        self.regionId = regionId
        self.instId = instId
        self.database = database
