#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: searializers
# Date: 7/31/2019
from rest_framework import serializers
from rest_framework import fields
from rest_framework import relations

from .models import NewAssetApprovalZone
from .models import Asset
from .models import IDC


# 预审批资产序列化
class NewAssetApprovalZoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAssetApprovalZone
        fields = "__all__"


# 资产序列化对象
class AssetSerializer(serializers.ModelSerializer):
    """
    资产序列化类
    """
    asset_type_choice = fields.JSONField(read_only=True)  # 返回选项对应的display值，方便前端渲染方式一
    asset_status = fields.SerializerMethodField()  # 放回选项对应display值的字典，方便前端渲染方式二

    class Meta:
        model = Asset
        fields = "__all__"

    def get_asset_status(self, obj):
        return dict(obj.asset_status)

    # asset_type = fields.ChoiceField(choices=Asset.asset_type_choice)
    # name = fields.CharField(max_length=64)
    # sn = fields.CharField(max_length=128)
    # business_unit = fields.CharField(allow_blank=True, allow_null=True)
    # status = fields.ChoiceField(choices=Asset.asset_status)
    # manufacturer = fields.CharField(allow_blank=True, allow_null=True)
    #
    # manage_ip = fields.IPAddressField(allow_blank=True, allow_null=True)
    #
    # tags = relations.PrimaryKeyRelatedField()
    #
    # admin = fields.CharField(allow_null=True, allow_blank=True)
    #
    # idc = fields.CharField(allow_blank=True, allow_null=True)
    # contract = fields.CharField(allow_blank=True, allow_null=True)
    # purchase_day = fields.Date(allow_blank=True, allow_null=True)


# IDC序列化类
class IDCModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = '__all__'


if __name__ == '__main__':
    pass
