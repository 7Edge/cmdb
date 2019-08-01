#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: searializers
# Date: 7/31/2019
from rest_framework import serializers
from rest_framework import fields

from .models import NewAssetApprovalZone


# 预审批资产序列化
class NewAssetApprovalZoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAssetApprovalZone
        fields = "__all__"


if __name__ == '__main__':
    pass
