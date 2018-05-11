# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, FlashCard

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
        cls.flash_page = FlashCard()




    @classmethod
    @teardown
    def tearDown(self):
        pass

    def test_exercise(self):
        """对不同小游戏类型，选择不同函数进行相应的操作"""
        # self.login_page.login()

        time.sleep(2)
        self.login_page.app_status()
        time.sleep(2)
        if self.home_page.wait_check_page() == "试卷":
            print("登录成功")
            # 进入首页后点击作业x条目
        while True:
            var = self.homework.judge_homework_YB()

            if '测试重构1' in var[1] and '测试重构1' in var[3][0]:

                # self.homework_exist(var[1].index + 1, var[2], var[3])
                self.home_page.test_reconstruction_one()
                self.flash_exersise_stduy()
                break

            else:
                Swipe().swipe_up(1000)
                self.home_page.test_reconstruction_one()
                self.flash_exersise_stduy()

                break

    def flash_exersise_stduy(self):
        Swipe().swipe_up(1000)
        count = self.homework.flash_count()
        # exercise_type = self.flash_page.flash_study()
        # print(exercise_type)
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.flash_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 闪卡练习 ':

                self.flash_page.flash_study_reconstruction()
                self.mathed()

                time.sleep(1)
                self.flash_page.mark_again()
                self.mathed1()
                time.sleep(1)
                self.flash_page.return_btn()
                time.sleep(1)
                self.flash_page.return_btn()
                time.sleep(1)

            break

    def mathed(self):
        max_num = int(self.flash_page.max_number_reconstruction1())
        j = 0
        # 获取到我们需要的最大的题数
        self.flash_page.word_explain()
        self.flash_page.word_explain1()
        self.flash_page.chick_blank()
        for i in range(0, int(max_num)):
            max_num = int(self.flash_page.max_number_reconstruction1())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            time.sleep(1)
            self.flash_page.click_star()
            time.sleep(1)
            self.flash_page.word()
            self.flash_page.chick_flash_study()
            self.flash_page.explanation()

            # 点击一下空白的地方
            self.flash_page.arrow()

    def mathed1(self):
        max_num = int(self.flash_page.max_number_reconstruction1())
        j = 0
        # 获取到我们需要的最大的题数
        self.flash_page.word_explain()
        self.flash_page.word_explain1()
        # self.flash_page.chick_blank_single()
        self.flash_page.chick_blank()
        for i in range(0, int(max_num)):
            max_num = int(self.flash_page.max_number_reconstruction1())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            time.sleep(1)
            self.flash_page.word()
            self.flash_page.chick_flash_study()
            self.flash_page.explanation()
            # 点击一下空白的地方
            self.flash_page.arrow()


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
