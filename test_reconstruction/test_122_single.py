# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage, Single_choice,Vobcabulary
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
        cls.single_page = Single_choice()
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
                if '测试重构3' in var[1]:
                    time.sleep(2)
                    self.home_page.test_reconstruction_three()
                    time.sleep(2)
                    self.homework_exist()
                    break


                else:
                    Swipe().swipe_up(1000)

                    time.sleep(2)



    def homework_exist(self):


        count = self.homework.sengle_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.single_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 单项选择 ':

                self.single_page.single_bound_num(i)


                time.sleep(1)
                self.mothed()
                time.sleep(3)
                self.vob_page.end_page()
                self.end_pege.reerror()
                self.mothed()
                time.sleep(3)
                self.vob_page.end_page()
                self.end_pege.check_answer()
                self.single_page.show_answer()
                self.end_pege.back_btn()
                #点击返回这个按钮
                self.end_pege.back_btn()
                # 点击返回这个按钮
                self.end_pege.back_btn()

    def mothed(self):
        time.sleep(3)

        j = 0
        max_num = int(self.single_page.rate())
        for i in range(int(max_num)):
            self.single_page.grey_btn()
            self.single_page.time_view_begin()
            max_num = int(self.single_page.rate())
            j = j + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            options = self.single_page.option_button()
            time.sleep(1)
            options[random.randint(4, len(options) - 1)].click()  # 随机点击选项
            self.single_page.time_view_end()
            ele = self.single_page.light_btn()
            if ele.text == "doneItem":
                ele.click()
                time.sleep(2)
            # elif self.single_page.gary_btn_text() == "doneItemNo":
            elif ele.text == "doneItemNo":
                print('恭喜 回答正确')
            # 到了这个页面之后,点击查看答案
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
