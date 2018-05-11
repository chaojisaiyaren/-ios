import random
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Word_book(object):

    """单词本的所有的页面元素属性"""
    def __init__(self,driver):
        self.driver = driver

    def click_word_book(self):
        """点击单词本，以xpath为例"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="单词本"]').click()

    def judgment_word_book(self):
        """判断是否进入到了单词单词本这页"""
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="已学单词总数 10"]').text
        m = re.findall("已学单词总数", element)

        return m[0]

    def click_rank(self):
        """点击排行榜"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="wordRanking"]').click()

    def show_word_number(self):
        """显示已经学习单词的数量"""

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[0].text

        return ele

    def judgment_page(self):

        """判断是否进入了排行榜页面"""
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="炫耀一下"]').text
        return ele

    def show_list(self):
        """显示的排行榜列表"""
        l = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            l.append(ele[i].text)
        print("排行榜显示的列表为",l)
        return  l

    def word_number(self):

        '''单词数量'''

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text

        return ele
    def nicname(self):
        '''学生id'''
        id = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text

        return id

    def rank(self):
        '''学生的名次'''
        rank = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        return rank

    def chick_show(self):
        '''点击炫耀一下'''
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="炫耀一下"]').click()

    def click_wc(self):
        """点击微信分享"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="WC"]').click()

    def click_correct(self):
        """点击确定"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="确定"]').click()

    def click_friends(self):
        '''点击朋友圈'''
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="FQ"]').click()
    def go_back(self):
        """点击返回"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

