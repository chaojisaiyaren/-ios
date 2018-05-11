#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import HTMLTestRunner
import re
import time
import os


from conf.base_config import GetVariable as gv


class RunCase:
    def __init__(self):

        if not os.path.exists(gv.REPORT_ROOT):
            os.mkdir(gv.REPORT_ROOT)

        date_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        self.test_report_path = gv.REPORT_ROOT  + '/'  + date_time


        if not os.path.exists(self.test_report_path):
            os.mkdir(self.test_report_path)
        # self.file_name = 'TestReport_' + date_time + '.html'  # 这个filename是生成的自动化测试报告的文件名

        # self.file_name = self.test_report_path + '/TestReport_' + date_time + '.html'  # 这个filename是生成的自动化测试报告的文件名
        self.file_name = self.test_report_path  + date_time + '.html'
    def get_path(self):

        return self.test_report_path



    def run(self, cases):
        desc = '用例执行情况统计：'
        report_title = '测试用例执行报告'
        print(self.file_name)
        fp = open(self.file_name, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=report_title,
                description=desc)
        runner.run(cases)
        fp.close()

        # desc = '用例执行情况：'
        # result = BeautifulReport(cases)
        # result.report(filename=self.file_name,
        #               description=desc,
        #               log_path=self.test_report_path)
