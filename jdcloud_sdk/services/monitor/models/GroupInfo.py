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


class GroupInfo(object):

    def __init__(self, charts=None, groupCode=None, groupName=None, metrics=None, tags=None, webCode=None):
        """
        :param charts: (Optional) 监控图的展示方式
        :param groupCode: (Optional) 分组groupCode
        :param groupName: (Optional) 分组名称
        :param metrics: (Optional) 分组内的metric列表
        :param tags: (Optional) 分组下metric对应的tags
        :param webCode: (Optional) 分组的webCode
        """

        self.charts = charts
        self.groupCode = groupCode
        self.groupName = groupName
        self.metrics = metrics
        self.tags = tags
        self.webCode = webCode
