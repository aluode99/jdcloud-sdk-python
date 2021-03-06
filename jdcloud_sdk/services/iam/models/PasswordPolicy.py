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


class PasswordPolicy(object):

    def __init__(self, length, age, expirationOperation, reusePrevention, retryTimes, validLoginDuration, rule, ):
        """
        :param length:  密码长度，6-20之间
        :param age:  密码有效期，0-1095之间
        :param expirationOperation:  过期重置类型：0-主账号重置，1-子账号重置
        :param reusePrevention:  历史密码检查次数,0-10之间
        :param retryTimes:  密码重试次数,1-16之间
        :param validLoginDuration:  
        :param rule:  密码字符类型，至少包含一种
        """

        self.length = length
        self.age = age
        self.expirationOperation = expirationOperation
        self.reusePrevention = reusePrevention
        self.retryTimes = retryTimes
        self.validLoginDuration = validLoginDuration
        self.rule = rule
