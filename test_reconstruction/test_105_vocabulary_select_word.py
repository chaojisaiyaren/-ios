# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, HomePage,VocabularySelection,Vobcabulary
from app.student.homework.object_page.end_page import Words_end
from utils.screen_swipe import Swipe
from conf.decorator import setup, teardown, testcase, teststeps
from utils.vob_data import vob_operate_word



class Games(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""

        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
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
            # 进入首页后点击作业x条目
        while True:
            var = self.homework.judge_homework_YB()

            if '测试重构1' in var[1] and '测试重构1' in var[3][0]:

                # self.homework_exist(var[1].index + 1, var[2], var[3])
                self.home_page.test_reconstruction_one()
                self.vob_selection_explantion()
                break

            else:
                Swipe().swipe_up(1000)
                self.home_page.test_reconstruction_one()
                self.vob_selection_explantion()

                break

    def vob_selection_explantion(self):
        # 进入词汇选择的条件
        count = self.homework.vob_count()
        title_type = self.vob_page.vob_explanation_reconstruction()
        print(title_type)
        print(len(count))
        time.sleep(3)
        for i in range(0, len(count)):
            var = self.homework.vob_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 词汇选择 ' and title_type == '选解释':
                print(var)
                self.vob_page.vob_word()
                time.sleep(2)
                self.method()

            break
        self.vob_page.end_page()
        self.vob_page.wrong_problem()
        self.mothed()
        self.vob_page.end_page()
        print("第二次的做题正确率，星星数目，积分和做题时间大于等于第一次做题的正确率星星数目和积分和做题时间")
        self.vob_page.chick_answer()
        self.vob_page.clcik_voice()
        self.vob_page.show_answer()
        self.vob_page.return_btn()
        self.vob_page.return_btn()
        self.vob_page.return_btn()
        time.sleep(2)



    def method(self):
        max_num = int(self.vob_page.vob_explantion_num_reconstruction())
        j = 0
        time.sleep(1)
        for i in range(int(max_num)):
            self.vob_page.grey_btn()
            self.vob_page.time_view_begin()
            j = j + 1
            max_num = int(self.vob_page.vob_explantion_num_reconstruction())
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            options = self.vob_page.vob_option_button()
            time.sleep(1)
            options[random.randint(1, len(options) - 1)].click()  # 随机点击选项
            self.vob_page.time_view_end()
            self.vob_page.light_btn()
            print("----------------------")
            time.sleep(2)

    def mothed(self):
        time.sleep(2)
        max_num = self.vob_page.vob_explantion_num_reconstruction()
        j = 0
        time.sleep(1)

        for i in range(int(max_num)):
            self.vob_page.grey_btn()
            self.vob_page.time_view_begin()
            j = j + 1
            max_num = int(self.vob_page.vob_explantion_num_reconstruction())
            print("进入第%d题,我们需要完成的小题的数目%d" % (j, max_num))
            time.sleep(2)
            self.vob_page.options_word(self.vob_option()).click()
            time.sleep(3)
            self.vob_page.time_view_end()
            self.vob_page.light_btn()
            print("输入正确后，点击下一步按钮进入下一题")
            print("------------------------------------------------")



    def vob_option(self):
        # 得到我们正确答案的列表的下表盘
        time.sleep(2)
        value = vob_operate_word(self.vob_page.word())
        time.sleep(2)
        print("我们选择正确的单词是：",value)
        index = [i for i, x in enumerate(self.vob_page.option()) if x == value][0]

        return index



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
