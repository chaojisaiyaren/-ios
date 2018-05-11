# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, FlashCard, Match_exerciser,Vobcabulary
from conf.decorator import setup, teardown, testcase, teststeps
from utils.screen_swipe import *


class Games(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""

        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.vob_page = Vobcabulary()


        # self.vocab_select = VocabularySelection(driver)
        cls.match_page =Match_exerciser()


    @classmethod
    @teardown
    def tearDown(self):
        pass

    def test_match_sentence(self):
        """对不同小游戏类型，选择不同函数进行相应的操作"""
        # self.login_page.login()

        time.sleep(2)
        self.login_page.app_status()
        time.sleep(2)
        if self.home_page.wait_check_page() == "试卷":
            print("登录成功")
            # 进入首页后点击作业条目
            while True:
                time.sleep(2)
                var = self.homework.judge_homework_exist()
                # and '稍难' in var[3][0]
                if '测试重构2' in var[1]:
                    time.sleep(2)
                    # self.homework_exist(var[1].index + 1, var[2], var[3])
                    self.home_page.test_reconstruction_two()
                    time.sleep(2)
                    self.match_sentence()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)
                    # self.home_page.item_list()
                    # self.chioce_blank()

    def match_sentence(self):
        Swipe().swipe_up(1000)
        count = self.homework.match_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.match_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 连连看 ':
                print(var)

                self.match_page.match_bound_num(i)

                time.sleep(1)
                # self.two_homework.chick_question()

                max_num = self.match_page.max_number_YB()
                print(len(max_num))

                # 获取到我们需要的最大的题数

                self.match_page.list_re()
                self.match_page.list_again()
                self.vob_page.end_page()
                self.match_page.again()
                self.match_page.list_re()
                self.match_page.list_again()
                self.vob_page.end_page()
                self.match_page.chick_answer()
                self.match_page.clcik_voice()
                self.match_page.show_answer()
                self.match_page.return_btn()
                self.match_page.return_btn()
                self.match_page.return_btn()



            break


def num():
    suite = unittest.TestSuite()
    suite.addTest(Games('test_match_sentence'))
    report_title = u'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = r'/Users/work/test_IOS/storges/test_report/' + 'TestReport_' + timestr + '.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=report_title,
        description=desc)
    runner.run(suite)
    fp.close()

if __name__ == '__main__':
    num()
