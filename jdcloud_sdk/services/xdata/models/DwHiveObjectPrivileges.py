# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class DwHiveObjectPrivileges(object):

    def __init__(self, status=None, message=None, select=None, insert=None, update=None, delete=None, drop=None, create=None, alter=None, owner=None):
        """
        :param status: (Optional) 状态
        :param message: (Optional) 返回信息
        :param select: (Optional) select权限
        :param insert: (Optional) insert权限
        :param update: (Optional) update权限
        :param delete: (Optional) delete权限
        :param drop: (Optional) drop权限
        :param create: (Optional) create权限
        :param alter: (Optional) alter权限
        :param owner: (Optional) 是否为此表所有者
        """

        self.status = status
        self.message = message
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete
        self.drop = drop
        self.create = create
        self.alter = alter
        self.owner = owner
