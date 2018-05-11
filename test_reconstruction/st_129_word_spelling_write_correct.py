# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Word_spelling,Vobcabulary
from app.student.homework.object_page.end_page import Words_end
from utils.screen_swipe import Swipe
from conf.decorator import setup, teardown, testcase, teststeps
from conf.basepage import BasePage


class Games(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""

        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.vob_page = Vobcabulary()
        cls.word_page = Word_spelling()

    @classmethod
    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_homework(self):
        """对不同小游戏类型，选择不同函数进行相应的操作"""
        # self.login_page.login()
        time.sleep(5)

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
                    self.word_spelling()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)
                    # self.home_page.item_list()
                    # self.chioce_blank()


    def word_spelling(self):
        count = self.homework.word_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.word_type(i).text
             # 获取小游戏类型
            if var == ' 单词拼写 ':
                self.word_page.word_write()
                print('进入小题，开始作答！！！')
                self.mothed()
                self.vob_page.end_page()
                self.word_page.again_practice()

                self.mothed()
                self.vob_page.end_page()
                time.sleep(1)
                self.word_page.chick_answer()
                self.word_page.clcik_voice()
                self.word_page.show_answer()
                self.word_page.return_btn()
                self.word_page.return_btn()
                self.word_page.return_btn()



            break

    def mothed(self):
        j = 0
        # time.sleep(1)
        # self.two_homework.chick_question()
        time.sleep(1)
        max_num = int(self.word_page.max_number())
        # 获取到我们需要的最大的题数
        for i in range(0, int(max_num)):
            self.word_page.grey_btn()
            self.word_page.time_view_begin()
            max_num = int(self.word_page.max_number())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            self.word_page.determination()
            self.word_page.word_text()
            self.word_page.time_view_end()
            time.sleep(1)
            self.word_page.arrow()
            self.word_page.again_arrow()
            time.sleep(3)
            print("--------------------------")
            time.sleep(1)

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
