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


class GetWorkFlowListRequest(JDCloudRequest):
    """
    获取工作流列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetWorkFlowListRequest, self).__init__(
            '/regions/{regionId}/{workflowName}:list', 'POST', header, version)
        self.parameters = parameters


class GetWorkFlowListParameters(object):

    def __init__(self, regionId, workflowName, ):
        """
        :param regionId: 地域ID
        :param workflowName: 工作流名称
        """

        self.regionId = regionId
        self.workflowName = workflowName
        self.selectParams = None

    def setSelectParams(self, selectParams):
        """
        :param selectParams: (Optional) 
        """
        self.selectParams = selectParams

