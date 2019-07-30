#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: handler
# Date: 7/29/2019
import json
import time
import logging
import urllib.parse
import urllib.request
from core import info_collection
from conf import settings

logger = logging.getLogger('cmdb-client')


class ArgvHandler(object):
    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        """
        分析执行的参数，如果执行的参数子命令有，则执行该功能，否则打印帮助信息
        :return:
        """
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.help_msg()

    @staticmethod
    def help_msg():
        """
        版主说明
        :return:
        """
        msg = '''
                参数名               功能

                collect_data        测试收集硬件信息的功能

                report_data         收集硬件信息并汇报
                '''
        print(msg)

    @staticmethod
    def collect_data():
        """
        收集硬件信息
        :return:
        """
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        """
        收集硬件信息，然后发送到服务器
        :return:
        """
        info = info_collection.InfoCollection()
        asset_data = info.collect()

        data = {"asset_data": json.dumps(asset_data)}

        url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])

        try:
            data_encode = urllib.parse.urlencode(data).encode()
            logger.info('Send asset %s to %s' % (data, url))
            response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
            msg = response.read().decode()

            logger.info('Response %s from %s' % (msg, url))
        except Exception as e:
            logger.warning('发送失败，错误原因：%s' % e)


if __name__ == '__main__':
    pass
