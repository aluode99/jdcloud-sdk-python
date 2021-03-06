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


class Software(object):

    def __init__(self, name=None, version=None, osTypeId=None, description=None):
        """
        :param name: (Optional) 软件包名称
        :param version: (Optional) 软件包版本
        :param osTypeId: (Optional) 操作系统系统类型ID
        :param description: (Optional) 软件包描述
        """

        self.name = name
        self.version = version
        self.osTypeId = osTypeId
        self.description = description
