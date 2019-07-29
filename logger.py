#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: logger
# Date: 7/26/2019
from logging.config import dictConfig

# 全局log组件对象配置
cfg = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO'
        },
        'time_rotate_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'filename': './logs/cmdb.log',
            'formatter': 'detailed'
        },
        'errors': {
            'class': 'logging.FileHandler',
            'filename': './logs/errors.log',
            'formatter': 'detailed'
        }
    },
    'loggers': {
        'cmdb': {
            'handlers': ['console', 'time_rotate_file', 'errors']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'errors']
    },
}


def init_logger():
    dictConfig(cfg)


init_logger()

if __name__ == '__main__':
    import logging

    tlogger = logging.getLogger('cmdb.' + __name__)
    print(tlogger.getEffectiveLevel())
    tlogger.info('test info')
    tlogger.warning('test warning')
