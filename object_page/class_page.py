import re
import time

from conf.basepage import BasePage

class Class_page(BasePage):
    #初始化属性


    def class_page(self):
        # 点击班级进入班级的页面
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="班级"]').click()

    def class_name(self):
        # 点击进入班级列表
        self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].click()

    def back_btn(self):
        # 点击返回按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    def scoreboard(self):
        # 点击积分排行榜
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="积分排行榜"]').click()

    def star_rank(self):
        # 点击星星排行榜
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="星星排行榜"]').click()

    def class_work(self):
        # 点击本班作业
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="本班作业"]').click()

    def quit_class(self):
        # 点击退出班级
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="退出班级"]').click()

    def this_week(self):
        # 点击本周
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="本周"]').click()

    def before_week(self):
        # 点击上周
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="上周"]').click()

    def this_month(self):
        # 点击本月
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="本月"]').click()

    def all_rank(self):
        # 点击全部
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="全部"]').click()

    def undone(self):
        # 点击未完成
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="未完成"]').click()

    def done(self):
        # 点击已完成
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="已完成"]').click()

    def ranking(self):
        # 获取名次

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[4].text

        return ele

    def real_rank(self):
        #下面的那个排名
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text
        time.sleep(1)
        # print("内容是",ele)
        # 这里获取的是现在的排名
        #根据排名计算下面的排名，高亮排名和下面的排名是否一直
        num = 4 + int(ele) + (int(ele)) * 2
        # print('数字是',num)
        time.sleep(1)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[num].text
        time.sleep(1)
        return element

    def light_nicname(self):
        # 获取高亮的名字
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[5].text
        return ele

    def nicname(self):

        #下面的那个排名
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text
        time.sleep(1)
        # print("内容是",ele)
        # 这里获取的是现在的排名
        #根据排名计算下面的排名，高亮排名和下面的排名是否一直
        num = 4 + int(ele) + (int(ele)) * 2 + 1
        # print('数字是',num)
        time.sleep(1)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[num].text
        time.sleep(1)
        return element

    def all_ligtht_rank(self):
        # 获取高亮的名字
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[6].text
        return ele

    def all_real_rank(self):

        #下面的那个排名
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text
        time.sleep(1)
        # print("内容是",ele)
        # 这里获取的是现在的排名
        #根据排名计算下面的排名，高亮排名和下面的排名是否一直
        num = 4 + int(ele) + (int(ele)) * 2 + 2
        # print('数字是',num)
        time.sleep(1)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[num].text
        time.sleep(1)
        return element

    def add_class(self):
        # 添加班级
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="addClass"]').click()

    def apply_class(self,number):
        # 申请入班
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="申请加入班级"]').send_keys(number)

    def inquire_class(self):
        # 点击查询班级
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查询班级"]').click()
        time.sleep(1)

    def again_apply(self):
        # 点击查询班级之后的申请入班
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="申请入班"]').click()

    def apply_word(self):
        #点击那个输入框，然后写真实姓名
        time.sleep(2)
        word = self.driver.find_element_by_accessibility_id("请输入真实姓名")
        return  word

