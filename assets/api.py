#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: api
# Date: 7/30/2019
import json
import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewAssetApprovalZoneModelSerializer

logger = logging.getLogger('cmdb-client.' + 'api')


# 上报接口
class AssetAPIView(APIView):

    def post(self, request, *args, **kwargs):
        asset_data = request.data.get('asset_data')

        asset_data.update({'data': json.dumps(asset_data)})

        serializer_obj = NewAssetApprovalZoneModelSerializer(data=asset_data, partial=True)
        if serializer_obj.is_valid():
            # serializer_obj.save()
            print(serializer_obj.validated_data)
            serializer_obj.save()

        logger.info('新增资产数据 %s' % asset_data)

        return Response({
            'code': 100,
            'msg': '资产数据上报成功！',
            'data': asset_data,
            'error': serializer_obj.errors
        })


if __name__ == '__main__':
    pass
