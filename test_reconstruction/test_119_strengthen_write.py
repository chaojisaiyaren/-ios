# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,Strengthen_sentence,Vobcabulary
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
        cls.strengthen_page = Strengthen_sentence()
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
                    self.strengthen_silent()
                    break


                else:
                    Swipe().swipe_up(1000)


                    time.sleep(2)
                    # self.home_page.item_list()
                    # self.chioce_blank()

    def strengthen_silent(self):
        #默写模式
        count = self.homework.strengthen_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.strengthen_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 强化炼句 ':
                print(var)

                self.strengthen_page.click_strengthen_write()
                print('进入小题，开始作答！！！')
                self.mothed()
                self.vob_page.end_page()
                self.strengthen_page.wrong_again()

                self.mothed()
                self.vob_page.end_page()
                time.sleep(1)
                self.strengthen_page.chick_answer()
                # self.strengthen_page.clcik_voice()
                self.strengthen_page.show_answer()
                self.strengthen_page.return_btn()
                self.strengthen_page.return_btn()
                self.strengthen_page.return_btn()

            break
    def mothed(self):
        j = 0
        time.sleep(1)
        # self.two_homework.chick_question()
        time.sleep(1)
        max_num = int(self.strengthen_page.silent_max_num())
        # 获取到我们需要的最大的题数
        for i in range(0, int(max_num)):
            self.strengthen_page.grey_btn()
            self.strengthen_page.time_view_begin()
            max_num = int(self.strengthen_page.silent_max_num())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            silent_list = self.strengthen_page.horizontal_line()
            # 获取整个横线上的列表
            for j in range(0, len(silent_list)):
                # 进行遍历然后一次点击
                silent_list[j].click()
                self.strengthen_page.word()
            self.strengthen_page.time_view_end()
            self.strengthen_page.arrow()
            time.sleep(1)
            self.strengthen_page.again_arrow()
            print("------------------------")
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
