#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN SASUKE
import re
import time
from conf.basepage import BasePage
from utils.click_bounds import games_keyboard
#二级页面
from conf.decorator import teststep, teststeps
class Words_end(BasePage):

    #以选词填空的内容作为一个判断是否进入里的一个标准
    #用xpath来作为依据
    @teststeps
    def wait_page(self):
        ele = self.driver.find_element_by_accessibility_id('选词填空').text
        return ele

    @teststeps
    def chick_class(self):
        #点击班级可以显示信息，以xpath作为依据
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="自动化测试班级"]').click()

    @teststeps
    def check_answer(self):
        #点击查看答案可以跳转到答案的详情页面，以xpath为依据
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststeps

    def correct_reply(self):
        # 这个是正确的答案
        l = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')
        for i in range (len(ele)):
            l.append(ele[i].text)

        l = ['one(ssda)', 'two(ssda)', 'Three on(ssda)', 'Four(ssda)', 'Five(ssda)']
        q1 = l[0].lower()
        q2 = [q1[0:-8], q1[1:-7], q1[2:-6]]
        w1 = l[1].lower()
        w2 = [w1[0:-8], w1[1:-7], w1[2:-6]]
        e1 = l[2].lower()
        e2 = [e1[0:-13], e1[1:-12], e1[2:-11], e1[3:-10], e1[4:-9], e1[6:7], e1[7:8]]
        r1 = l[3].lower()
        r2 = [r1[0:1], r1[1:2], r1[2:3], r1[3:4]]
        t1 = l[4].lower()
        t2 = [t1[0:1], t1[1:2], t1[2:3], t1[3:4]]
        p = [q2, w2, e2, r2, t2]
        for j in range(len(p)):
            games_keyboard(self,p[j])


    @teststeps
    def reerror(self):
        #点击错题再练可以跳转到我们之前做过的游戏，以xpath为依据
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststeps
    def back_btn(self):
        #点击错题再练可以返回上一页的内容，以xopath作为依据
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststeps
    def back_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()


class Single_end(BasePage):

    @teststep
    def back_btn(self):
        #进行元素的一个返回的操作
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def check_answer(self):
        #
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
        time.sleep(2)

    @teststep
    def again_hard(self):
        #点击再练一边这个按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def again_wrong(self):
        #点击错题再练这个按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def again_exercise(self):
        # 点击错题再练这个按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()




