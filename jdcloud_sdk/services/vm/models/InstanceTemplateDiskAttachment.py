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


class InstanceTemplateDiskAttachment(object):

    def __init__(self, diskCategory=None, autoDelete=None, instanceTemplateDisk=None, deviceName=None, noDevice=None):
        """
        :param diskCategory: (Optional) 磁盘分类，取值为本地盘(local)或者数据盘(cloud)。
系统盘支持本地盘(local)或者云硬盘(cloud)。系统盘选择local类型，必须使用localDisk类型的镜像；同理系统盘选择cloud类型，必须使用cloudDisk类型的镜像。
数据盘仅支持云硬盘(cloud)。

        :param autoDelete: (Optional) 随云主机一起删除，删除主机时自动删除此磁盘，默认为true，本地盘(local)不能更改此值。
如果云主机中的数据盘(cloud)是包年包月计费方式，此参数不生效。
如果云主机中的数据盘(cloud)是共享型数据盘，此参数不生效。

        :param instanceTemplateDisk: (Optional) 数据盘配置
        :param deviceName: (Optional) 数据盘逻辑挂载点，取值范围：vda,vdb,vdc,vdd,vde,vdf,vdg,vdh,vdi。系统盘不需要使用，数据盘时才能够使用。
        :param noDevice: (Optional) 排除设备，使用此参数noDevice配合deviceName一起使用。
创建打包镜像：如deviceName:vdb、noDevice:true，则表示云主机中的数据盘vdb不参与创建镜像。
创建模板：如deviceName:vdb、noDevice:true，则表示镜像中的数据盘vdb不参与创建主机。
创建主机：如deviceName:vdb、noDevice:true，则表示镜像中的数据盘vdb，或者模板(使用模板创建主机)中的数据盘vdb不参与创建主机。

        """

        self.diskCategory = diskCategory
        self.autoDelete = autoDelete
        self.instanceTemplateDisk = instanceTemplateDisk
        self.deviceName = deviceName
        self.noDevice = noDevice
