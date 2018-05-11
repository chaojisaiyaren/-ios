# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Cloze,Vobcabulary
from app.student.homework.object_page.end_page import Words_end
from utils.screen_swipe import Swipe
from conf.decorator import setup, teardown, testcase, teststeps


class Games(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""

        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.cloze_page = Cloze()
        cls.vob_page = Vobcabulary()
    @classmethod
    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_homework(self):
        """对不同小游戏类型，选择不同函数进行相应的操作"""
        # self.login_page.login()
        time.sleep(5)

        self.login_page.app_status1()

        time.sleep(2)

        if self.home_page.wait_check_page() == "试卷":
            print("登录成功")
            # 进入首页后点击作业条目
            while True:
                time.sleep(2)

                var = self.homework.judge_homework_exist()
                # and '稍难' in var[3][0]
                if '测试重构3' in var[1]:
                    time.sleep(2)
                    self.home_page.test_reconstruction_three()
                    time.sleep(2)
                    self.cloze()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)



    def cloze(self):
    #进入完形填空的条件
        count = self.homework.cloze_count()
        print(len(count))
        time.sleep(3)
        for i in range(0, len(count)):
            var = self.homework.cloze_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 完形填空 ':
                self.cloze_page.cloze_bound_num(i)
                self.mothed()
                self.cloze_page.cloze_arrow()
                self.vob_page.end_page()
                self.cloze_page.wrong_problem()
                self.mothed()
                self.cloze_page.cloze_arrow()
                self.vob_page.end_page()
                self.cloze_page.check_answer()
                self.cloze_page.show_answer()
                self.cloze_page.back_btn()
                self.cloze_page.back_btn()
                self.cloze_page.back_btn()

    def mothed(self):
        self.cloze_page.small_font()
        self.cloze_page.ordinary_front()
        self.cloze_page.big_front()
        max_num = int(self.cloze_page.cloze_num())
        j = 0
        print("我们需要的答案的个数", max_num)
        for i in range(0, int(max_num)):
            self.cloze_page.grey_btn()
            self.cloze_page.time_view_begin()
            max_num = int(self.cloze_page.cloze_num())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            # self.cloze_page.random_choice(i)
            # time.sleep(1)
            options = self.cloze_page.cloze_option_button(i)
            time.sleep(1)
            # print(len(options))
            options.click()  # 一次点击A
            self.cloze_page.time_view_end()
            time.sleep(3)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Games('test_homework'))

    report_title = u'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = r'/Users/work/test_IOS/storges/test_report/screen_shot/Result_' + timestr + '.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=report_title,
        description=desc)
    runner.run(suite)
    fp.close()
