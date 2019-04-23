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


class CreateTopicRequest(JDCloudRequest):
    """
    创建一个指定名称的topic
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateTopicRequest, self).__init__(
            '/regions/{regionId}/topics', 'POST', header, version)
        self.parameters = parameters


class CreateTopicParameters(object):

    def __init__(self, regionId, topicName, type, ):
        """
        :param regionId: 所在区域的Region ID
        :param topicName: topic名称
        :param type: 类型，[normal,global_order]
        """

        self.regionId = regionId
        self.topicName = topicName
        self.type = type
        self.description = None

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，长度不大于255
        """
        self.description = description
