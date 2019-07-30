#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: main
# Date: 7/29/2019
import os
import sys
# BASE_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.getcwd())

sys.path.append(BASE_DIR)

from utils import logger
from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
