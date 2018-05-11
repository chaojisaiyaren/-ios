# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Sentence_conversion,Vobcabulary
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
        cls.sentence_page = Sentence_conversion()
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
                    self.sentence_conversion()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)

    def sentence_conversion(self):
        #句型转换

        count = self.homework.sentence_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.sentence_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 句型转换 ':
                print(var)
                time.sleep(2)
                self.sentence_page.sentence_bound_num(i)
                self.mothed()
                self.vob_page.end_page()
                self.sentence_page.wrong_again()
                self.mothed()
                self.vob_page.end_page()
                self.sentence_page.chick_answer()
                self.sentence_page.show_answer()
                self.sentence_page.return_btn()
                self.sentence_page.return_btn()
                self.sentence_page.return_btn()


            break
    def mothed(self):

        time.sleep(2)
        # self.two_homework.chick_question()
        # time.sleep(1)
        j = 0
        max_num = int(self.sentence_page.sentence_max_num())
        # 获取到我们需要的最大的题数
        for i in range(0, int(max_num)):
            self.sentence_page.grey_btn()
            self.sentence_page.time_view_begin()
            j = j + 1
            max_num = int(self.sentence_page.sentence_max_num())
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            time.sleep(2)
            word_num = self.sentence_page.words_num()
            frequency = (len(word_num) - 1) / 2 - 1
            num = self.sentence_page.choice_blanck_num()
            num_blank = (len(num) + 2) / 2
            print("num_blank", num_blank)
            for j in range(0, int(frequency)):

                self.sentence_page.choice_blank(int(num_blank)).click()
            self.sentence_page.time_view_end()
            self.sentence_page.arrow()
            time.sleep(2)
            self.sentence_page.again_arrow()
            time.sleep(2)

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
