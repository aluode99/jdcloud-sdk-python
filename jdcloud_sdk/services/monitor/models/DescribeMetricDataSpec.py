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


class DescribeMetricDataSpec(object):

    def __init__(self, resourceId, serviceCode, aggrType=None, endTime=None, groupBy=None, startTime=None, tags=None, timeInterval=None):
        """
        :param aggrType: (Optional) 指标聚合方式，每个指标都有默认的聚合方式， 可选值包括：sum,avg.max.min
        :param endTime: (Optional) 查询时间范围的结束时间， UTC时间，格式：2016-12- yyyy-MM-dd'T'HH:mm:ssZ（为空时，将由startTime与timeInterval计算得出）
in: query
        :param groupBy: (Optional) 是否对查询的tags分组
in: query
        :param resourceId:  资源的uuid
        :param serviceCode:  资源的类型，取值vm, lb, ip, database 等
        :param startTime: (Optional) 查询时间范围的开始时间， UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ（默认为当前时间，早于30d时，将被重置为30d）
in: query
        :param tags: (Optional) 自定义标签
in: query
        :param timeInterval: (Optional) 时间间隔：1h，6h，12h，1d，3d，7d，14d，固定时间间隔，timeInterval 与 endTime 至少填一项
in: query
        """

        self.aggrType = aggrType
        self.endTime = endTime
        self.groupBy = groupBy
        self.resourceId = resourceId
        self.serviceCode = serviceCode
        self.startTime = startTime
        self.tags = tags
        self.timeInterval = timeInterval
