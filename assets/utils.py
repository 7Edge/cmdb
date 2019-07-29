#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: utils
# Date: 7/29/2019
import logging


def get_logger(name):
    return logging.getLogger('cmdb.' + name)


if __name__ == '__main__':
    pass
