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


class BaseRuleT(object):

    def __init__(self, calculation, metricId, noticePeriod, operation, period, ruleType, threshold, times, autoScalingPolicyId=None, calculateUnit=None, downSample=None, noticeLevel=None, tags=None):
        """
        :param autoScalingPolicyId: (Optional) 弹性伸缩组ID
        :param calculateUnit: (Optional) 监控项单位
        :param calculation:  统计方法，必须与定义的metric一致，可选值列表：avg,sum,max,min
        :param downSample: (Optional) 降采样函数
        :param metricId:  监控项ID
        :param noticeLevel: (Optional) 
        :param noticePeriod:  通知周期，单位：小时
        :param operation:  报警比较符，只能为以下几种lte(<=),lt(<),gt(>),gte(>=),eq(==),ne(!=)
        :param period:  查询指标的周期，单位为分钟,目前支持的取值：1, 2，5，15，30，60
        :param ruleType:  规则类型, 1表示云监控，2表示弹性伸缩，3表示AG，4表示AutoHeal，5表示自定义监控，6表示hawkeye
        :param tags: (Optional) 多值标签
        :param threshold:  报警阈值，目前只开放数值类型功能
        :param times:  连续探测几次都满足阈值条件时报警，可选值:1,2,3,5,10,15,30,60
        """

        self.autoScalingPolicyId = autoScalingPolicyId
        self.calculateUnit = calculateUnit
        self.calculation = calculation
        self.downSample = downSample
        self.metricId = metricId
        self.noticeLevel = noticeLevel
        self.noticePeriod = noticePeriod
        self.operation = operation
        self.period = period
        self.ruleType = ruleType
        self.tags = tags
        self.threshold = threshold
        self.times = times
