# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner
from appium import webdriver
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.object_page.home_page import HomePage, Tow_homepage
from app.student.homework.object_page.games_page import Homework, FlashCard, Choice_words, Word_spelling
from app.student.user_center.object_page.user_Info_page import UserInfoPage
from app.student.user_center.object_page.user_center_page import UserCenterPage
from utils.remote_info import RemoteInfo
from utils.yb_data import yb_letter
from utils.screen_swipe import *
from utils.click_bounds import games_keyboard,click_bounds,guess_keyboard

report_path = r'/Users/work/test_IOS/storges/test_report/'

class Games(unittest.TestCase):

    def setUp(self):
        """启动应用"""
        global driver
        remote = RemoteInfo().remote_info_511()
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', remote)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.homework = Homework(driver)
        self.user_center = UserCenterPage(driver)
        self.user_info = UserInfoPage(driver)
        self.flash_card = FlashCard(driver)
        self.two_homework = Tow_homepage(driver)
        # self.vocab_select = VocabularySelection(driver)
        self.choice_blank = Choice_words(driver)
        self.word_page = Word_spelling(driver)

    def tearDown(self):
        driver.quit()

    def test_word(self):
        """对不同小游戏类型，选择不同函数进行相应的操作"""
        # self.login_page.login()
        self.login_page.input_username('15555555555')
        self.login_page.input_password('123321')
        self.login_page.login_button()
        time.sleep(10)
        if self.home_page.wait_check_page() == "试卷":
            print("登录成功")
            # 进入首页后点击作业条目
        while True:
            var = self.homework.judge_homework_YB()

            if '词汇选择&单词拼写' in var[1] and '词汇选择&单词拼写' in var[3][0]:

                # self.homework_exist(var[1].index + 1, var[2], var[3])
                time.sleep(2)
                self.home_page.YB()
                self.word_spelling()
                break

            else:
                Swipe(driver).swipe_up(1000)
                time.sleep(2)
                self.home_page.YB()
                self.word_spelling()

                break

    def word_spelling(self):
        mode = self.homework.word_customize_YB()

        count = self.homework.word_count()
        print(len(count))

        for i in range(0, len(count)):
            var = self.homework.word_type(i).text
            print(var)  # 获取小游戏类型
            if var == ' 单词拼写 ' and mode == "自定义":


                self.word_page.word_bound_num(i)

                # time.sleep(1)x
                # self.two_homework.chick_question()
                time.sleep(1)
                max_num = self.word_page.max_number_YB()
                # 获取到我们需要的最大的题数
                for i in range(int(max_num)):
                    self.word_page.word_YB()
                    # self.word_page.word()
                    time.sleep(1)
                    self.word_page.arrow()
                    time.sleep(5)
                    # self.word_page.again_arrow()
                    # time.sleep(1)

                self.word_page.again_practice()
                time.sleep(1)
                self.word_page.return_btn()
                time.sleep(1)
                self.word_page.return_btn()
                time.sleep(2)

            break



    # def word(self):
    #     word = yb_letter(self.word_page.word_spelling_text())
    #     print("这个单词是",word)
    #     games_keyboard(self,word)



# if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Games('test_word'))

def num():
    suite = unittest.TestSuite()
    suite.addTest(Games('test_word'))
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