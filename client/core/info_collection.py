#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: info_collection
# Date: 7/29/2019
import sys
import logging
import platform

logger = logging.getLogger('cmdb-client.' + __name__)


class InfoCollection(object):
    """
    InfoCollection 用于收集当前平台的信息
    """
    SYS_TYPE = platform.system()

    def collect(self):
        try:
            func = getattr(self, InfoCollection.SYS_TYPE.lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            logger.critical('cmdb-client不支持当前操作系统：%s' % InfoCollection.SYS_TYPE)
            sys.exit('cmdb-client不支持当前操作系统：%s' % InfoCollection.SYS_TYPE)

    @staticmethod
    def build_report_data(data):
        """
        数据清洗
        :param data:
        :return:
        """
        pass
        return data

    @staticmethod
    def linux():
        from plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info import Win32Info
        return Win32Info().collect()


if __name__ == '__main__':
    pass
