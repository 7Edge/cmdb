#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: urls
# Date: 7/30/2019
from django.urls import re_path
from .api import AssetAPIView, IDCAPIView

urlpatterns = [
    re_path('^assets/', AssetAPIView.as_view(), name='assets'),
    re_path('^idc/', IDCAPIView.as_view(), name='idc')
]

if __name__ == '__main__':
    pass
