#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: api
# Date: 7/30/2019
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import HttpResponse, render, render_to_response, redirect, reverse
from django.http.response import HttpResponse, JsonResponse

from django.views import View

logger = logging.getLogger('cmdb-client.' + 'api')


# 上报接口
class AssetAPIView(APIView):

    def post(self, request, *args, **kwargs):
        asset_data = request.data.get('asset_data')
        logger.info('新增资产数据 %s' % asset_data)
        return Response({
            'code': 100,
            'msg': '资产数据上报成功！',
            'data': asset_data
        })


if __name__ == '__main__':
    pass
