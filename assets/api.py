#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: api
# Date: 7/30/2019
import json
import logging
import copy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import NewAssetApprovalZoneModelSerializer, AssetSerializer, IDCModelSerializer
from .etc.response import DataResponse
from .models import Asset, NewAssetApprovalZone, IDC

logger = logging.getLogger('cmdb.' + 'api')


# 上报接口
class AssetAPIView(APIView):
    """
    资产新增到预审批表：
        如果资产已经在资产表存在，则部分更新提交的数据。
        如果资产不存在，则新建到预审批表中。
    """

    def post(self, request, *args, **kwargs):
        result_data = DataResponse()
        try:
            asset_data = request.data.get('asset_data')  # 获取资产数据字典
            data = copy.deepcopy(json.loads(asset_data))
            data.update({'data': asset_data})  # 将资产地json字符串更新到data中

            # 判定资产sn是否已存在，存在更新，不存在新增
            sn = data.get('sn')
            asset_obj = Asset.objects.filter(sn=sn).first()
            approval_asset_obj = NewAssetApprovalZone.objects.filter(sn=sn).first()

            # 根据是否存在于已有资产，或者存在于审批资产来做更新或者新增操作
            if asset_obj:  # 资产存在，进行部分更新操作。
                asset_serializer = AssetSerializer(instance=asset_obj, data=data, partial=True)  # 都是部分更新。
                if asset_serializer.is_valid():
                    obj = asset_serializer.save()
                    logger.info('更新资产信息 %s 更新 %s' % (obj.sn, asset_serializer.validated_data))

                    result_data.data = asset_serializer.data
                    result_data.msg = '更新资源成功'

                else:
                    result_data.msg = '更新资产信息失败！'
                    result_data.code = 1003
                    result_data.error = asset_serializer.errors
            elif approval_asset_obj:  # 预审批资产存在
                approval_asset_serializer = NewAssetApprovalZoneModelSerializer(instance=approval_asset_obj,
                                                                                data=data,
                                                                                partial=True)
                if approval_asset_serializer.is_valid():
                    obj = approval_asset_serializer.save()
                    logger.info('更新预审批资产信息 %s 更新 %s' % (obj.sn, approval_asset_serializer.validated_data))

                    result_data.data = approval_asset_serializer.data
                    result_data.msg = '更新预审批资产信息成功！'
                else:
                    result_data.msg = '更新资产信息失败！'
                    result_data.code = 1003
                    result_data.error = approval_asset_serializer.errors

            else:  # 新增预审批资产
                serializer_obj = NewAssetApprovalZoneModelSerializer(data=data)
                if serializer_obj.is_valid():
                    obj = serializer_obj.save()
                    logger.info('新增预审批资产信息 %s 新增 %s' % (obj.sn, serializer_obj.validated_data))

                    result_data.data = serializer_obj.data
                    result_data.msg = "上报预审批资产成功！"
                else:
                    result_data.code = 1003
                    result_data.msg = 'deserialized fail!'
                    result_data.error = serializer_obj.errors
        except Exception as e:
            logger.error(msg='%s' % e)
            result_data.code = 1002
            result_data.msg = 'server error!'
            return Response(result_data.dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result_data.dict, status=status.HTTP_200_OK)


# IDC接口
class IDCAPIView(APIView):
    """
    IDC
    """

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')

        obj = IDC.objects.filter(name=name).first()
        ser_obj = IDCModelSerializer(data=request.data, instance=obj)

        print('request.data:', request.data)
        print('is_valid结果：', ser_obj.is_valid())
        print('errors:', ser_obj.errors)
        print('validated_data', ser_obj.validated_data)
        instance = ser_obj.save()

        print('data', ser_obj.data)
        print('instance', instance)
        return Response('test')


if __name__ == '__main__':
    pass
