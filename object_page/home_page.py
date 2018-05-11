#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN FEIFEI
import time

from utils.screen_swipe import *
from conf.decorator import teststep, teststeps
from conf.basepage import BasePage


class HomePage(BasePage):


    @teststep
    def wait_check_page(self, timeout=10, poll_frequency=0.5):
        """以“试卷label”的xpath-index为依据"""
        time.sleep(2)
        element = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="试卷"]')[0].text
        time.sleep(3)
        return element

    @teststep
    def click_homework_label(self):
        """以“作业label”的xpath为依据"""
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="作业"])[1]').click()

    @teststep
    def click_testpaper_label(self):
        """以“试卷label”的xpath为依据"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="试卷"]').click()

    @teststep
    def click_tab_hw(self):
        """以“作业tab”的id为依据"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="作业"]').click()

    @teststep
    def click_test_class(self):
        """以“班级tab”的id为依据"""
        self.driver .find_element_by_xpath('//XCUIElementTypeButton[@name="班级"]').click()

    @teststep
    def click_tab_profile(self):
        """以“个人中心tab”的id为依据"""
        self.driver .find_element_by_xpath('//XCUIElementTypeButton[@name="我的"]').click()

    def click_tab_profile_text(self):
        """以“个人中心tab”的id为依据"""
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="我的"]').text

        return ele

    # def item_count(self):
        #以后实现的目标，循环点击

    #     # TODO item条数搜集
    @teststep
    def item_list(self):
        """以作业或者列表的xpath也就是type作为依据"""
        # self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="自动化测试1"]').click()
        """以作业或者列表的xpath也就是type作为依据（稍难列表里面的）"""
        # self.driver.find_elements_by_accessibility_id('XCUIElementTypeCell')[1].click()
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="稍难"]').click()

    @teststep
    def list_eazy(self):
        """以作业或者列表的xpath也就是type作为依据（稍简单列表里面的）"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="稍简单"]').click()

    @teststep
    def setting_two(self):
        "进入设置YB字体2"
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB字体2"]').click()

    @teststep
    def setting_one(self):
        "进入设置YB字体2"
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB字体1"]').click()

    @teststep
    def test_reconstruction_one(self):
        """测试重构1"""
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="测试重构1"])[1]').click()

    @teststep
    def test_reconstruction_two(self):
        """测试重构2"""
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="测试重构2"])[1]').click()

    @teststep
    def test_reconstruction_three(self):
        """测试重构3"""
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="测试重构3"])[1]').click()


    @teststep
    def test_reconstruction_four(self):
        """测试重构4"""
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="测试重构4"])[1]').click()

    @teststep
    def YB(self):
        "进入单词&词汇选择选择条框"
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="词汇选择&单词拼写"]').click()

    @teststep
    def test5(self):
        """以作业或者列表的xpath也就是type作为依据（稍简单列表里面的）"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="test5"]').click()

    @teststep
    def test3(self):
        """以作业或者列表的xpath也就是type作为依据（稍简单列表里面的）"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="test3"]').click()

    @teststep
    def test6(self):
        # self.driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()

        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="test6"]').click()

    @teststep
    def homework(self):

        """以“作业或者试卷列表内条目”的id为依据"""
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
        return ele

    @teststep
    def test2(self):
        """以作业或者列表的xpath也就是type作为依据（稍简单列表里面的）"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="test2"]').click()

    @teststep
    def restore_words(self):
        """以还原单词的xpath作为依据"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="单个还原单词自动化数据"]').click()

    @teststep
    def guess_word(self):
        "YB字体猜词游戏的练习，以xapth为依据"
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="猜词游戏"]').click()

    @teststep
    def judge_homework_exist(self):
        """判断要进行操作的作业是否存在"""
        homework_title = []
        homework_list = HomePage().homework()
        for index1 in range(0, len(homework_list)):
            homework_title.append(homework_list[index1].text)  # 获取作业title列表
        print('homework_title:', homework_title)

        item = homework_title[len(homework_title) - 1]  # 最后一个作业的title
        print('item:', item)

        tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
        print('tips:', tips)

        return tips, item, homework_title, homework_list

    @teststep
    def homework_count(self):
        """获取作业title列表第一个页面的作业 """
        homework_title = []
        homework_list = HomePage().homework()
        for index1 in range(0, len(homework_list)):
            homework_title.append(homework_list[index1].text)  # 获取作业title列表

        return homework_title, homework_list

    @teststep
    def homework_count_2(self):
        """获取作业title列表非第一页的作业 及 页面内最后一个作业的title 以及 元素 '到底啦 下拉刷新试试' """
        homework_title = []
        homework_list = HomePage().homework()
        for index1 in range(0, len(homework_list)):
            homework_title.append(homework_list[index1].text)  # 获取作业title列表

        item_1 = homework_list[len(homework_list) - 1]  # 最后一个作业的title
        tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
        print('tips:', tips)

        return tips, item_1, homework_title, homework_list

    @teststep
    def text(self, index1):
        """元素：到底啦 下拉刷试试"""
        try:
            item = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="到底啦，下拉刷新试试"])[1]')
            if item.text == '到底啦，下拉刷新试试':
                return True
            else:
                return False
        except:  # 元素没有，会报错.如果元素存在则说明也不会发生
            pass


    #这个兽点金item_list之后的二级页面
    #todo:这些应该根据元素的判断进行自动判断还有点击

class Tow_homepage(BasePage):
    #作业的二级页面

    @teststep
    def cloze(self):
        #这个是完形填空
        Swipe().swipe_up(1000)
        time.sleep(3)
        # Swipe(self.driver).swipe_down(1000)
        # time.sleep(3)


        self.driver.find_elements_by_xpath('(//XCUIElementTypeStaticText[@name="兼职测试题"])')[5].click()
