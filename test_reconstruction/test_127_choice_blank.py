# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage, Choice_words,Vobcabulary
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
        cls.choice_blank = Choice_words()
        cls.end_pege = Words_end()
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
                    self.chioce_blank()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)


    def chioce_blank(self):

        count = self.homework.homework_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.tv_testbank_type(i).text
            print(var)                  # 获取小游戏类型
            if  var == ' 选词填空 ':
                print(var)
                self.choice_blank.click_bounds_num(i)
                self.mothed()
                self.choice_blank.arrow()
                self.vob_page.end_page()
                self.end_pege.reerror()
                self.mothed()
                self.choice_blank.arrow()
                self.vob_page.end_page()
                self.end_pege.check_answer()
                self.choice_blank.show_answer()
                self.end_pege.back_button()
                self.end_pege.back_button()
                self.end_pege.back_button()
                # else:
                #     print("不太对")
    def mothed(self):
        j = 0
        self.choice_blank.small_font()
        self.choice_blank.ordinary_front()
        self.choice_blank.big_front()
        max_num = int(self.choice_blank.max_number())
        for i in range(0, int(max_num)):
            self.choice_blank.grey_btn()
            self.choice_blank.time_view_begin()
            j = j + 1
            max_num = int(self.choice_blank.max_number())
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            chick = self.choice_blank.chose_blank(i)
            chick.click()
            self.choice_blank.word()
            self.choice_blank.time_view_end()



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
