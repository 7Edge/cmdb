#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: logger
# Date: 7/26/2019
from logging.config import dictConfig

cfg = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': '../log/cmdb-client.log',
            'formatter': 'detailed'
        },
        'errors': {
            'class': 'logging.FileHandler',
            'filename': '../log/errors.log',
            'formatter': 'detailed'
        }
    },
    'loggers': {
        'cmdb-client': {
            'handlers': ['file', 'errors'],
            'level': 'INFO'
        }
    }
}


def init_logger():
    dictConfig(cfg)


init_logger()

if __name__ == '__main__':
    pass
