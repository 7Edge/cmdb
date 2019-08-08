#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: response
# Date: 8/2/2019
"""
响应对象，用于管理响应数据
"""


class BaseResponse(object):
    """
    基础响应类，宝航code与msg
    """

    def __init__(self):
        self.code = 1000
        self.msg = 'success'

    @property
    def dict(self):
        """
        返回一个字典，对象中管理的数据。
        :return:
        """
        return self.__dict__


class DataResponse(BaseResponse):
    """
    返回数据
    """

    def __init__(self):
        super().__init__()
        self.data = None


if __name__ == '__main__':
    pass
