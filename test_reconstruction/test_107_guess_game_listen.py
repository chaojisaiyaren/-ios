# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Guess_game,Vobcabulary
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
        cls.guess_page = Guess_game()
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
                if '测试重构1' in var[1]:
                    time.sleep(2)
                    self.home_page.test_reconstruction_one()
                    time.sleep(2)
                    self.guess_game()
                    break


                else:
                    Swipe().swipe_up(1000)


                    time.sleep(2)
                    # self.home_page.item_list()
                    # self.chioce_blank()

    def guess_game(self):
        #猜词游戏
        count = self.homework.guess_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.guess_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 猜词游戏 ':
                print(var)

                self.guess_page.guess_listen()

                time.sleep(1)
                # self.two_homework.chick_question()
                self.mothed()
                print("进入结果页面")
                self.vob_page.end_page()
                self.guess_page.wrong_again()
                self.mothed1()
                print("再次进入结果页面")
                self.vob_page.end_page()
                self.guess_page.chick_answer()
                self.guess_page.clcik_voice()
                self.guess_page.show_answer()
                time.sleep(1)
                self.guess_page.return_btn()
                self.guess_page.return_btn()
                self.guess_page.return_btn()



            break

    def mothed(self):
        max_num = int(self.guess_page.guess_max_listen())
        # 获取到我们需要的最大的题数
        # j = 0
        for i in range(0, int(max_num)):
            self.guess_page.time_view_begin()
            # self.guess_page.letter()
            self.guess_page.word()
            self.guess_page.time_view_end()
            print("输入六次失败，自动跳转下一题")

    def mothed1(self):
        max_num = int(self.guess_page.guess_max_listen())
        # 获取到我们需要的最大的题数
        j = 0
        for i in range(0, int(max_num)):
            self.guess_page.time_view_begin()
            j = j + 1
            max_num = int(self.guess_page.guess_max_listen())
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            self.guess_page.word_correct()
            self.guess_page.time_view_end()
            print("输入单词正确，两秒之后进入下一题")
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
