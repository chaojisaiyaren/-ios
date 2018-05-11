# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Listen_practice,Vobcabulary
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
        cls.listen_page = Listen_practice()
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
                if '测试重构4' in var[1]:
                    time.sleep(2)
                    self.home_page.test_reconstruction_four()
                    time.sleep(2)
                    self.listen_practice()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)

    def listen_practice(self):
        count = self.homework.listen_practice_count()
        print(len(count))
        time.sleep(3)
        for i in range(0, len(count)):
            var = self.homework.listen_practice_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 听力练习 ':
                print(var)
                self.listen_page.listen_bound_num(i)
                self.listen_page.time_view_begin()
                self.mothed()
                self.listen_page.time_view_end()
                time.sleep(20)
                self.listen_page.listen_arrow()
                self.vob_page.end_page()
                self.listen_page.practice_again()
                self.listen_page.time_view_begin()
                self.mothed()
                time.sleep(20)
                self.listen_page.time_view_end()
                time.sleep(1)
                self.listen_page.listen_arrow()
                self.vob_page.end_page()
                self.listen_page.check_answer()
                self.listen_page.back_btn()
                self.listen_page.back_btn()
                self.listen_page.back_btn()

    def mothed(self):
        max_num = int(self.listen_page.listen_num())
        print("我们需要的答案的个数", max_num)
        self.listen_page.listen_speaker()
        time.sleep(3)
        j = 0
        for i in range(0, int(max_num)):
            self.listen_page.grey_btn()
            self.listen_page.time_view_begin()
            max_num = int(self.listen_page.listen_num())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))

            options = self.listen_page.listen_option_button(i)
            time.sleep(1)
            # print(len(options))
            options.click()  # 依次点击A
            Swipe().swipe_up(1000)






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
