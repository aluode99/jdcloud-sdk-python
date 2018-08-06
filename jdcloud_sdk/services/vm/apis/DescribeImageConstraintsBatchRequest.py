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


class DescribeImageConstraintsBatchRequest(JDCloudRequest):
    """
    批量查询镜像的规格类型限制。<br>
通过此接口可以查看镜像不支持的规格类型。只有官方镜像、第三方镜像有规格类型的限制，个人的私有镜像没有此限制。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeImageConstraintsBatchRequest, self).__init__(
            '/regions/{regionId}/imageConstraints', 'GET', header, version)
        self.parameters = parameters


class DescribeImageConstraintsBatchParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.ids = None

    def setIds(self, ids):
        """
        :param ids: (Optional) 镜像ID列表
        """
        self.ids = ids
