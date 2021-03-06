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


class OrderPriceDetail(object):

    def __init__(self, price=None, priceScale4=None, discount=None, discountedPrice=None, originalPrice=None, resourceId=None, appCode=None, serviceCode=None, site=None, region=None, billingType=None, timeSpan=None, timeUnit=None, networkOperator=None, formula=None, favorableInfo=None, priceSnapShot=None, pin=None, taskId=None, startTime=None, endTime=None, processType=None, sourceId=None):
        """
        :param price: (Optional) 折扣前总价
        :param priceScale4: (Optional) 四位小数价格
        :param discount: (Optional) 折扣金额
        :param discountedPrice: (Optional) 折扣后订单金额
        :param originalPrice: (Optional) 订单原价 包年时 一年原价为12个月价格，totalPrice为10个月价格
        :param resourceId: (Optional) 资源id
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param site: (Optional) 站点  0:主站  其他:专有云
        :param region: (Optional) 地域
        :param billingType: (Optional) 计费类型1:按配置2:按用量3:包年包月
        :param timeSpan: (Optional) 时长
        :param timeUnit: (Optional) 时长类型 1:小时2:天3:月4:年
        :param networkOperator: (Optional) 网络类型 0:non1:非BGP2:BGP
        :param formula: (Optional) 配置信息
        :param favorableInfo: (Optional) FavorableInfo转成json后的字符串
        :param priceSnapShot: (Optional) 价格快照
        :param pin: (Optional) 用户pin
        :param taskId: (Optional) 自然单列表
        :param startTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        :param processType: (Optional) 变配明细（1-升配补差价，2-降配延时）
        :param sourceId: (Optional) 交易单模块sourceId
        """

        self.price = price
        self.priceScale4 = priceScale4
        self.discount = discount
        self.discountedPrice = discountedPrice
        self.originalPrice = originalPrice
        self.resourceId = resourceId
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.site = site
        self.region = region
        self.billingType = billingType
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.networkOperator = networkOperator
        self.formula = formula
        self.favorableInfo = favorableInfo
        self.priceSnapShot = priceSnapShot
        self.pin = pin
        self.taskId = taskId
        self.startTime = startTime
        self.endTime = endTime
        self.processType = processType
        self.sourceId = sourceId
