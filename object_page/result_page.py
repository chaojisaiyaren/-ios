#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI
import random
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps

class ResultPage(BasePage):
    """结果页"""

    @teststep
    def wait_check_result_page(self):
        """以“title:排行榜”的ID为依据"""
        locator = (By.ID, "com.vanthink.student.debug:id/rank")
        element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        return element.text

    @teststep
    def rank_time(self):
        #完成时的时间
        item = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text
        return item

    @teststep
    def correct_rate(self):
        """准确率"""
        rate = self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[0].text
        num = re.search(r'\d+', rate)
        return num.group()


    @teststep
    def result_score(self):
        """结果页积分"""
        rate = self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[1].text
        num = re.search(r'\d+', rate)
        return num.group()

    @teststep
    def result_star(self):
        """星星"""
        rate = self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[2].text
        num = re.search(r'\d+', rate)
        return num.group()

    @teststep
    def result_time(self):
        """时间"""
        rate = self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[3].text
        pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b')  # 定义匹配模式
        num = re.findall(pattern, rate)
        # print(re.findall(pattern, rank)[0])
        return num[0]

    @teststep
    def rank_title(self):
        """title: 排行榜"""
        rank = self.driver.find_element_xpath('//XCUIElementTypeStaticText[@name="排行榜"]').text

        # print(re.findall(pattern, rank)[0])
        return rank

    @teststep
    def rank_menu(self):
        """排行榜下拉按钮"""
        self.driver\
            .find_element_by_id("android:id/text1").click()

    @teststep
    def rank_menu_item(self):
        """排行榜下拉菜单"""
        item = self.driver.find_elements_by_id("android:id/text1")
        return item

    # 以下为排行榜list内容
    @teststep
    def rank_index(self):
        """排名"""
        item = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return item

    @teststep
    def new_rank_index(self):
        """再次进入的新的排名"""
        item = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return item

    @teststep
    def rank_name(self):
        """学生昵称"""
        item = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2].text
        return item

    @teststep
    def new_rank_name(self):

        """再次进入的学生昵称"""
        item = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2].text
        return item

    @teststep
    def again_rate(self):
        """再次进入的正确率"""
        rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        num = re.search(r'\d+', rate)
        return num.group()

    @teststep
    def rank_accuracy_rate(self):
        """准确率最高的那次的正确率"""
        rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        num = re.search(r'\d+', rate)
        return num.group()

    @teststep
    def rank_spend_time(self):
        """准确率最高的那次 完成所用时间"""
        time = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text
        return time

    @teststep
    def again_time(self):
        """再次进入的时间"""
        time = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text
        return time

    @teststep
    def check_result_button(self):
        """查看答案按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/detail") \
            .click()

    @teststep
    def error_again_button(self):
        """错题再练按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/again") \
            .click()

    @teststep
    def again_button(self):
        """再练一边按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/again") \
            .click()

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton").click()

    @teststep
    def back_up(self):
        """从结果页返回到作业list"""
        j = 0
        while j < 2:
            self.back_up_button()  # 结果页 返回按钮
            j += 1

    @teststep
    def result_page_ranking(self, nickname, accuracy_rate):
        """结果页结果统计&排行榜,"""
        print('进入结果页', accuracy_rate)
        index = []
        optimal_rate = []  # 最优准确率
        optimal_time = []  # 最优准确率所用时间
        if self.wait_check_result_page():  # 结果页检查点
            # 本次结果统计——准确率、积分、星星、所用时间
            correct_rate = re.sub("\D", "", self.correct_rate())
            time = re.sub("\D", "", self.result_time())  # 不带格式的时间 xxxx
            if accuracy_rate == correct_rate:
                print('本次成绩- 准确率、所用时间：', correct_rate+'%', re.search(r"(\d{1,2}:\d{1,2})", self.result_time()).group(0))

            self.rank_menu()  # 结果页 排行榜下拉菜单
            item = self.rank_menu_item()
            for j in range(len(item)):
                print('j:', j)
                item[j].click()  # 结果页 切换不同班级排行榜

                rank_name = self.rank_name()  # 排行榜list条目比较
                rank_index = self.rank_index()
                for i in range(len(rank_name)):
                    rank_rate = re.sub("\D", "", self.rank_accuracy_rate()[i].text)
                    rank_time = re.sub("\D", "", self.rank_spend_time()[i+1].text)  # 排行榜不带格式的时间 xxxx
                    # i+1的原因是排行榜的时间与右上角本次所用时间resource—id相同
                    mat = re.search(r"(\d{1,2}:\d{1,2})", self.rank_spend_time()[i+1].text)  # 排行榜带格式的时间 xx:xx

                    if rank_name[i].text == nickname and len(rank_name) != 1:  # 排行榜不只有自己
                        print(correct_rate, rank_rate)
                        if correct_rate == rank_rate:  # 将本次成绩与排行榜中最优成绩作比较-相等
                            if time < rank_time:  # 成绩相等时 比较时间
                                print('本次用时较短 Congratulations')
                            elif time == rank_time:
                                print('本次准确率、所用时间与之前成绩持平  Fighting')
                            else:
                                print('本次用时较长 Fighting')
                        elif correct_rate < rank_rate:
                            print('本次成绩非最优 Fighting')
                        else:
                            print('排行榜逻辑有问题')
                        print('排行榜成绩 - 排名、昵称、准确率、所用时间：', rank_index[i].text, rank_name[i].text, rank_rate+'%', mat.group(0))
                    elif len(rank_name) == 1:  # 排行榜只有自己
                        print('排行榜成绩 - 昵称、准确率、所用时间：', rank_name[i].text, rank_rate+'%', mat.group(0))

                    index.append(rank_index[i].text)
                    optimal_rate.append(rank_rate)
                    optimal_time.append(rank_time)
                if j != len(item)-1:
                    self.rank_menu()  # 结果页 排行榜下拉菜单
        else:
            print('未进入结果页')
        self.back_up_button()
        print(index, optimal_rate, optimal_time)
        print('==================================================')

    @teststep
    def result_page_score(self, count):
        """结果页结果统计 -- 积分"""
        print('进入结果页')
        if self.wait_check_result_page():  # 结果页检查点
            # 本次结果统计——准确率、积分、星星、所用时间
            score = re.sub("\D", "", self.result_score())
            if int(score) == count:
                print("积分逻辑无误 -- 本次答对 %d题 积分：%d", count, int(score))
            else:
                print("积分逻辑有误 - 本次答对 %d题 但积分：%d", count, int(score))
