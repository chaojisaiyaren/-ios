#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN SASUKE
import re
import time
import random
from utils.click_bounds import click_bounds
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.click_bounds import games_keyboard,click_bounds,guess_keyboard
from utils.screen_swipe import Swipe
from app.student.homework.object_page.home_page import HomePage
from utils.yb_data import yb_operate
from utils.yb_data import yb_letter,yb_letter_write,yb_operate,yb_guess,yb_letter_select
from conf.basepage import BasePage
from random import choice
from conf.decorator import teststep, teststeps
from utils.vob_data import reconstruction_guess,vob_operate,reconstruction_write,reconstruction_self


class Homework(BasePage):
    """作业页面 元素信息"""

    @teststep
    def homework_count(self):
        """作业类型条目"""
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 选词填空 "]')
        return ele

    @teststep
    def click_homework(self,index):
        #点击作业
        self.driver.find_elements_by_class_name("XCUIElementTypeCell")[index+1].click()

    @teststep
    def sengle_count(self):
        #单项选择的进入条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单项选择 "]')
        return ele

    @teststep
    def tv_testbank_type(self,index):
        """作业的类型 这里用的是xpath"""
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 选词填空 "]')[index]

        # item = self.driver.find_element_by_accessibility_id('选词填空').text



        return item

    @teststep
    def cloze_count(self):
        #完形填空的进入条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 完形填空 "]')
        print("完形填空",ele)
        return ele

    @teststep
    def single_type(self,index):
        #单项选择的作用的类型
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单项选择 "]')[index]

        # item = self.driver.find_element_by_accessibility_id('选词填空').text

        return item

    @teststep
    def cloze_type(self,index):
        #完形填空的作用的类型
        Swipe().swipe_up(1000)
        time.sleep(3)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 完形填空 "]')[index]

        # item = self.driver.find_element_by_accessibility_id('选词填空').text

        return item

    @teststep
    def read_count(self):
        #阅读理解的进入条件
        Swipe().swipe_up(1000)
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 阅读理解 "]')
        print("阅读理解",ele)
        return ele

    @teststep
    def read_type(self,index):
        #完形填空的作用的类型

        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 阅读理解 "]')[index]

        # item = self.driver.find_element_by_accessibility_id('选词填空').text

        return item

    @teststep
    def listen_practice_count(self):
        #听力练习的进入条件

        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 听力练习 "]')
        print("听力练习",ele)
        return ele

    @teststep
    def listen_practice_type(self,index):
        #完形填空的作用的类型

        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 听力练习 "]')[index]

        # item = self.driver.find_element_by_accessibility_id('选词填空').text

        return item

    @teststep
    def art_type(self,index):
        #补全文章的作用类型
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 补全文章 "]')[index]

        return item

    @teststep
    def art_count(self):
        #阅读理解的进入条件

        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 补全文章 "]')
        print("补全文章",ele)
        return ele

    @teststep
    def vob_count(self):
        #进入词汇选择的条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')
        print("词汇选择",ele)
        return ele

    @teststep
    def vob_count_explanatio (self):
        #进入词汇选择的条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')
        print("词汇选择",ele)
        return ele

    @teststep
    def vob_type(self,index):
        #词汇的作用类型
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')[index]

        return item

    @teststep
    def vob_type_YB(self):
        #词汇的作用类型YB(选单词)
        item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（选单词）"]')

        return item

    @teststep
    def listen_count(self):
        #进入单词听写的条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词听写 "]')
        print("单词听写",ele)
        return ele

    @teststep
    def listen_type(self,index):
        #单词听写的作用类型
        time.sleep(2)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词听写 "]')[index]

        return item

    @teststep
    def flash_count(self):
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('(//XCUIElementTypeButton[@name=" 闪卡练习 "])[1]')
        print("闪卡练习",ele)
        return ele

    @teststep
    def flash_type(self,index):
        #单词听写的作用类型
        item = self.driver.find_elements_by_xpath('(//XCUIElementTypeButton[@name=" 闪卡练习 "])[1]')[index]

        return item

    @teststep
    def copy_count(self):
        #闪卡练习，抄写模式
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 闪卡练习 "]')
        print("闪卡练习",ele)
        return ele

    @teststep
    def copy_type(self,index):
        #单词听写的作用类型
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 闪卡练习 "]')[index]

        return item

    @teststep
    def copy_type_study(self):
        #抄写模式这个学习的类型
        item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="马承同步三上 lesson2 闪卡练习（抄写模式）（引用1）"]')
        return item

    @teststep
    def flash_type_study(self):
        item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="中考精华词汇 基础版65（学习模式）"]')
        return item

    @teststep
    def word_type(self,index):
        #单词拼写的作用类型
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词拼写 "]')[index]

        return item

    @teststep
    def word_type_word(self):

        #单词拼写的作用类型默写模式
        word = []
        item = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(item)):
            word.append(item[i].text)
        print("列表是",word)



        return item

    @teststep
    def word_type_random(self):

        #单词拼写的作用类型默写模式
        item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（随机模式）"]')

        return item

    @teststep
    def word_customize_YB(self):

        #   这个是单词拼写YB下自定义的条框的判断
        time.sleep(3)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（自定义）"]').text
        m = re.findall('自定义', ele)
        print("打印出来的是什么",m[0])
        return m[0]

    @teststep
    def word_write_YB(self):

        #   这个是单词拼写YB下自定义的默写的判断
        time.sleep(3)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（默写模式）"]').text
        m = re.findall('默写模式', ele)
        print("打印出来的是什么", m[0])
        return m[0]

    @teststep
    def word_random_YB(self):

        #   这个是单词拼写YB下自定义的默写的判断
        time.sleep(3)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（随机模式）"]').text
        m = re.findall('随机模式', ele)
        print("打印出来的是什么", m[0])
        return m[0]

    @teststep
    def word_vob_YB(self):

        #这个是词汇选择YB下的选单词的判断
        time.sleep(3)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（选单词）"]').text
        m = re.findall('选单词', ele)
        print("打印出来的是什么", m[0])
        return m[0]

    @teststep
    def word_count(self):
        #进入单词听写的条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词拼写 "]')
        print("单词拼写",ele)
        return ele

    @teststep
    def strengthen_count(self):
        # 进入单词听写的条件
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 强化炼句 "]')
        print("强化炼句", ele)
        return ele

    @teststep
    def strengthen_type(self,index):
        # 进入单词听写的条件
        time.sleep(2)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 强化炼句 "]')[index]

        return item

    @teststep
    def guess_count(self):
        # 进入猜词游戏的条件
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 猜词游戏 "]')
        print("猜词游戏", ele)
        return ele

    @teststep
    def guess_type(self,index):
        # 进入单词听写的条件
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 猜词游戏 "]')[index]

        return item

    @teststep
    def restore_count(self):
        # 进入还原单词的条件
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 还原单词 "]')
        print("还原单词", ele)
        return ele

    @teststep
    def restore_type(self,index):
        # 进还原单词的条件
        time.sleep(2)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 还原单词 "]')[index]

        return item

    @teststep
    def conjunctions_count(self):
        # 进入还原单词的条件
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连词成句 "]')
        print("连词成句", ele)
        return ele

    @teststep
    def conjunctions_type(self,index):
        # 进入还原单词的条件
        time.sleep(2)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连词成句 "]')[index]

        return item

    @teststep
    def sentence_count(self):
        # 进入句型转换的条件
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 句型转换 "]')
        print("句型转换", ele)
        return ele

    @teststep
    def sentence_type(self,index):
        # 进还原单词的条件
        time.sleep(2)
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 句型转换 "]')[index]

        return item

    @teststep
    def match_count(self):
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连连看 "]')
        print("连连看", ele)
        return ele

    @teststep
    def match_type(self,index):
        # 进入连连看的条件
        item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连连看 "]')[index]

        return item

    @teststep
    def tv_testbank_name(self,index):
        """作业的模式 这里用的xpath"""
        item = self.driver.find_elements_by_class_name('/XCUIElementTypeStaticText')[index].text
        m = re.match(".*\（(.*)\）.*", item)
        print(m.group(1))
        return m.group(1)

    # def click_homework(self):
    #     """点击作业条目 这里用的还是xpath"""
    #     # TODO 作业item点击
    #     self.driver.find_elements_by_xpath('(//XCUIElementTypeStaticText[@name="兼职测试题"])')[1].click()
    @teststep
    def judge_homework_exist(self):
        """判断要进行操作的作业是否存在"""
        homework_title = []
        homework_list = HomePage().homework()
        #我们得到的列表里面从下标为1开始，每三个才是它的坐标，所有我们这样做的为了过滤一下
        for index1 in range(1, len(homework_list),3):
            homework_title.append(homework_list[index1].text)  # 获取作业title列表

        print('homework_title:', homework_title,len(homework_title))

        item = homework_title[len(homework_title) - 1]  # 最后一个作业的title
        print('item:', item)

        # tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
        # print('tips:', tips)
        n = 6

        work_list = [homework_title[i:i + n] for i in range(0, len(homework_title), n)]

        return  item, homework_title, homework_list,work_list

    @teststep
    def judge_homework_YB(self):
        """判断要进行操作的作业是否存在"""
        homework_title = []
        homework_list = HomePage().homework()
        #我们得到的列表里面从下标为1开始，每三个才是它的坐标，所有我们这样做的为了过滤一下
        for index1 in range(1, len(homework_list),3):
            homework_title.append(homework_list[index1].text)  # 获取作业title列表

        print('homework_title:', homework_title,len(homework_title))

        item = homework_title[len(homework_title) - 1]  # 最后一个作业的title
        print('item:', item)

        # tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
        # print('tips:', tips)
        n = 6

        work_list = [homework_title[i:i + n] for i in range(0, len(homework_title), n)]

        return  item, homework_title, homework_list,work_list

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

    @teststep
    def games_count(self):
        """小游戏数目 """
        item = self.driver.find_elements_by_id("XCUIElementTypeButton")
        return item

class Choice_words(BasePage):
    """选词填空"""

    @teststep
    def wait_choice(self):
        #根据元素的"classname"来进行元素的提取
        time.sleep(2)
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="选词填空"]').text
        return ele

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element
    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("现在做题的时间是：",ele)
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("现在做题的时间是：",ele)
    @teststep
    def chose_blank(self,index):
        #这个是依次点击五个按钮
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[index]
        return ele

    @teststep
    def click_bounds_num(self,index):
        obj = Homework().tv_testbank_type(index)
        bounds = obj.location
        # print(bounds)
        # x = obj.get_attribute("x")
        # print(x)
        # y = obj.get_attribute("y")
        # print(y)
        x = bounds['x']
        y = bounds['y']
        # width = size['width']
        # height = size['height']

        loc_x = x + 100
        loc_y = y

        click_bounds(self, loc_x, loc_y)
        # click_bounds(self,int(x)+100,int(y))
        # ele = self.driver.find_element_by_accessibility_id("x").text
        # print(ele)
        # time.sleep(2)
    @teststep
    def small_font(self):
        # 点击普通的小字体
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
        print("点击了缩小的Aa的图标。英文字体变得小了")
    def ordinary_front(self):
        # 点击普通的字体
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
        print("点击了普通大小的的Aa的图标。英文字体发生了改变了")
    def big_front(self):
        # 点击大字体
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
        print("点击了放大的Aa的图标。英文字体扩大了了")
    @teststep
    def arrow(self):
        #这个是那个arrow的箭头，用xpath来选取元素
        # 再次点击按钮（两次按钮的元素是不一样的）
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def back_btn(self):
        #返回按钮用xpath进行定位
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def tip_words(self):
        #还是以这个提示词的xpath选取元素的
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="提示词"]').click()

    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["s","s","d","a"]
        word = list(ele)
        for i in range(len(word)):

            games_keyboard(self, word[i])
            print("依次填写的单词字母是:",word[i])
class Single_choice(BasePage):
    """单项选择练习"""

    @teststep
    def wait_page(self,timeout=10, poll_frequency=0.5):
        #以这个页面的xpath作为依据,证明已经进入了这个页面
        element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="单项选择"]').text
        # element = self.driver.find_element_by_accessibility_id('单项选择').text
        time.sleep(3)
        return element

    @teststep
    def back_btn(self):
        """返回按钮以xpath作为元素"""
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def light_btn_text(self):
        """前进的那个按钮"""
        element = self.driver.find_element_by_accessibility_id('doneItem').text
        return element

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return rate

    # 下一步按钮
    @teststep
    def light_btn(self):
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')[1]
        return ele

    #灰色的按钮，获取里面的元素
    @teststep
    def gary_btn_text(self):
        element = self.driver.find_element_by_accessibility_id('doneItemNo').text
        return element
    #灰色按钮
    def gray_btn(self):
        self.driver.find_element_by_accessibility_id('doneItemNo').click()
    #点击那个完形填空的字是不能进入后面的界面的，所以我们向右多移动了100px的距离，然后就可以点带那个大的框了
    @teststep
    def single_bound_num(self,index):
        obj = Homework().single_type(index)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        # width = size['width']
        # height = size['height']

        loc_x = x + 100
        loc_y = y

        click_bounds(self, loc_x, loc_y)
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def grey_btn(self):
     """灰色按钮是不可点击的状态"""
     time.sleep(1)
     ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
     if ele == "doneItemNo":
         print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)
    @teststep
    def single_bound_num_rank(self, index):
        #点击排行榜
        obj = Homework().single_type(index)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        # width = size['width']
        # height = size['height']

        loc_x = x + 340
        loc_y = y
        print("点击的位置",loc_x,loc_y)

        click_bounds(self, loc_x, loc_y)


    @teststep
    def correct_reply(self):
        # 点击正确的回答
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="这个是答案"]').click()

    @teststep

    def correct_reply(self):
        # 点击正确的回答
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="这个是答案"]').click()



    def choice_A(self):
        #选择A选项
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="A"]').click()

    @teststep
    def option_button(self):
        """获取四个选项"""
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")

        return ele

    @teststep
    def option_button_YB(self):
        """获取四个选项"""
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        YB = ele[0:3]
        print("我们要点击的单词",YB)

        return YB

    @teststep
    def single_option(self):
        # 得到我们正确答案的列表的下表盘
        single_list = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range (len(ele)):
            single_list.append(ele[i].text)
        print(single_list)

        index = [i for i, x in enumerate(single_list) if x == self.option_button_YB()][0]
        print("选项的索引",index)
        return index

    def option_YB(self):

        self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[int(self.single_option()-1)].click()











    def wait_process(self):
        #待完成这个文字
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="待完成："]').text
        return element

class Cloze(BasePage):
    #完形选择\
    #初始化__init__函数

    @teststep
    def wait_cloze(self):
        #以完形填空的xpath为依据，然后用里面的text进行判断，是否进入到这一页
        element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="完形填空"]').text
        return element

    @teststep
    def back_btn(self):
        #左上角的返回按钮，以xpath作为依据
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
    @teststep
    def small_font(self):
        # 点击普通的小字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
        print("点击了缩小的Aa的图标。英文字体变得小了")
    def ordinary_front(self):
        # 点击普通的字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
        print("点击了普通大小的的Aa的图标。英文字体发生了改变了")
    def big_front(self):
        # 点击大字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
        print("点击了放大的Aa的图标。英文字体扩大了了")
    @teststep
    def cloze_num(self):
        # 拿到我们需要做的题的个数
        rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return rate
    @teststep
    def grey_btn(self):
     """灰色按钮是不可点击的状态"""
     time.sleep(1)
     ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
     if ele == "doneItemNo":
         print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)

    @teststep
    def cloze_correct(self):
        # 正确的答案
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[3]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[4]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[5]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[6]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[7]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[8]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[9]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[10]').click()
        time.sleep(2)

    @teststep
    def cloze_option_button(self,i):
        """获取四个选项"""
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
        # print("答案的列表",len(ele))

        return ele

    @teststep
    #点击我们完形填空的空白的地方
    def cloze_bound_num(self, index):
        obj = Homework().cloze_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)
    #这个是我们的箭头的按键
    @teststep
    def cloze_arrow(self):
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("填写全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    #点击错题再练
    @teststep
    def wrong_problem(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def again_problem(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

    #点击查看答案'
    @teststep
    def check_answer(self):
        time.sleep(2)

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)

class ReadingComprehension(BasePage):

    @teststep
    def wait_read(self):
        # 以阅读理解的xpath为依据，然后用里面的text进行判断，是否进入到这一页
        element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="阅读理解"]').text
        return element

    @teststep
    def back_btn(self):
        #左上角的返回按钮，以xpath作为依据
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def read_num(self):
        # 拿到我们需要做的题的个数
        element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return element
    @teststep
    def grey_btn(self):
     """灰色按钮是不可点击的状态"""
     time.sleep(1)
     ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
     if ele == "doneItemNo":
         print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)
    @teststep
    def read_bound_num(self, index):
        obj = Homework().read_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def read_option_button(self,i):
        """获取四个选项"""
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
        # print("答案的列表",len(ele))

        return ele
    #这个是我们的箭头的按键
    @teststep
    def read_arrow(self):
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("填写全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def click_answer(self):
        # 点击答案
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[3]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[4]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[5]').click()
        time.sleep(2)

    #点击再练一边
    @teststep
    def practice_again(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()
        time.sleep(3)
    @teststep
    def small_font(self):
        # 点击普通的小字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
        print("点击了缩小的Aa的图标。英文字体变得小了")
    def ordinary_front(self):
        # 点击普通的字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
        print("点击了普通大小的的Aa的图标。英文字体发生了改变了")
    def big_front(self):
        # 点击大字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
        print("点击了放大的Aa的图标。英文字体扩大了了")
    #点击查看答案'
    @teststep
    def check_answer(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

class Complement_article(BasePage):
    #补全文章的作业

    @teststep
    def wait_art(self):
        # 以补全文章的xpath为依据，然后用里面的text进行判断，是否进入到这一页
        element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="补全文章"]').text
        return element

    @teststep
    def back_btn(self):
        #左上角的返回按钮，以xpath作为依据
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def art_num(self):
        # 拿到我们需要做的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        return element

    @teststep
    def art_bound_num(self, index):
        obj = Homework().art_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)
    def comp_num(self):
        # 拿到我们需要做的题的个数
        element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return element
    @teststep
    def read_option_button(self,i):
        """获取四个选项"""
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
        # print("答案的列表",len(ele))

        return ele
    #这个是我们的箭头的按键

    @teststep
    def again_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    #点击再练一边
    time.sleep(2)

    @teststep
    def wrong_again(self):
        time,slice(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()
        time.sleep(2)
    #点击查看答案'
    @teststep
    def check_answer(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
    @teststep
    def grey_btn(self):
     """灰色按钮是不可点击的状态"""
     time.sleep(1)
     ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
     if ele == "doneItemNo":
         print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)
    #点击补全文章的选择
    @teststep
    def art_A(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="A"]').click()

    @teststep
    def art_B(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="B"]').click()

    @teststep
    def art_C(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="C"]').click()

    @teststep
    def art_D(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="D"]').click()

    @teststep
    def art_E(self):
        time.sleep(1)
        Swipe().swipe_up_bottom(1000)
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="E"]').click()

    @teststep
    def small_font(self):
        # 点击普通的小字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
        print("点击了缩小的Aa的图标。英文字体变得小了")
    def ordinary_front(self):
        # 点击普通的字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
        print("点击了普通大小的的Aa的图标。英文字体发生了改变了")
    def big_front(self):
        # 点击大字体
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
        print("点击了放大的Aa的图标。英文字体扩大了了")
class Vobcabulary(BasePage):
    """词汇选择"""

    @teststep
    #我们点击的词汇选择的框
    def vob_bound_num(self, index):
        obj = Homework().vob_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)

    @teststep
    def vob_reconstrction(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选解释）"]').click()
    @teststep

    def vob_word(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选单词）"]').click()

    @teststep
    def vob_bound_num_YB(self):
        obj = Homework().vob_type_YB()
        print(obj)
        bounds = obj.location


        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置", loc_x, loc_y)
        click_bounds(self, loc_x, loc_y)




        time.sleep(2)

    @teststep
    def vob_voice(self):
        #点击喇叭让应用读音
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="audio wq"]').click()

    @teststep
    def vob_option_button(self):
        """获取四个选项"""
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeCell")

        return ele

    @teststep
    def vob_option_reconstruction(self):
        """获取四个选项"""
        time.sleep(5)
        vob = []
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
        for i in range (len(ele)):
            vob.append(ele[i].text)
        print("这个列表是",vob)
        return vob

    @teststep
    def options(self):
        """获取四个选项"""
        # word = []
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        # for i in range(len(ele)):
        #     word.append(ele[i].text)
        # print("需要填写的单词是",word)
        return ele

    @teststep
    def option(self):
        """获取四个选项"""
        word = []
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("需要填写的单词是",word)
        return word

    @teststep
    def options_word(self,index):
        #点击选项
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[index]

        return ele
    @teststep
    def options_word_ex(self,index):
        # 选项的解释
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[index].text

        return ele

    @teststep
    def  word(self):
        #获取的单词
        # word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text
        # for i in range(len(ele)):
        #     word.append(ele[i].text)
        # print("列表里面的单词是",word)
        return  ele

    @teststep
    def vob_explanation(self):
        #进入词汇选择选解释的条件
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="剑桥3级词汇小测8月22日（选解释）"]').text
        m = re.match(".*\（(.*)\）.*", element)
        return m.group(1)

    @teststep
    def vob_explanation_reconstruction(self):
        #进入词汇选择选解释的条件
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选解释）"]').text
        m = re.match(".*\（(.*)\）.*", element)
        return m.group(1)
    @teststep
    def vob_explanation_word(self):
        #进入词汇选择选解释的条件
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选单词）"]').text
        m = re.match(".*\（(.*)\）.*", element)
        return m.group(1)

    @teststep
    def vob_listen(self):
        #进入听音选词的条件
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="外研版第一单元单词听写（听音选词）"]').text
        m = re.match(".*\（(.*)\）.*", element)
        return m.group(1)

    @teststep
    def vob_num(self):
        # 拿到我们需要做的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
        return element

    @teststep
    def vob_num_YB(self):
        # 拿到我们需要做的题的个数
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        return element

    @teststep
    def vob_num_word_YB(self):
        # 拿到我们需要做的题的个数
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        return element

    @teststep
    def vob_explantion_num(self):
        #词汇选择看词选解释的最大的题目数量
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="12"]').text
        return element

    @teststep
    def vob_explantion_num_reconstruction(self):
        #词汇选择看词选解释的最大的题目数量
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        return element

    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有选择单词灰色的按钮是不可点击的，灰色按钮的name属性是%s"%ele)
        return ele
    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)

    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("结束做题的时间是：",ele)
    @teststep
    def vob_listen_num(self):
        #词汇选择听音、选解释的最大的题目数量
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
        return element

    @teststep
    def light_btn(self):
        #前进的那个按钮
        # time.sleep(2)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("选择选项之后之后按钮是可以点击的，可以点击的，那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def clcik_voice(self):
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
        print("点击喇叭，但是发生准确与否还不能判断")
    @teststep
    def return_btn(self):
        #点击返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def wrong_problem(self):
        #点击错题再练
        time.sleep(2)
        print("点击错题再练说明出现错题再练的标志")
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()


    @teststep
    def again_problem(self):
        # 点击错题再练
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()
    # 结果页的方法与逻辑
    @teststep
    def show_page(self):
        time.sleep(2)
        ele = []
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(element)):
            ele.append(element[i].text)
        print('元素的text属性',ele)
        return ele
    @teststep
    def correct_rate(self):
        """准确率"""
        time.sleep(2)
        rate = self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[0].text
        time.sleep(2)
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
    def rank_accuracy_rate(self):
        """准确率最高的那次的正确率"""
        rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2].text
        num = re.search(r'\d+', rate)
        return num.group()
    @teststep
    def rank_spend_time(self):
        """准确率最高的那次 完成所用时间"""
        time = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b')  # 定义匹配模式
        num = re.findall(pattern, time)
        # print(re.findall(pattern, rank)[0])
        return num[0]

    @teststep
    # 结果页的方法与逻辑
    def end_page(self):
        time.sleep(2)
        rank_now = self.correct_rate()  # 学生这次做完题的准确率
        rank_integral = self.result_score()  # 学生这次做完题的积分
        rank_start = self.result_star()  # 学生的星星
        rank_time = self.result_time()  # 学生做完答题所用的时间
        best_score = self.rank_accuracy_rate()
        work_time = self.rank_spend_time()
        # 01:08
        rank_now_time = int(rank_time[0:1]) * 3600 + int(rank_time[1:2]) * 60 + int(rank_time[3:4]) * 10 + int(rank_time[4:5])
        rank_best_time = int(work_time[0:1]) *  3600 + int(work_time[1:2]) * 60 + int(work_time[3:4]) * 10 + int(work_time[4:5])
        print("打印出来的一些列元素", rank_now, rank_integral, rank_start, rank_time, best_score, work_time)
        print("此时学生做题的准确率：%s，积分:%s,星星：%s，时间:%s" % (rank_now, rank_integral, rank_start, rank_time))
        if int(rank_now) >= int(best_score) and rank_now_time >= rank_best_time:
            print("您的答题正确率得到了提高，但是答题的效率稍微低了一点，您的答题正确率为%d,答题的时间为%d" % (int(rank_now), rank_now_time))

        elif int(rank_now) >= int(best_score) and rank_now_time < rank_best_time:
            print("Congratulations您的正确率和答题时间超越了你的最高水平，当前你的最高正确率是%d,您的最佳答题时间为%d" % (int(rank_now), rank_now_time))

        elif int(rank_now) >= int(best_score) and rank_now_time >= rank_best_time:
            print("您的答题正确率得到了提高，但是答题的效率稍微低了一点，您的答题正确率为%d,答题的时间为%d" % (int(rank_now), rank_now_time))
        else:
            print("您的答题时间和正确率都没有提高。。请再接再厉，您当前答题的正确率为%d，答题的时间为%d秒" % (int(rank_now), rank_now_time))
        time.sleep(2)
        return rank_now,rank_integral,rank_start,rank_now_time
class Dictation(BasePage):
    """单词听写"""

    @teststep
    #我们点击单词听写的框
    def listen_bound_num(self, index):
        obj = Homework().listen_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("做完题的时间是：",ele)
    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s"%ele)
        return ele
    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["s","s","d","a"]
        word = list(ele)
        for i in range(len(word)):
            games_keyboard(self, word[i])
            print("我们输入的字母是:",word[i])

    @teststep
    def arrow(self):
        #点金前进的那个箭头
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def again_arrow(self):
        #还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s"%ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()
    # 点击喇叭
    @teststep
    def clcik_voice(self):
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
        print("点击喇叭，但是发生准确与否还不能判断")
    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def return_btn(self):
        #点击返回
        time.sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)

    @teststep
    def wrong_problem(self):
        #点击错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

class Word_spelling(BasePage):
    """单词拼写"""

    #我们点击的单词拼写的框
    @teststep
    def word_bound_num(self, index):
        obj = Homework().word_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def word_bound_write(self):
        #点击单词拼写的默写模式
        obj = Homework().word_type_word()
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def word_write_xpath(self):

        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（默写模式）"]').click()
    @teststep
    def word_write(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（默写模式）"]').click()

    @teststep
    def word_write_random(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（随机模式）"]').click()

    @teststep
    def word_bound_random(self):
        #点击单词拼写的随机模式
        obj = Homework().word_type_random()
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)



    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s"%ele)
        return ele

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def max_number_YB(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        time.sleep(2)
        return element

    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["s","s","d","a"]
        word = list(ele)
        for i in range(len(word)):
            games_keyboard(self, word[i])
            print("我们输入的单词是",word[i])

    @teststep
    def explanation(self):
        """单词的中文的翻译"""


        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[4].text


        return ele
    @teststep
    def exp(self):
        """单词的中文的翻译"""


        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text


        return ele

    @teststep
    def word_text(self):
        # 写的是正确的拼写的单词
        # 取到这个正确的单词
        self.lower()
        value = reconstruction_write(self.explanation())
        print("我们需要填写的单词是",value)
        for i in range (len(value)):
            games_keyboard(self,value[i])
            str = "".join(self.show_all_text())
            if value == str:
                print("开启大写字母之后点击的字母和显示的字母相同，所以测试结果正确")

    @teststep
    def show_text(self):
        # 这页的所有的name内容
        # list = []
        ele =  self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[-1].text
        # for i in range(len(ele)):
        #     list.append(ele[i].text)
        # print("这页的所有的列表",list)
        # return list
        print("我们页面显示的单词是",ele)
        return ele
    @teststep
    def show_all_text(self):
        # 这页的所有的name内容
        time.sleep(2)
        list = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')
        for i in range(len(ele)):
            list.append(ele[i].text)
        print("这页的所有的列表",list)
        return list


    @teststep
    def word_self(self):
        # 写的是正确的拼写的单词
        # 取到这个正确的单词
        self.lower()
        value = reconstruction_self(self.exp())
        print("我们需要填写的单词是",value)
        for i in range (len(value)):
            games_keyboard(self,value[i])
            if value == self.show_text():
                print("开启大写字母之后点击的字母和显示的字母相同，所以测试结果正确")


    @teststep
    def lower(self):
        # 点击开启大写字母的按键。
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="c chaKeyboardShiftButton"]').click()
        # text = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="c chaKeyboardShiftButton"]').text
        print("点击了大写的字母")



    @teststep
    def determination(self):
        """用于判定是否是空白"""

        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
        print("这个元素是%s,所以这个元素上的横线是空的"%(ele))

        return ele

    # !/usr/bin/env python
    # encoding:UTF-8
    # @Author  : SUN SASUKE
    import re
    import time

    from utils.click_bounds import click_bounds
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from utils.click_bounds import games_keyboard, click_bounds, guess_keyboard
    from utils.screen_swipe import Swipe
    from app.student.homework.object_page.home_page import HomePage
    from utils.yb_data import yb_operate
    from utils.yb_data import yb_letter, yb_letter_write, yb_operate, yb_guess, yb_letter_select
    from conf.basepage import BasePage
    from random import choice
    from conf.decorator import teststep, teststeps
    from utils.vob_data import reconstruction_guess, vob_operate

    class Homework(BasePage):
        """作业页面 元素信息"""

        @teststep
        def homework_count(self):
            """作业类型条目"""
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 选词填空 "]')
            return ele

        @teststep
        def click_homework(self, index):
            # 点击作业
            self.driver.find_elements_by_class_name("XCUIElementTypeCell")[index + 1].click()

        @teststep
        def sengle_count(self):
            # 单项选择的进入条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单项选择 "]')
            return ele

        @teststep
        def tv_testbank_type(self, index):
            """作业的类型 这里用的是xpath"""
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 选词填空 "]')[index]

            # item = self.driver.find_element_by_accessibility_id('选词填空').text

            return item

        @teststep
        def cloze_count(self):
            # 完形填空的进入条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 完形填空 "]')
            print("完形填空", ele)
            return ele

        @teststep
        def single_type(self, index):
            # 单项选择的作用的类型
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单项选择 "]')[index]

            # item = self.driver.find_element_by_accessibility_id('选词填空').text

            return item

        @teststep
        def cloze_type(self, index):
            # 完形填空的作用的类型
            Swipe().swipe_up(1000)
            time.sleep(3)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 完形填空 "]')[index]

            # item = self.driver.find_element_by_accessibility_id('选词填空').text

            return item

        @teststep
        def read_count(self):
            # 阅读理解的进入条件
            Swipe().swipe_up(1000)
            time.sleep(3)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 阅读理解 "]')
            print("阅读理解", ele)
            return ele

        @teststep
        def read_type(self, index):
            # 完形填空的作用的类型

            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 阅读理解 "]')[index]

            # item = self.driver.find_element_by_accessibility_id('选词填空').text

            return item

        @teststep
        def listen_practice_count(self):
            # 听力练习的进入条件

            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 听力练习 "]')
            print("听力练习", ele)
            return ele

        @teststep
        def listen_practice_type(self, index):
            # 完形填空的作用的类型

            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 听力练习 "]')[index]

            # item = self.driver.find_element_by_accessibility_id('选词填空').text

            return item

        @teststep
        def art_type(self, index):
            # 补全文章的作用类型
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 补全文章 "]')[index]

            return item

        @teststep
        def art_count(self):
            # 阅读理解的进入条件

            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 补全文章 "]')
            print("补全文章", ele)
            return ele

        @teststep
        def vob_count(self):
            # 进入词汇选择的条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')
            print("词汇选择", ele)
            return ele

        @teststep
        def vob_count_explanatio(self):
            # 进入词汇选择的条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')
            print("词汇选择", ele)
            return ele

        @teststep
        def vob_type(self, index):
            # 词汇的作用类型
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 词汇选择 "]')[index]

            return item

        @teststep
        def vob_type_YB(self):
            # 词汇的作用类型YB(选单词)
            item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（选单词）"]')

            return item

        @teststep
        def listen_count(self):
            # 进入单词听写的条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词听写 "]')
            print("单词听写", ele)
            return ele

        @teststep
        def listen_type(self, index):
            # 单词听写的作用类型
            time.sleep(2)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词听写 "]')[index]

            return item

        @teststep
        def flash_count(self):
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('(//XCUIElementTypeButton[@name=" 闪卡练习 "])[1]')
            print("闪卡练习", ele)
            return ele

        @teststep
        def flash_type(self, index):
            # 单词听写的作用类型
            item = self.driver.find_elements_by_xpath('(//XCUIElementTypeButton[@name=" 闪卡练习 "])[1]')[index]

            return item

        @teststep
        def copy_count(self):
            # 闪卡练习，抄写模式
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 闪卡练习 "]')
            print("闪卡练习", ele)
            return ele

        @teststep
        def copy_type(self, index):
            # 单词听写的作用类型
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 闪卡练习 "]')[index]

            return item

        @teststep
        def copy_type_study(self):
            # 抄写模式这个学习的类型
            item = self.driver.find_element_by_xpath(
                '//XCUIElementTypeStaticText[@name="马承同步三上 lesson2 闪卡练习（抄写模式）（引用1）"]')
            return item

        @teststep
        def flash_type_study(self):
            item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="中考精华词汇 基础版65（学习模式）"]')
            return item

        @teststep
        def word_type(self, index):
            # 单词拼写的作用类型
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词拼写 "]')[index]

            return item

        @teststep
        def word_type_word(self):

            # 单词拼写的作用类型默写模式
            word = []
            item = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(item)):
                word.append(item[i].text)
            print("列表是", word)

            return item

        @teststep
        def word_type_random(self):

            # 单词拼写的作用类型默写模式
            item = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（随机模式）"]')

            return item

        @teststep
        def word_customize_YB(self):

            #   这个是单词拼写YB下自定义的条框的判断
            time.sleep(3)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（自定义）"]').text
            m = re.findall('自定义', ele)
            print("打印出来的是什么", m[0])
            return m[0]

        @teststep
        def word_write_YB(self):

            #   这个是单词拼写YB下自定义的默写的判断
            time.sleep(3)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（默写模式）"]').text
            m = re.findall('默写模式', ele)
            print("打印出来的是什么", m[0])
            return m[0]

        @teststep
        def word_random_YB(self):

            #   这个是单词拼写YB下自定义的默写的判断
            time.sleep(3)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（随机模式）"]').text
            m = re.findall('随机模式', ele)
            print("打印出来的是什么", m[0])
            return m[0]

        @teststep
        def word_vob_YB(self):

            # 这个是词汇选择YB下的选单词的判断
            time.sleep(3)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（选单词）"]').text
            m = re.findall('选单词', ele)
            print("打印出来的是什么", m[0])
            return m[0]

        @teststep
        def word_count(self):
            # 进入单词听写的条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 单词拼写 "]')
            print("单词拼写", ele)
            return ele

        @teststep
        def strengthen_count(self):
            # 进入单词听写的条件
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 强化炼句 "]')
            print("强化炼句", ele)
            return ele

        @teststep
        def strengthen_type(self, index):
            # 进入单词听写的条件
            time.sleep(2)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 强化炼句 "]')[index]

            return item

        @teststep
        def guess_count(self):
            # 进入猜词游戏的条件
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 猜词游戏 "]')
            print("猜词游戏", ele)
            return ele

        @teststep
        def guess_type(self, index):
            # 进入单词听写的条件
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 猜词游戏 "]')[index]

            return item

        @teststep
        def restore_count(self):
            # 进入还原单词的条件
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 还原单词 "]')
            print("还原单词", ele)
            return ele

        @teststep
        def restore_type(self, index):
            # 进还原单词的条件
            time.sleep(2)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 还原单词 "]')[index]

            return item

        @teststep
        def conjunctions_count(self):
            # 进入还原单词的条件
            time.sleep(3)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连词成句 "]')
            print("连词成句", ele)
            return ele

        @teststep
        def conjunctions_type(self, index):
            # 进入还原单词的条件
            time.sleep(2)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连词成句 "]')[index]

            return item

        @teststep
        def sentence_count(self):
            # 进入句型转换的条件
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 句型转换 "]')
            print("句型转换", ele)
            return ele

        @teststep
        def sentence_type(self, index):
            # 进还原单词的条件
            time.sleep(2)
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 句型转换 "]')[index]

            return item

        @teststep
        def match_count(self):
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连连看 "]')
            print("连连看", ele)
            return ele

        @teststep
        def match_type(self, index):
            # 进入连连看的条件
            item = self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name=" 连连看 "]')[index]

            return item

        @teststep
        def tv_testbank_name(self, index):
            """作业的模式 这里用的xpath"""
            item = self.driver.find_elements_by_class_name('/XCUIElementTypeStaticText')[index].text
            m = re.match(".*\（(.*)\）.*", item)
            print(m.group(1))
            return m.group(1)

        # def click_homework(self):
        #     """点击作业条目 这里用的还是xpath"""
        #     # TODO 作业item点击
        #     self.driver.find_elements_by_xpath('(//XCUIElementTypeStaticText[@name="兼职测试题"])')[1].click()
        @teststep
        def judge_homework_exist(self):
            """判断要进行操作的作业是否存在"""
            homework_title = []
            homework_list = HomePage().homework()
            # 我们得到的列表里面从下标为1开始，每三个才是它的坐标，所有我们这样做的为了过滤一下
            for index1 in range(1, len(homework_list), 3):
                homework_title.append(homework_list[index1].text)  # 获取作业title列表

            print('homework_title:', homework_title, len(homework_title))

            item = homework_title[len(homework_title) - 1]  # 最后一个作业的title
            print('item:', item)

            # tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
            # print('tips:', tips)
            n = 6

            work_list = [homework_title[i:i + n] for i in range(0, len(homework_title), n)]

            return item, homework_title, homework_list, work_list

        @teststep
        def judge_homework_YB(self):
            """判断要进行操作的作业是否存在"""
            homework_title = []
            homework_list = HomePage().homework()
            # 我们得到的列表里面从下标为1开始，每三个才是它的坐标，所有我们这样做的为了过滤一下
            for index1 in range(1, len(homework_list), 3):
                homework_title.append(homework_list[index1].text)  # 获取作业title列表

            print('homework_title:', homework_title, len(homework_title))

            item = homework_title[len(homework_title) - 1]  # 最后一个作业的title
            print('item:', item)

            # tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
            # print('tips:', tips)
            n = 6

            work_list = [homework_title[i:i + n] for i in range(0, len(homework_title), n)]

            return item, homework_title, homework_list, work_list

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

        @teststep
        def games_count(self):
            """小游戏数目 """
            item = self.driver.find_elements_by_id("XCUIElementTypeButton")
            return item

    class Choice_words(BasePage):
        """选词填空"""

        @teststep
        def wait_choice(self):
            # 根据元素的"classname"来进行元素的提取
            time.sleep(2)
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="选词填空"]').text
            return ele

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def chose_blank(self, index):
            # 这个是依次点击五个按钮
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[index]
            return ele

        @teststep
        def click_bounds_num(self, index):
            obj = Homework().tv_testbank_type(index)
            bounds = obj.location
            # print(bounds)
            # x = obj.get_attribute("x")
            # print(x)
            # y = obj.get_attribute("y")
            # print(y)
            x = bounds['x']
            y = bounds['y']
            # width = size['width']
            # height = size['height']

            loc_x = x + 100
            loc_y = y

            click_bounds(self, loc_x, loc_y)
            # click_bounds(self,int(x)+100,int(y))
            # ele = self.driver.find_element_by_accessibility_id("x").text
            # print(ele)
            # time.sleep(2)

        @teststep
        def small_font(self):
            # 点击普通的小字体
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
            print("点击了缩小的Aa的图标。英文字体变得小了")

        def ordinary_front(self):
            # 点击普通的字体
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
            print("点击了普通大小的的Aa的图标。英文字体发生了改变了")

        def big_front(self):
            # 点击大字体
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
            print("点击了放大的Aa的图标。英文字体扩大了了")

        @teststep
        def arrow(self):
            # 这个是那个arrow的箭头，用xpath来选取元素
            # 再次点击按钮（两次按钮的元素是不一样的）
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
            if ele == "doneItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def back_btn(self):
            # 返回按钮用xpath进行定位
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def tip_words(self):
            # 还是以这个提示词的xpath选取元素的
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="提示词"]').click()

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["s", "s", "d", "a"]
            word = list(ele)
            for i in range(len(word)):
                games_keyboard(self, word[i])

    class Single_choice(BasePage):
        """单项选择练习"""

        @teststep
        def wait_page(self, timeout=10, poll_frequency=0.5):
            # 以这个页面的xpath作为依据,证明已经进入了这个页面
            element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="单项选择"]').text
            # element = self.driver.find_element_by_accessibility_id('单项选择').text
            time.sleep(3)
            return element

        @teststep
        def back_btn(self):
            """返回按钮以xpath作为元素"""
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def light_btn_text(self):
            """前进的那个按钮"""
            element = self.driver.find_element_by_accessibility_id('doneItem').text
            return element

        @teststep
        def rate(self):
            """获取作业数量"""
            rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
            return rate

        # 下一步按钮
        @teststep
        def light_btn(self):
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')[1]
            return ele

        # 灰色的按钮，获取里面的元素
        @teststep
        def gary_btn_text(self):
            element = self.driver.find_element_by_accessibility_id('doneItemNo').text
            return element

        # 灰色按钮
        def gray_btn(self):
            self.driver.find_element_by_accessibility_id('doneItemNo').click()

        # 点击那个完形填空的字是不能进入后面的界面的，所以我们向右多移动了100px的距离，然后就可以点带那个大的框了
        @teststep
        def single_bound_num(self, index):
            obj = Homework().single_type(index)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            # width = size['width']
            # height = size['height']

            loc_x = x + 100
            loc_y = y

            click_bounds(self, loc_x, loc_y)

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def single_bound_num_rank(self, index):
            # 点击排行榜
            obj = Homework().single_type(index)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            # width = size['width']
            # height = size['height']

            loc_x = x + 340
            loc_y = y
            print("点击的位置", loc_x, loc_y)

            click_bounds(self, loc_x, loc_y)

        @teststep
        def correct_reply(self):
            # 点击正确的回答
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="这个是答案"]').click()

        @teststep
        def correct_reply(self):
            # 点击正确的回答
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="这个是答案"]').click()

        def choice_A(self):
            # 选择A选项
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="A"]').click()

        @teststep
        def option_button(self):
            """获取四个选项"""
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")

            return ele

        @teststep
        def option_button_YB(self):
            """获取四个选项"""
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
            YB = ele[0:3]
            print("我们要点击的单词", YB)

            return YB

        @teststep
        def single_option(self):
            # 得到我们正确答案的列表的下表盘
            single_list = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                single_list.append(ele[i].text)
            print(single_list)

            index = [i for i, x in enumerate(single_list) if x == self.option_button_YB()][0]
            print("选项的索引", index)
            return index

        def option_YB(self):

            self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[int(self.single_option() - 1)].click()

        def wait_process(self):
            # 待完成这个文字
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="待完成："]').text
            return element

    class Cloze(BasePage):
        # 完形选择\
        # 初始化__init__函数

        @teststep
        def wait_cloze(self):
            # 以完形填空的xpath为依据，然后用里面的text进行判断，是否进入到这一页
            element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="完形填空"]').text
            return element

        @teststep
        def back_btn(self):
            # 左上角的返回按钮，以xpath作为依据
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def small_font(self):
            # 点击普通的小字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
            print("点击了缩小的Aa的图标。英文字体变得小了")

        def ordinary_front(self):
            # 点击普通的字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
            print("点击了普通大小的的Aa的图标。英文字体发生了改变了")

        def big_front(self):
            # 点击大字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
            print("点击了放大的Aa的图标。英文字体扩大了了")

        @teststep
        def cloze_num(self):
            # 拿到我们需要做的题的个数
            rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
            return rate

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def cloze_correct(self):
            # 正确的答案
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[2]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[3]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[4]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[5]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[6]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[7]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[8]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[9]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[10]').click()
            time.sleep(2)

        @teststep
        def cloze_option_button(self, i):
            """获取四个选项"""
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
            # print("答案的列表",len(ele))

            return ele

        @teststep
        # 点击我们完形填空的空白的地方
        def cloze_bound_num(self, index):
            obj = Homework().cloze_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        # 这个是我们的箭头的按键
        @teststep
        def cloze_arrow(self):
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
            if ele == "doneItem":
                print("填写全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        # 点击错题再练
        @teststep
        def wrong_problem(self):
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def again_problem(self):
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        # 点击查看答案'
        @teststep
        def check_answer(self):
            time.sleep(2)

            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

    class ReadingComprehension(BasePage):

        @teststep
        def wait_read(self):
            # 以阅读理解的xpath为依据，然后用里面的text进行判断，是否进入到这一页
            element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="阅读理解"]').text
            return element

        @teststep
        def back_btn(self):
            # 左上角的返回按钮，以xpath作为依据
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def read_num(self):
            # 拿到我们需要做的题的个数
            element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
            return element

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def read_bound_num(self, index):
            obj = Homework().read_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def read_option_button(self, i):
            """获取四个选项"""
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
            # print("答案的列表",len(ele))

            return ele

        # 这个是我们的箭头的按键
        @teststep
        def read_arrow(self):
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
            if ele == "doneItem":
                print("填写全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def click_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[2]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[3]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[4]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="答案"])[5]').click()
            time.sleep(2)

        # 点击再练一边
        @teststep
        def practice_again(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        @teststep
        def small_font(self):
            # 点击普通的小字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
            print("点击了缩小的Aa的图标。英文字体变得小了")

        def ordinary_front(self):
            # 点击普通的字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
            print("点击了普通大小的的Aa的图标。英文字体发生了改变了")

        def big_front(self):
            # 点击大字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
            print("点击了放大的Aa的图标。英文字体扩大了了")

        # 点击查看答案'
        @teststep
        def check_answer(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    class Complement_article(BasePage):
        # 补全文章的作业

        @teststep
        def wait_art(self):
            # 以补全文章的xpath为依据，然后用里面的text进行判断，是否进入到这一页
            element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="补全文章"]').text
            return element

        @teststep
        def back_btn(self):
            # 左上角的返回按钮，以xpath作为依据
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def art_num(self):
            # 拿到我们需要做的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            return element

        @teststep
        def art_bound_num(self, index):
            obj = Homework().art_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        def comp_num(self):
            # 拿到我们需要做的题的个数
            element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
            return element

        @teststep
        def read_option_button(self, i):
            """获取四个选项"""
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
            # print("答案的列表",len(ele))

            return ele

        # 这个是我们的箭头的按键

        @teststep
        def again_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
            if ele == "doneItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        # 点击再练一边
        time.sleep(2)

        @teststep
        def wrong_again(self):
            time, slice(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()
            time.sleep(2)

        # 点击查看答案'
        @teststep
        def check_answer(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        # 点击补全文章的选择
        @teststep
        def art_A(self):
            time.sleep(1)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="A"]').click()

        @teststep
        def art_B(self):
            time.sleep(1)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="B"]').click()

        @teststep
        def art_C(self):
            time.sleep(1)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="C"]').click()

        @teststep
        def art_D(self):
            time.sleep(1)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="D"]').click()

        @teststep
        def art_E(self):
            time.sleep(1)
            Swipe().swipe_up_bottom(1000)
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="E"]').click()

        @teststep
        def small_font(self):
            # 点击普通的小字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[1]').click()
            print("点击了缩小的Aa的图标。英文字体变得小了")

        def ordinary_front(self):
            # 点击普通的字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[2]').click()
            print("点击了普通大小的的Aa的图标。英文字体发生了改变了")

        def big_front(self):
            # 点击大字体
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="Aa"])[3]').click()
            print("点击了放大的Aa的图标。英文字体扩大了了")

    class Vobcabulary(BasePage):
        """词汇选择"""

        @teststep
        # 我们点击的词汇选择的框
        def vob_bound_num(self, index):
            obj = Homework().vob_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)

        @teststep
        def vob_reconstrction(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选解释）"]').click()

        @teststep
        def vob_word(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选单词）"]').click()

        @teststep
        def vob_bound_num_YB(self):
            obj = Homework().vob_type_YB()
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)

            time.sleep(2)

        @teststep
        def vob_voice(self):
            # 点击喇叭让应用读音
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="audio wq"]').click()

        @teststep
        def vob_option_button(self):
            """获取四个选项"""
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeCell")

            return ele

        @teststep
        def vob_option_reconstruction(self):
            """获取四个选项"""
            time.sleep(5)
            vob = []
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
            for i in range(len(ele)):
                vob.append(ele[i].text)
            print("这个列表是", vob)
            return vob

        @teststep
        def options(self):
            """获取四个选项"""
            # word = []
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
            # for i in range(len(ele)):
            #     word.append(ele[i].text)
            # print("需要填写的单词是",word)
            return ele

        @teststep
        def option(self):
            """获取四个选项"""
            word = []
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("需要填写的单词是", word)
            return word

        @teststep
        def options_word(self, index):
            # 点击选项
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[index]

            return ele

        @teststep
        def word(self):
            # 获取的单词
            # word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text
            # for i in range(len(ele)):
            #     word.append(ele[i].text)
            # print("列表里面的单词是",word)
            return ele

        @teststep
        def vob_explanation(self):
            # 进入词汇选择选解释的条件
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="剑桥3级词汇小测8月22日（选解释）"]').text
            m = re.match(".*\（(.*)\）.*", element)
            return m.group(1)

        @teststep
        def vob_explanation_reconstruction(self):
            # 进入词汇选择选解释的条件
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选解释）"]').text
            m = re.match(".*\（(.*)\）.*", element)
            return m.group(1)

        @teststep
        def vob_explanation_word(self):
            # 进入词汇选择选解释的条件
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（选单词）"]').text
            m = re.match(".*\（(.*)\）.*", element)
            return m.group(1)

        @teststep
        def vob_listen(self):
            # 进入听音选词的条件
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="外研版第一单元单词听写（听音选词）"]').text
            m = re.match(".*\（(.*)\）.*", element)
            return m.group(1)

        @teststep
        def vob_num(self):
            # 拿到我们需要做的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
            return element

        @teststep
        def vob_num_YB(self):
            # 拿到我们需要做的题的个数
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            return element

        @teststep
        def vob_num_word_YB(self):
            # 拿到我们需要做的题的个数
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            return element

        @teststep
        def vob_explantion_num(self):
            # 词汇选择看词选解释的最大的题目数量
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="12"]').text
            return element

        @teststep
        def vob_explantion_num_reconstruction(self):
            # 词汇选择看词选解释的最大的题目数量
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            return element

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有选择单词灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def vob_listen_num(self):
            # 词汇选择听音、选解释的最大的题目数量
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
            return element

        @teststep
        def light_btn(self):
            # 前进的那个按钮
            # time.sleep(2)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def clcik_voice(self):
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def return_btn(self):
            # 点击返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def wrong_problem(self):
            # 点击错题再练
            time.sleep(2)
            print("点击错题再练说明出现错题再练的标志")
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def again_problem(self):
            # 点击错题再练
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        # 结果页的方法与逻辑
        @teststep
        def show_page(self):
            time.sleep(2)
            ele = []
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(element)):
                ele.append(element[i].text)
            print('元素的text属性', ele)
            return ele

        @teststep
        def correct_rate(self):
            """准确率"""
            time.sleep(2)
            rate = \
            self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[
                0].text
            time.sleep(2)
            num = re.search(r'\d+', rate)
            return num.group()

        @teststep
        def result_score(self):
            """结果页积分"""
            rate = \
            self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[
                1].text
            num = re.search(r'\d+', rate)
            return num.group()

        @teststep
        def result_star(self):
            """星星"""
            rate = \
            self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[
                2].text
            num = re.search(r'\d+', rate)
            return num.group()

        @teststep
        def result_time(self):
            """时间"""
            rate = \
            self.driver.find_elements_by_xpath("//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")[
                3].text
            pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b')  # 定义匹配模式
            num = re.findall(pattern, rate)
            # print(re.findall(pattern, rank)[0])
            return num[0]

        @teststep
        def rank_accuracy_rate(self):
            """准确率最高的那次的正确率"""
            rate = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2].text
            num = re.search(r'\d+', rate)
            return num.group()

        @teststep
        def rank_spend_time(self):
            """准确率最高的那次 完成所用时间"""
            time = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
            pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b')  # 定义匹配模式
            num = re.findall(pattern, time)
            # print(re.findall(pattern, rank)[0])
            return num[0]

        @teststep
        # 结果页的方法与逻辑
        def end_page(self):
            time.sleep(2)
            rank_now = self.correct_rate()  # 学生这次做完题的准确率
            rank_integral = self.result_score()  # 学生这次做完题的积分
            rank_start = self.result_star()  # 学生的星星
            rank_time = self.result_time()  # 学生做完答题所用的时间
            best_score = self.rank_accuracy_rate()
            work_time = self.rank_spend_time()
            # 01:08
            rank_now_time = int(rank_time[0:1]) * 3600 + int(rank_time[1:2]) * 60 + int(rank_time[3:4]) * 10 + int(
                rank_time[4:5])
            rank_best_time = int(work_time[0:1]) * 3600 + int(work_time[1:2]) * 60 + int(work_time[3:4]) * 10 + int(
                work_time[4:5])
            print("打印出来的一些列元素", rank_now, rank_integral, rank_start, rank_time, best_score, work_time)
            print("此时学生做题的准确率：%s，积分:%s,星星：%s，时间:%s" % (rank_now, rank_integral, rank_start, rank_time))
            if int(rank_now) >= int(best_score) and rank_now_time >= rank_best_time:
                print("您的答题正确率得到了提高，但是答题的效率稍微低了一点，您的答题正确率为%d,答题的时间为%d" % (int(rank_now), rank_now_time))

            elif int(rank_now) >= int(best_score) and rank_now_time < rank_best_time:
                print("Congratulations您的正确率和答题时间超越了你的最高水平，当前你的最高正确率是%d,您的最佳答题时间为%d" % (int(rank_now), rank_now_time))

            elif int(rank_now) >= int(best_score) and rank_now_time >= rank_best_time:
                print("您的答题正确率得到了提高，但是答题的效率稍微低了一点，您的答题正确率为%d,答题的时间为%d" % (int(rank_now), rank_now_time))
            else:
                print("您的答题时间和正确率都没有提高。。请再接再厉，您当前答题的正确率为%d，答题的时间为%d秒" % (int(rank_now), rank_now_time))
            time.sleep(2)
            return rank_now, rank_integral, rank_start, rank_now_time

    class Dictation(BasePage):
        """单词听写"""

        @teststep
        # 我们点击单词听写的框
        def listen_bound_num(self, index):
            obj = Homework().listen_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["s", "s", "d", "a"]
            word = list(ele)
            for i in range(len(word)):
                games_keyboard(self, word[i])

        @teststep
        def arrow(self):
            # 点金前进的那个箭头
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def again_arrow(self):
            # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        # 点击喇叭
        @teststep
        def clcik_voice(self):
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def return_btn(self):
            # 点击返回
            time.sleep(1)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def wrong_problem(self):
            # 点击错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    class Word_spelling(BasePage):
        """单词拼写"""

        # 我们点击的单词拼写的框
        @teststep
        def word_bound_num(self, index):
            obj = Homework().word_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def word_bound_write(self):
            # 点击单词拼写的默写模式
            obj = Homework().word_type_word()
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def word_write_xpath(self):

            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（默写模式）"]').click()

        @teststep
        def word_write(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（默写模式）"]').click()

        @teststep
        def word_write_random(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（随机模式）"]').click()

        @teststep
        def word_bound_random(self):
            # 点击单词拼写的随机模式
            obj = Homework().word_type_random()
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def max_number_YB(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            time.sleep(2)
            return element

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["s", "s", "d", "a"]
            word = list(ele)
            for i in range(len(word)):
                games_keyboard(self, word[i])

        @teststep
        def determination(self):
            """用于判定是否是空白"""

            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[3].text
            print(ele)
            if ele == " None":
                print("默写模式横线上是空的")
            return ele

        @teststep
        def arrow(self):
            # 点金前进的那个箭头
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        # 点击喇叭
        def clcik_voice(self):
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def again_arrow(self):
            # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def word_spelling_text(self):
            # 单词拼写的text

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text

            return ele

        @teststep
        def word_spelling_write(self):
            # 单词拼写的text

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[4].text

            return ele

        @teststep
        def word_YB(self):
            word = yb_letter(self.word_spelling_text())

            games_keyboard(self, word)
            print("这个单词是", word)

        @teststep
        def word_write_YB(self):
            # 这个是单词拼写的默写模式
            word = yb_letter_write(self.word_spelling_write())

            games_keyboard(self, word)
            print("这个单词是", word)

        @teststep
        def word_write_ew(self):
            # ew 是bug点不了特殊处理
            word = ["e", "w"]
            for i in range(len(word)):
                games_keyboard(self, word[i])

            print("这个单词是", word)

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def return_btn(self):
            # 点击返回
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
            time.sleep(1)

        @teststep
        def wrong_problem(self):
            # 点击错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def again_practice(self):
            # 点击错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

    class FlashCard(BasePage):
        """闪卡练习"""

        # 我们点击闪卡游戏的框
        @teststep
        def flash_bound_num(self):
            obj = Homework().flash_type_study()
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="15"]').text
            time.sleep(2)
            return element

        @teststep
        def max_number_YB(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            time.sleep(2)
            return element

        def max_number_reconstruction(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        def max_number_reconstruction1(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def flash_study(self):
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="中考精华词汇 基础版65（学习模式）"]').text
            m = re.match(".*\（(.*)\）.*", element)
            return m.group(1)

        @teststep
        def chick_blank(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="changeNo"]').click()
            time.sleep(2)

        @teststep
        def chick_flash_study(self):
            # 我们点击的那个框

            # def chick_flash_bound(self):
            #     obj = Homework(self.driver).flash_type_study()
            #     print(obj)
            #     bounds = obj.location

            # x = bounds['x']
            # y = bounds['y']
            loc_x = 180
            loc_y = 285
            click_bounds(self, loc_x, loc_y)

        @teststep
        def flash_study_YB(self):
            """以YB模式的xpath为标准"""
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（学习模式）"]').click()

        @teststep
        def flash_study_reconstruction(self):
            """以xpath为标准"""
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（学习模式）（引用1）"]').click()

        @teststep
        def flash_study_reconstruction1(self):
            """以xpath为标准"""
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（学习模式）"]').click()

        @teststep
        def arrow(self):
            # 点金前进的那个箭头
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def word_explain(self):
            # 以及解释

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print('闪卡模式双面的英文单词，单词是', ele)
            return ele

        @teststep
        def word_explain1(self):
            # 以及解释

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text
            print('闪卡模式双面的中文解释，单词是', ele)
            return ele

        @teststep
        def word(self):
            # 英文单词
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print('在双面模式下的英文的单词', ele)
            return ele

        def explanation(self):
            # 中文解释

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print('在双面模式下的中文的解释', ele)
            return ele

        @teststep
        def again_arrow(self):
            # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
            self.driver.find_element_by_xpath('	//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def again_study(self):
            # 点击在学一边
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="再学一遍 Study again"]').click()

        @teststep
        def mark_again(self):
            # 点击标记内容在学一遍
            self.driver.find_element_by_xpath(
                '//XCUIElementTypeStaticText[@name="标记⭐️内容再练一遍 ⭐️Star cards study again"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def click_star(self):
            # 点击星星
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()

        @teststep
        def click_card(self):
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="changeNo"]').click()

        @teststep
        def return_btn(self):
            # 点击返回
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    class Flash_copy(BasePage):

        # 我们点击闪卡游戏的框
        @teststep
        def flash_bound_num(self):
            obj = Homework().copy_type_study()
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="10"]').text
            time.sleep(2)
            return element

        @teststep
        def max_number_copy_YB(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            time.sleep(2)
            return element

        @teststep
        # def max_number_copy_(self):
        #     # 获取我们需要填写的题的个数
        #     number = []
        #     element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        #     time.sleep(2)
        #     for i in range(len(element)):
        #         number.append(element[i].text)
        #     print("这个页面的所有的name属性是",number)
        #     return number
        @teststep
        def max_number_copy_reconstruction(self):
            # 获取我们需要填写的题的个数

            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def copy_study(self):
            element = self.driver.find_element_by_xpath(
                '//XCUIElementTypeStaticText[@name="马承同步三上 lesson2 闪卡练习（抄写模式）（引用1）"]').text
            print(element)
            m = re.findall("抄写模式", element)
            name = m[0]
            return name

        @teststep
        def word(self):
            """闪卡练习- 抄写模式 内展示的Word"""
            ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2]

            return ele

        @teststep
        def voice(self):
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

        @teststep
        def chick_flash_study(self):

            loc_x = 180
            loc_y = 285
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)

        @teststep
        def copy_flash(self):

            max_num = self.max_number()
            # 获取到我们需要的最大的题数

            for i in range(0, int(max_num) - 6):
                word = list(self.word().text)

                self.voice()
                time.sleep(2)
                self.click_star()
                print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
                for j in range(len(word)):
                    games_keyboard(self, word[j])
                time.sleep(4)

            word_list = ["o", "k"]
            self.voice()
            time.sleep(2)
            self.click_star()
            for k in range(len(word_list)):
                games_keyboard(self, word_list[k])
                time.sleep(3)

        @teststep
        def copy_flash_fun(self):

            for q in range(0, 5):
                word = list(self.word().text)

                self.voice()
                time.sleep(2)
                self.click_star()
                print("第几题：%s" % (q + 1), "单词是:%s" % self.word().text)
                for w in range(len(word)):
                    games_keyboard(self, word[w])
                time.sleep(3)

        @teststep
        def copy_flash_YB(self):
            big_C = 'c'
            max_num = self.max_number_copy_YB()
            # 获取到我们需要的最大的题数

            for i in range(0, 2):
                word = list(self.word().text)
                time.sleep(2)
                self.voice()
                time.sleep(2)
                self.click_star()
                print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
                for j in range(len(word)):
                    games_keyboard(self, word[j])
                time.sleep(4)
            self.voice()
            time.sleep(2)
            self.click_star()
            games_keyboard(self, big_C)
            time.sleep(3)
            for i in range(0, int(max_num) - 3):
                word = list(self.word().text)
                time.sleep(2)
                self.voice()
                time.sleep(2)
                self.click_star()
                print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
                for j in range(len(word)):
                    games_keyboard(self, word[j])
                time.sleep(4)

        def copy_flash_reconstruction(self):
            i = 0

            max_num = int(self.max_number_copy_reconstruction())
            # self.max_number_copy_()
            # 获取到我们需要的最大的题数

            for i in range(0, max_num):

                max_num = int(self.max_number_copy_reconstruction())
                i = i + 1
                print("进入第%d题,我们需要完成的小题的数目%d" % (i, max_num))
                word = list(self.word().text)
                time.sleep(2)
                self.voice()
                time.sleep(2)
                self.click_star()
                print("第几题：%s" % (i), "单词是:%s" % self.word().text)
                for j in range(len(word)):
                    games_keyboard(self, word[j])
                print("输入正确，两秒之后自动跳转到下一题")
                time.sleep(4)

        def copy_flash_reconstruction1(self):
            i = 0

            max_num = int(self.max_number_copy_reconstruction())
            # self.max_number_copy_()
            # 获取到我们需要的最大的题数

            for i in range(0, max_num):

                max_num = int(self.max_number_copy_reconstruction())
                i = i + 1
                print("进入第%d题,我们需要完成的小题的数目%d" % (i, max_num))
                word = list(self.word().text)
                time.sleep(2)
                self.voice()
                time.sleep(2)

                print("第几题：%s" % (i), "单词是:%s" % self.word().text)
                for j in range(len(word)):
                    games_keyboard(self, word[j])
                print("输入正确，两秒之后自动跳转到下一题")
                time.sleep(4)

        @teststep
        def copy_type_study_yb(self):
            # YB模式下的闪卡练习的抄写模式
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（抄写模式）"]').click()

        @teststep
        def copy_type_study_reconstruction(self):
            # 重构下的闪卡练习的抄写模式
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（抄写模式）"]').click()

        @teststep
        def arrow(self):
            # 点金前进的那个箭头
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def again_arrow(self):
            # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
            self.driver.find_element_by_xpath('	//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def again_study(self):
            # 点击在学一边
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="再学一遍 Study again"]').click()

        @teststep
        def mark_again(self):
            # 点击标记内容在学一遍
            self.driver.find_element_by_xpath(
                '//XCUIElementTypeStaticText[@name="标记⭐️内容再练一遍 ⭐️Star cards study again"]').click()

        @teststep
        def click_star(self):
            # 点击星星
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def click_star(self):
            # 点击星星
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()

        @teststep
        def return_btn(self):
            # 点击返回
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    class Strengthen_sentence(BasePage):
        # 强化炼句
        @teststep
        def click_strengthen_self(self):
            # 点击自定义模式下的强化炼句
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（自定义模式）"]').click()

        @teststep
        def click_strengthen_write(self):
            # 点击自定义模式下的强化炼句
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（默写模式）"]').click()

        @teststep
        def click_strengthen_complex(self):
            # 点击自定义模式下的强化炼句
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（复杂模式）"]').click()

        @teststep
        def click_strengthen_simple(self):
            # 点击自定义模式下的强化炼句
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（简单模式）"]').click()

        @teststep
        def strengthen_bound_num(self, index):
            obj = Homework().strengthen_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def max_number(self):
            # 获取我们需要填写的题的个数
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="4"]').text
            time.sleep(2)
            return element

        @teststep
        def silent_max_num(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["s"]
            word = list(ele)
            for i in range(len(word)):
                games_keyboard(self, word[i])

        @teststep
        def horizontal_line(self):
            # 点击横线

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')

            return ele

        @teststep
        def horizontal_line_paper(self):
            # 点击横线

            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

        @teststep
        def horizontal_line_1(self):
            # 点击横线
            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

        def horizontal_line_2(self):
            # 点击横线2

            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()

        @teststep
        def arrow(self):
            # 点击那个前进的按钮
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def again_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def wrong_again(self):
            # 错题再练
            time.sleep(5)

            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()
            # 点击喇叭

        @teststep
        def clcik_voice(self):
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def return_btn(self):
            # 返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

    class Match_exerciser(BasePage):
        # 连连看

        @teststep
        def match_bound_num(self, index):
            # 点击框的位置
            obj = Homework().match_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def max_number(self):
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="8"]').text
            time.sleep(2)
            return element

        @teststep
        def max_number_YB(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def chick_answer(self):
            # 点击答案
            time.sleep(5)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def clcik_voice(self):
            # 点击声音
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def again(self):
            # 点击再练一遍
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        @teststep
        def return_btn(self):
            # 返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def quite(self):
            # 点击quite这个单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="quiet"]').click()

        @teststep
        def re_quite(self):
            # 点击quite这个英文单词、
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="安静的"]').click()

        @teststep
        def student(self):
            # 点击学生这个单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="student"]').click()

        @teststep
        def re_student(self):
            # 点击学生这个中文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="学生"]').click()

        @teststep
        def mr(self):
            # 点击mr这个英文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Mr."]').click()

        @teststep
        def re_mr(self):
            # 点击mr这个中文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="先生"]').click()

        @teststep
        def teacher(self):
            # 点击老师这个英文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="teacher"]').click()

        @teststep
        def re_techer(self):
            # 点就教师这个中文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="教师"]').click()

        @teststep
        def mrs(self):
            # 点击女士这个英文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Mrs."]').click()

        @teststep
        def re_mrs(self):
            # 点击女士这个中文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="女士；夫人"]').click()

        @teststep
        def doctor(self):
            # 点击英文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doctor"]').click()

        @teststep
        def re_doctor(self):
            # 点击中文这个单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="医生"]').click()

        @teststep
        def beside(self):
            # 点击beside
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="beside"]').click()

        @teststep
        def re_beside(self):
            # 点击中文在。。。身边
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="在……旁边"]').click()

        @teststep
        def nurse(self):
            # 点击护士这个英文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nurse"]').click()

        @teststep
        def re_nurse(self):
            # 点击护士这个中文单词
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="护士"]').click()

        @teststep
        def list1(self):

            word1_list = ["/ɑ/", "/ɜ/", "/ɔ/", "/ð/", "/ə/"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = yb_letter_select(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                time.sleep(2)

        @teststep
        def list2(self):
            word1_list = ["/ɒ/", "/g/", "/ʊ/", '/ɪ/', "/θ/"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = yb_letter_select(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                time.sleep(2)

        @teststep
        def list3(self):
            word1_list = ["/ʃ/", "/ʌ/", "/ʒ/", "/ɛ/", "/ŋ/"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = yb_letter_select(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                time.sleep(2)

        @teststep
        def list4(self):
            word1_list = ["/æ/", "/ˈ/"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = yb_letter_select(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                time.sleep(2)

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def list_re(self):
            word1_list = ["Apple", "Hello", "like", "over"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                print("这里面的序号是", index)
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = vob_operate(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                self.time_view()
                time.sleep(2)

        @teststep
        def list_again(self):
            word1_list = ["like is", "but"]

            all_list = []
            # 这个是单词和解释的列表
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            # 遍历这个列表
            for i in range(len(ele)):
                # 把这个列表的text属性提取出来然后添加到一个新的列表里面
                all_list.append(ele[i].text)
            print("所有列表的内容是", all_list)
            for j in range(len(word1_list)):
                index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
                value = vob_operate(word1_list[j])
                time.sleep(2)
                print(value)
                index2 = [i for i, x in enumerate(all_list) if x == value][0]
                self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
                self.time_view()
                time.sleep(2)

    class Listen_practice(BasePage):
        # 作业之听力练习

        @teststep
        def wait_read(self):
            # 以阅读理解的xpath为依据，然后用里面的text进行判断，是否进入到这一页
            element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="听力练习"]').text
            return element

        @teststep
        def back_btn(self):
            # 左上角的返回按钮，以xpath作为依据
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def listen_num(self):
            # 拿到我们需要做的题的个数
            element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
            return element

        @teststep
        def listen_bound_num(self, index):
            obj = Homework().listen_practice_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def listen_option_button(self, i):
            """获取四个选项"""
            ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
            # print("答案的列表",len(ele))

            return ele

        @teststep
        def listen_speaker(self):
            # 听力的那个喇叭
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        # 这个是我们的箭头的按键
        @teststep
        def listen_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
            if ele == "doneItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        # 点击再练一边
        @teststep
        def practice_again(self):
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        # 点击查看答案'
        @teststep
        def check_answer(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    class Guess_game(BasePage):
        # 猜词游戏

        @teststep
        def guess_bound_num(self, index):
            obj = Homework().guess_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def guess_listen_YB(self):
            # YB模式下的人猜词游戏有发音
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（有发音）"]').click()

        @teststep
        def guess_listen(self):
            # YB模式下的人猜词游戏有发音
            time.sleep(2)

            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（有发音）"]').click()

        @teststep
        def guess_no_listen(self):
            # YB模式下的人猜词游戏有发音
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（无发音）"]').click()

        @teststep
        def guess_no_listen_YB(self):
            # YB模式下的猜词游戏无发音
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（无发音）"]').click()

        @teststep
        def guess_max_num(self):
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
            time.sleep(2)
            return element

        @teststep
        def guess_max_listen(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def guess_max_YB_num(self):
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            time.sleep(2)
            return element

        @teststep
        def guess_max_YB_no_num(self):
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="18"]').text
            time.sleep(2)
            return element

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
            word = list(ele)
            for i in range(len(word)):
                guess_keyboard(self, word[i])

        @teststep
        def word_YB(self):

            word = yb_letter(self.guess_write())

            guess_keyboard(self, word)
            print("这个单词是", word)

        @teststep
        def word_correct(self):
            """填写正确的单词的方法"""
            word = reconstruction_guess(self.guess_write())
            for i in range(len(word)):
                guess_keyboard(self, word[i])
            print("这个单词是", word)

        @teststep
        def word_no_list_YB(self):

            word = yb_guess(self.guess_write())

            guess_keyboard(self, word)
            print("这个单词是", word)

        @teststep
        def guess_word(self):

            """这里需要用到小键盘 内展示的Word"""
            ele = ["e", "w"]
            ele = ["e", "w"]
            word = list(ele)
            for i in range(len(word)):
                guess_keyboard(self, word[i])

        @teststep
        def guess_word_apple(self):

            """这里需要用到小键盘 内展示的Word"""
            ele = ["a", "p", "p", "l", "e"]

            word = list(ele)
            for i in range(len(word)):
                guess_keyboard(self, word[i])

        @teststep
        def guess_write(self):
            # 单词拼写的text

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text

            return ele

        # def guess_write_no_listen(self):
        #     #单词拼写的text
        #     word = []
        #     ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        #     for i in range(len(ele)):
        #         word.append(ele[i].text)
        #
        #     print("单词列表",word)

        # return ele

        @teststep
        def horizontal_line(self):
            # 点击横线
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')
            print("列表的个数和列表", len(ele), ele)

            return ele

        @teststep
        def horizontal_line_1(self):
            # 点击横线
            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

        @teststep
        def horizontal_line_2(self):
            # 点击横线2

            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()

        @teststep
        def arrow(self):
            # 点击那个前进的按钮
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def again_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        # 点击喇叭
        @teststep
        def clcik_voice(self):
            self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
            print("点击喇叭，但是发生准确与否还不能判断")

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def wrong_again(self):
            # 错题再练
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def again_exercise(self):
            # 错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        @teststep
        def return_btn(self):
            # 返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    class Restore_words(BasePage):
        # 还原单词

        @teststep
        def restore_bound_num(self, index):
            obj = Homework().restore_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def restore_max_num(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("题目序号", element)
            time.sleep(2)
            return element

        @teststep
        def word(self):

            """这里需要用到小键盘 内展示的Word"""
            ele = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
            word = list(ele)
            for i in range(len(word)):
                guess_keyboard(self, word[i])

        @teststep
        def sound(self):
            # 点击声音
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

        @teststep
        def drag(self):
            Swipe().swipe_up_restore(1000)

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def arrow(self):
            # 点击那个前进的按钮
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def show_word(self):
            # 显示内容的列表
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("我们的单词的列表是", word)
            return word

        @teststep
        def again_arrow(self):
            # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有挪动单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def chick_answer(self):
            # 点击答案
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def wrong_again(self):
            # 错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def return_btn(self):
            # 返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    class Sentence_conversion(BasePage):
        # 句型转换

        @teststep
        def sentence_bound_num(self, index):
            obj = Homework().sentence_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def sentence_max_num(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            time.sleep(2)
            return element

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

        @teststep
        def time_view(self):
            # 计时的时间
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            print("现在做题的时间是：", ele)

        @teststep
        def choice_blanck_num(self):
            # 这个是用来计算的
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            return ele

        @teststep
        def choice_blank(self, i):
            # 拿到我们所有的答案的列表

            element = self.driver.find_elements_by_class_name('XCUIElementTypeButton')[i]

            return element

            # print('元素和个数',len(ele),ele)

        @teststep
        def words_num(self):
            l = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
            for i in range(len(ele)):
                l.append(ele[i].text)
            print("这个列表的所有元素是", l)

            return ele

        @teststep
        def sound(self):
            # 点击声音
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

        @teststep
        def drag(self):
            Swipe().swipe_up_restore(1000)

        @teststep
        def arrow(self):
            # 点击那个前进的按钮
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def again_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def show_answer(self):
            # 显示的全部答案
            word = []
            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
            for i in range(len(ele)):
                word.append(ele[i].text)
            print("正确的单词的列表是", word)

        @teststep
        def wrong_again(self):
            # 错题再练
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def return_btn(self):
            # 返回
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    class Conjunctions_sentence(BasePage):
        # 连词成句

        @teststep
        def conjunctions_bound_num(self, index):
            obj = Homework().conjunctions_type(index)
            print(obj)
            bounds = obj.location

            x = bounds['x']
            y = bounds['y']
            loc_x = x + 100
            loc_y = y
            print("点击的位置", loc_x, loc_y)
            click_bounds(self, loc_x, loc_y)
            time.sleep(2)

        @teststep
        def add_YB_restore(self):
            # 进入加YB还原单词的列表

            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="加YB还原单词"]').click()

        @teststep
        def conjunctions_max_num(self):
            time.sleep(2)
            element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
            time.sleep(2)
            return element

        @teststep
        def conjunctions_max_num_YB(self):
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
            time.sleep(2)
            return element

        @teststep
        def word(self):
            """这里需要用到小键盘 内展示的Word"""
            ele = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
            word = list(ele)
            for i in range(len(word)):
                guess_keyboard(self, word[i])

        @teststep
        def sound(self):
            # 点击声音
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

        @teststep
        def drag(self):
            Swipe().swipe_up_conjunctions(1000)

        @teststep
        def drag_re(self):
            Swipe().swipe_up_conjunctions_re(1000)

        @teststep
        def drag_YB(self):

            Swipe().swipe_up_restore(1000)

        @teststep
        def arrow(self):
            # 点击那个前进的按钮
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

        @teststep
        def grey_btn(self):
            """灰色按钮是不可点击的状态"""
            time.sleep(1)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
            if ele == "doneItemNo":
                print("还没有挪动单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
            return ele

        @teststep
        def time_view(self):
            # 计时的时间

            ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

            print("现在做题的时间是：", ele)

        @teststep
        def again_arrow(self):
            # 再次点击按钮（两次按钮的元素是不一样的）
            time.sleep(2)
            ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
            if ele == "nextItem":
                print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

        @teststep
        def chick_answer(self):
            # 点击答案
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

        @teststep
        def wrong_again(self):
            # 错题再练
            time.sleep(2)
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

        @teststep
        def return_btn(self):
            # 返回
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        @teststep
        def again_restore(self):
            # 再来一遍
            self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

        @teststep
        def drag_paper(self):
            # 考试的连词成句想有滑动出发按钮
            Swipe().swipe_right_paper(1000)

    class WordListen:
        """闪卡练习"""

        def __init__(self, driver):
            self.driver = driver

        def wait_check_page(self):
            """以“title:闪卡练习”的xpath-index为依据"""
            locator = (By.XPATH, "//android.widget.TextView[contains(@index,1)]")
            element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(locator))[0]
            return element[0].text

        def flash_card_copy(self):
            """闪卡练习--抄写模式"""

    class GuessWord:
        """猜词游戏"""

        def guess_word(self):
            """猜词游戏"""
            # TODO 猜词游戏

    class VocabularySelection:
        """词汇选择"""

        def vocabulary_selection(self):
            """词汇选择"""
            # TODO 词汇选择

    @teststep
    def arrow(self):
        #点金前进的那个箭头
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()
    # 点击喇叭
    def clcik_voice(self):
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
        print("点击喇叭，但是发生准确与否还不能判断")

    @teststep
    def again_arrow(self):
        #还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s"%ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def word_spelling_text(self):
        #单词拼写的text

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text

        return ele

    @teststep
    def word_spelling_write(self):
        #单词拼写的text

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[4].text

        return ele

    @teststep
    def word_YB(self):
        word = yb_letter(self.word_spelling_text())

        games_keyboard(self, word)
        print("这个单词是", word)

    @teststep
    def word_write_YB(self):
        # 这个是单词拼写的默写模式
        word = yb_letter_write(self.word_spelling_write())

        games_keyboard(self, word)
        print("这个单词是", word)

    @teststep
    def word_write_ew(self):
        # ew 是bug点不了特殊处理
        word = ["e","w"]
        for i in range(len(word)):
            games_keyboard(self,word[i])

        print("这个单词是",word)

    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)

    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("结束做题的时间是：",ele)

    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def return_btn(self):
        #点击返回
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
        time.sleep(1)

    @teststep
    def wrong_problem(self):
        #点击错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def again_practice(self):
        #点击错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()





class FlashCard(BasePage):
    """闪卡练习"""

    #我们点击闪卡游戏的框
    @teststep
    def flash_bound_num(self):
        obj = Homework().flash_type_study()
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="15"]').text
        time.sleep(2)
        return element

    @teststep
    def max_number_YB(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        time.sleep(2)
        return element

    def max_number_reconstruction(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element
    def max_number_reconstruction1(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def flash_study(self):
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="中考精华词汇 基础版65（学习模式）"]').text
        m = re.match(".*\（(.*)\）.*", element)
        return m.group(1)

    @teststep
    def chick_blank(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="FlashcardChange"]').click()
        time.sleep(2)
    @teststep
    def chick_blank_single(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="FlashcardChangeNo"]').click()
        time.sleep(2)
    @teststep
    def chick_flash_study(self):
    #我们点击的那个框

    # def chick_flash_bound(self):
    #     obj = Homework(self.driver).flash_type_study()
    #     print(obj)
    #     bounds = obj.location

        # x = bounds['x']
        # y = bounds['y']
        time.sleep(2)
        loc_x = 180
        loc_y = 285
        click_bounds(self, loc_x, loc_y)

    @teststep
    def flash_study_YB(self):
        """以YB模式的xpath为标准"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（学习模式）"]').click()

    @teststep
    def flash_study_reconstruction(self):
        """以xpath为标准"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（学习模式）（引用1）"]').click()
    @teststep
    def flash_study_reconstruction1(self):
        """以xpath为标准"""
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（学习模式）"]').click()
    @teststep
    def arrow(self):
        #点金前进的那个箭头
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def word_explain(self):
        # 以及解释

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print('闪卡模式双面的英文单词，单词是',ele)
        return ele

    @teststep
    def word_explain1(self):
        # 以及解释

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text
        print('闪卡模式双面的中文解释，单词是',ele)
        return ele

    @teststep
    def word(self):
        # 英文单词
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print('在双面模式下的英文的单词',ele)
        return ele

    def explanation(self):
        # 中文解释

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print('在双面模式下的中文的解释', ele)
        return ele


    @teststep
    def again_arrow(self):
        #还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
        time.sleep(3)
        self.driver.find_element_by_xpath('	//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def again_study(self):
        #点击在学一边
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="再学一遍 Study again"]').click()

    @teststep
    def mark_again(self):
        #点击标记内容在学一遍
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="标记⭐️内容再练一遍"]').click()

    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def click_star(self):
        #点击星星
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()

    @teststep
    def click_card(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="changeNo"]').click()

    @teststep
    def return_btn(self):
        #点击返回
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

class Flash_copy(BasePage):

    #我们点击闪卡游戏的框
    @teststep
    def flash_bound_num(self):
        obj = Homework().copy_type_study()
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="10"]').text
        time.sleep(2)
        return element

    @teststep
    def max_number_copy_YB(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        time.sleep(2)
        return element

    @teststep
    # def max_number_copy_(self):
    #     # 获取我们需要填写的题的个数
    #     number = []
    #     element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
    #     time.sleep(2)
    #     for i in range(len(element)):
    #         number.append(element[i].text)
    #     print("这个页面的所有的name属性是",number)
    #     return number
    @teststep
    def max_number_copy_reconstruction(self):
        #获取我们需要填写的题的个数

        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def copy_study(self):
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="马承同步三上 lesson2 闪卡练习（抄写模式）（引用1）"]').text
        print(element)
        m = re.findall("抄写模式", element)
        name = m[0]
        return name

    @teststep
    def word(self):
        """闪卡练习- 抄写模式 内展示的Word"""
        ele = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[2]

        return ele

    @teststep
    def voice(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

    @teststep
    def chick_flash_study(self):

        loc_x = 180
        loc_y = 285
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)

    @teststep
    def copy_flash(self):

        max_num = self.max_number()
        # 获取到我们需要的最大的题数

        for i in range(0,int(max_num)-6):
            word = list(self.word().text)

            self.voice()
            time.sleep(2)
            self.click_star()
            print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
            for j in range(len(word)):

                games_keyboard(self,word[j])
            time.sleep(4)

        word_list = ["o","k"]
        self.voice()
        time.sleep(2)
        self.click_star()
        for k in range(len(word_list)):

            games_keyboard(self,word_list[k])
            time.sleep(3)


    @teststep

    def copy_flash_fun(self):



        for q in range(0, 5):
            word = list(self.word().text)

            self.voice()
            time.sleep(2)
            self.click_star()
            print("第几题：%s" % (q + 1), "单词是:%s" % self.word().text)
            for w in range(len(word)):
                games_keyboard(self, word[w])
            time.sleep(3)


    @teststep

    def copy_flash_YB(self):
        big_C = 'c'
        max_num = self.max_number_copy_YB()
        # 获取到我们需要的最大的题数

        for i in range(0,2):
            word = list(self.word().text)
            time.sleep(2)
            self.voice()
            time.sleep(2)
            self.click_star()
            print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
            for j in range(len(word)):
                games_keyboard(self,word[j])
            time.sleep(4)
        self.voice()
        time.sleep(2)
        self.click_star()
        games_keyboard(self,big_C)
        time.sleep(3)
        for i in range(0,int(max_num)-3):
            word = list(self.word().text)
            time.sleep(2)
            self.voice()
            time.sleep(2)
            self.click_star()
            print("第几题：%s" % (i + 1), "单词是:%s" % self.word().text)
            for j in range(len(word)):
                games_keyboard(self,word[j])
            time.sleep(4)

    def copy_flash_reconstruction(self):
        i = 0

        max_num = int(self.max_number_copy_reconstruction())
        # self.max_number_copy_()
        # 获取到我们需要的最大的题数

        for i in range(0,max_num):

            max_num = int(self.max_number_copy_reconstruction())
            i = i+1
            print("进入第%d题,我们需要完成的小题的数目%d"% (i,max_num) )
            word = list(self.word().text)
            time.sleep(2)
            self.voice()
            time.sleep(2)
            self.click_star()
            print("第几题：%s" % (i), "单词是:%s" % self.word().text)
            for j in range(len(word)):
                games_keyboard(self,word[j])
            print("输入正确，两秒之后自动跳转到下一题")
            time.sleep(4)

    def copy_flash_reconstruction1(self):
        i = 0

        max_num = int(self.max_number_copy_reconstruction())
        # self.max_number_copy_()
        # 获取到我们需要的最大的题数

        for i in range(0, max_num):

            max_num = int(self.max_number_copy_reconstruction())
            i = i + 1
            print("进入第%d题,我们需要完成的小题的数目%d" % (i, max_num))
            word = list(self.word().text)
            time.sleep(2)
            self.voice()
            time.sleep(2)

            print("第几题：%s" % (i), "单词是:%s" % self.word().text)
            for j in range(len(word)):
                games_keyboard(self, word[j])
            print("输入正确，两秒之后自动跳转到下一题")
            time.sleep(4)


    @teststep
    def copy_type_study_yb(self):
        # YB模式下的闪卡练习的抄写模式
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（抄写模式）"]').click()

    @ teststep
    def copy_type_study_reconstruction(self):
        # 重构下的闪卡练习的抄写模式
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（抄写模式）"]').click()

    @teststep
    def arrow(self):
        #点金前进的那个箭头
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def again_arrow(self):
        #还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
        self.driver.find_element_by_xpath('	//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def again_study(self):
        #点击在学一边
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="再学一遍 Study again"]').click()

    @teststep
    def mark_again(self):
        #点击标记内容在学一遍
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="标记⭐️内容再练一遍"]').click()
    @teststep
    def click_star(self):
        #点击星星
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()
    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def click_star(self):
        #点击星星
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="fccollectionNo"]').click()

    @teststep
    def return_btn(self):
        #点击返回
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

class Strengthen_sentence(BasePage):
     #强化炼句
    @teststep
    def click_strengthen_self(self):
        # 点击自定义模式下的强化炼句
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（自定义模式）"]').click()

    @teststep
    def click_strengthen_write(self):
         # 点击自定义模式下的强化炼句
         self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（默写模式）"]').click()

    @teststep
    def click_strengthen_complex(self):
         # 点击自定义模式下的强化炼句
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（复杂模式）"]').click()

    @teststep
    def click_strengthen_simple(self):
         # 点击自定义模式下的强化炼句
         self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（简单模式）"]').click()


    @teststep
    def strengthen_bound_num(self, index):
        obj = Homework().strengthen_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def max_number(self):
        #获取我们需要填写的题的个数
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="4"]').text
        time.sleep(2)
        return element

    @teststep
    def silent_max_num(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["s"]
        word = list(ele)
        for i in range(len(word)):

            games_keyboard(self, word[i])
            print("我们填写字母是",word[i])


    @teststep
    def horizontal_line(self):
     # 点击横线

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')

        return ele

    @teststep
    def horizontal_line_paper(self):
     # 点击横线

     self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

    @teststep
    def horizontal_line_1(self):
        #点击横线
        self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

    def horizontal_line_2(self):
        #点击横线2

        self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()

    @teststep
    def arrow(self):
        #点击那个前进的按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def again_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def chick_answer(self):
        #点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def wrong_again(self):
        #错题再练
        time.sleep(5)

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()
        # 点击喇叭

    @teststep
    def clcik_voice(self):
     self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
     print("点击喇叭，但是发生准确与否还不能判断")
    @teststep
    def return_btn(self):
        #返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def grey_btn(self):
     """灰色按钮是不可点击的状态"""
     time.sleep(1)
     ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
     if ele == "doneItemNo":
         print("还没有输入单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
     return ele
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)
class Match_exerciser(BasePage):
    #连连看

    @teststep
    def match_bound_num(self, index):
        #点击框的位置
        obj = Homework().match_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def max_number(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="8"]').text
        time.sleep(2)
        return element

    @teststep
    def max_number_YB(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def chick_answer(self):
        #点击答案
        time.sleep(5)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)

    @teststep
    def clcik_voice(self):
        # 点击声音
        time.sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
        print("点击喇叭，但是发生准确与否还不能判断")

    @teststep
    def again(self):
        #点击再练一遍
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()
        time.sleep(3)

    @teststep
    def return_btn(self):
        #返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def quite(self):
        #点击quite这个单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="quiet"]').click()

    @teststep
    def re_quite(self):
        #点击quite这个英文单词、
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="安静的"]').click()

    @teststep
    def student(self):
        #点击学生这个单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="student"]').click()

    @teststep
    def re_student(self):
        #点击学生这个中文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="学生"]').click()

    @teststep
    def mr(self):
        #点击mr这个英文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Mr."]').click()

    @teststep
    def re_mr(self):
        #点击mr这个中文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="先生"]').click()

    @teststep
    def teacher(self):
        #点击老师这个英文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="teacher"]').click()

    @teststep
    def re_techer(self):
        #点就教师这个中文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="教师"]').click()

    @teststep
    def mrs(self):
        #点击女士这个英文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Mrs."]').click()

    @teststep
    def re_mrs(self):
        #点击女士这个中文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="女士；夫人"]').click()

    @teststep
    def doctor(self):
        #点击英文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doctor"]').click()

    @teststep
    def re_doctor(self):
        #点击中文这个单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="医生"]').click()

    @teststep
    def beside(self):
        #点击beside
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="beside"]').click()

    @teststep
    def re_beside(self):
        #点击中文在。。。身边
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="在……旁边"]').click()

    @teststep
    def nurse(self):
        #点击护士这个英文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nurse"]').click()

    @teststep
    def re_nurse(self):
        #点击护士这个中文单词
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="护士"]').click()

    @teststep
    def list1(self):

        word1_list = ["/ɑ/","/ɜ/","/ɔ/","/ð/","/ə/"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range (len(word1_list)):

            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = yb_letter_select(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            time.sleep(2)

    @teststep
    def list2(self):
        word1_list = ["/ɒ/","/g/","/ʊ/",'/ɪ/',"/θ/"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range(len(word1_list)):
            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = yb_letter_select(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            time.sleep(2)

    @teststep
    def list3(self):
        word1_list = ["/ʃ/", "/ʌ/", "/ʒ/", "/ɛ/", "/ŋ/"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range(len(word1_list)):
            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = yb_letter_select(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            time.sleep(2)

    @teststep
    def list4(self):
        word1_list = ["/æ/", "/ˈ/"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range(len(word1_list)):
            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = yb_letter_select(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            time.sleep(2)

    @teststep
    def time_view(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("现在做题的时间是：", ele)
    @teststep
    def list_re(self):
        word1_list = ["Apple", "Hello","like","over"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range(len(word1_list)):
            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            print("这里面的序号是",index)
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = vob_operate(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            self.time_view()
            time.sleep(2)

    @teststep
    def list_again(self):
        word1_list = ["like is", "but"]

        all_list = []
        # 这个是单词和解释的列表
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # 遍历这个列表
        for i in range(len(ele)):
            # 把这个列表的text属性提取出来然后添加到一个新的列表里面
            all_list.append(ele[i].text)
        print("所有列表的内容是", all_list)
        for j in range(len(word1_list)):
            index = [i for i, x in enumerate(all_list) if x == word1_list[j]][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index].click()
            value = vob_operate(word1_list[j])
            time.sleep(2)
            print(value)
            index2 = [i for i, x in enumerate(all_list) if x == value][0]
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[index2].click()
            self.time_view()
            time.sleep(2)




class Listen_practice(BasePage):
    #作业之听力练习

    @teststep
    def wait_read(self):
        # 以阅读理解的xpath为依据，然后用里面的text进行判断，是否进入到这一页
        element = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="听力练习"]').text
        return element

    @teststep
    def back_btn(self):
        #左上角的返回按钮，以xpath作为依据
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

    @teststep
    def listen_num(self):
        # 拿到我们需要做的题的个数
        element = self.driver.find_elements_by_class_name("XCUIElementTypeStaticText")[1].text
        return element

    @teststep
    def listen_bound_num(self, index):
        obj = Homework().listen_practice_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置",loc_x,loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def listen_option_button(self,i):
        """获取四个选项"""
        ele = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="A"]')[i]
        # print("答案的列表",len(ele))

        return ele

    @teststep
    def listen_speaker(self):
        #听力的那个喇叭
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：",ele)

    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)
    #这个是我们的箭头的按键
    @teststep
    def listen_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').text
        if ele == "doneItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    #点击再练一边
    @teststep
    def practice_again(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()
        time.sleep(5)
    #点击查看答案'
    @teststep
    def check_answer(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()


class Guess_game(BasePage):
    # 猜词游戏

    @teststep
    def guess_bound_num(self, index):
        obj = Homework().guess_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置", loc_x, loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def guess_listen_YB(self):
        #YB模式下的人猜词游戏有发音
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（有发音）"]').click()

    @teststep
    def guess_listen(self):
        #YB模式下的人猜词游戏有发音
        time.sleep(2)

        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（有发音）"]').click()

    @teststep
    def guess_no_listen(self):
        #YB模式下的人猜词游戏有发音
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="兼职测试题（无发音）"]').click()

    @teststep
    def guess_no_listen_YB(self):
        #YB模式下的猜词游戏无发音
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="设置YB（无发音）"]').click()

    @teststep
    def guess_max_num(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').text
        time.sleep(2)
        return element

    @teststep
    def guess_max_listen(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("结束做题的时间是：",ele)

    @teststep
    def guess_max_YB_num(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        time.sleep(2)
        return element

    @teststep
    def guess_max_YB_no_num(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="18"]').text
        time.sleep(2)
        return element

    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["q","w","e","r","t","y","u","i","o","p"]
        word = list(ele)
        for i in range(len(word)):
            guess_keyboard(self, word[i])


    @teststep
    def word_YB(self):

        word = yb_letter(self.guess_write())

        guess_keyboard(self, word)
        print("这个单词是", word)

    @teststep
    def word_correct(self):
        """填写正确的单词的方法"""
        word = reconstruction_guess(self.guess_write())
        for i in range(len(word)):

            guess_keyboard(self, word[i])
        print("输入的这个单词是", word)

    @teststep
    def word_no_list_YB(self):

        word = yb_guess(self.guess_write())

        guess_keyboard(self, word)
        print("这个单词是", word)

    @teststep
    def guess_word(self):

        """这里需要用到小键盘 内展示的Word"""
        ele = [ "e", "w"]
        ele = [ "e", "w"]
        word = list(ele)
        for i in range(len(word)):
            guess_keyboard(self, word[i])

    @teststep
    def guess_word_apple(self):

        """这里需要用到小键盘 内展示的Word"""
        ele = [ "a", "p","p","l","e"]

        word = list(ele)
        for i in range(len(word)):
            guess_keyboard(self, word[i])

    @teststep
    def guess_write(self):
        #单词拼写的text

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[3].text

        return ele



    # def guess_write_no_listen(self):
    #     #单词拼写的text
    #     word = []
    #     ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
    #     for i in range(len(ele)):
    #         word.append(ele[i].text)
    #
    #     print("单词列表",word)

        # return ele

    @teststep
    def horizontal_line(self):
        # 点击横线
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')
        print("列表的个数和列表", len(ele), ele)

        return ele

    @teststep
    def horizontal_line_1(self):
        # 点击横线
        self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()

    @teststep
    def horizontal_line_2(self):
        # 点击横线2

        self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()

    @teststep
    def arrow(self):
        # 点击那个前进的按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def again_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    # 点击喇叭
    @teststep
    def clcik_voice(self):
        self.driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="audio wq"])[1]').click()
        print("点击喇叭，但是发生准确与否还不能判断")
    @teststep
    def chick_answer(self):
        # 点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def letter(self):
        # 点击的字母 下标是1～26
        letter = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        for i in range(10):
            ele[random.randint(1, len(ele) - 1)].click()
        # for i in range(len(ele)):
        #     letter.append(ele[i].text)
        # print("点击的字母的列表",letter)
        # return letter
        return ele


    @teststep
    def wrong_again(self):
        # 错题再练
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def again_exercise(self):
        # 错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

    @teststep
    def return_btn(self):
        # 返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

class Restore_words(BasePage):
    # 还原单词

    @teststep
    def restore_bound_num(self, index):
        obj = Homework().restore_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置", loc_x, loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def restore_max_num(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        print("题目序号",element)
        time.sleep(2)
        return element

    @teststep
    def word(self):

        """这里需要用到小键盘 内展示的Word"""
        ele = ["q","w","e","r","t","y","u","i","o","p"]
        word = list(ele)
        for i in range(len(word)):
            guess_keyboard(self, word[i])

    @teststep
    def sound(self):
        #点击声音
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()
    @teststep
    def text(self):
        """全部的列表的数据"""
        list = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            list.append(ele[i].text)
        print("这页全部的数据是",list)
        return list

    @teststep
    def drag(self):
        Swipe().swipe_up_restore(1000)

    @teststep
    def drag1(self):
        Swipe().swipe_up_restore1(1000)

    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("结束做题的时间是：",ele)


    @teststep
    def arrow(self):
        # 点击那个前进的按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def show_word(self):
        # 显示内容的列表
        word = []
        ele =  self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("我们的单词的列表是",word)
        return word
    @teststep
    def word_text(self):
        # 显示内容的列表

        ele =  self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[5].text
        print("我们显示的单词是",ele)
        return ele

    @teststep
    def again_arrow(self):
        # 还要点击的那个箭头但是两次箭头的xpath不是一个很神奇
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有挪动单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s"%ele)
        return ele

    @teststep
    def chick_answer(self):
        # 点击答案
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def wrong_again(self):
        # 错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def return_btn(self):
        # 返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

class Sentence_conversion(BasePage):
    # 句型转换

    @teststep
    def sentence_bound_num(self, index):
        obj = Homework().sentence_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置", loc_x, loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def sentence_max_num(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element
    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有输入选项时灰色的按钮是不可点击的，灰色按钮的name属性是%s" % ele)

    @teststep
    def time_view_begin(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("开始做题的时间是：", ele)
    @teststep
    def time_view_end(self):
        # 计时的时间
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        print("结束做题的时间是：", ele)
    @teststep
    def choice_blanck_num(self):
        #这个是用来计算的
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        return ele

    @teststep
    def choice_blank(self,i):
        #拿到我们所有的答案的列表

        element = self.driver.find_elements_by_class_name('XCUIElementTypeButton')[i]

        return element

        # print('元素和个数',len(ele),ele)

    @teststep
    def words_num(self):
        l = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        for i in range(len(ele)):
            l.append(ele[i].text)
        print("这个列表的所有元素是",l)

        return ele

    @teststep
    def sound(self):
        #点击声音
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

    @teststep
    def drag(self):
        Swipe().swipe_up_restore(1000)

    @teststep
    def arrow(self):
        # 点击那个前进的按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()

    @teststep
    def again_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("输入全部单词之后按钮是可以点击的，可以点击的那么属性是%s"%ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def chick_answer(self):
        # 点击答案
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()
    @teststep
    def show_answer(self):
        # 显示的全部答案
        word = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            word.append(ele[i].text)
        print("正确的单词的列表是",word)
    @teststep
    def wrong_again(self):
        # 错题再练
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def return_btn(self):
        # 返回
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

class Conjunctions_sentence(BasePage):
    # 连词成句

    @teststep
    def conjunctions_bound_num(self, index):
        obj = Homework().conjunctions_type(index)
        print(obj)
        bounds = obj.location

        x = bounds['x']
        y = bounds['y']
        loc_x = x + 100
        loc_y = y
        print("点击的位置", loc_x, loc_y)
        click_bounds(self, loc_x, loc_y)
        time.sleep(2)

    @teststep
    def add_YB_restore(self):
        # 进入加YB还原单词的列表

        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="加YB还原单词"]').click()

    @teststep
    def conjunctions_max_num(self):
        time.sleep(2)
        element = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        time.sleep(2)
        return element

    @teststep
    def conjunctions_max_num_YB(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="17"]').text
        time.sleep(2)
        return element

    @teststep
    def word(self):
        """这里需要用到小键盘 内展示的Word"""
        ele = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        word = list(ele)
        for i in range(len(word)):
            guess_keyboard(self, word[i])

    @teststep
    def sound(self):
        # 点击声音
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="horn"]').click()

    @teststep
    def drag(self):
        Swipe().swipe_up_conjunctions(1000)

    @teststep
    def drag_re(self):
        Swipe().swipe_up_conjunctions_re(1000)

    @teststep
    def drag_YB(self):

        Swipe().swipe_up_restore(1000)

    @teststep
    def arrow(self):
        # 点击那个前进的按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItem"]').click()
    @teststep
    def grey_btn(self):
        """灰色按钮是不可点击的状态"""
        time.sleep(1)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="doneItemNo"]').text
        if ele == "doneItemNo":
            print("还没有挪动单词时灰色的按钮是不可点击的，灰色按钮的name属性是%s"%ele)
        return ele

    @teststep
    def time_view_begin(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("开始做题的时间是：",ele)
    @teststep
    def time_view_end(self):
        # 计时的时间

        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text

        print("结束做题的时间是：",ele)

    @teststep
    def again_arrow(self):
        # 再次点击按钮（两次按钮的元素是不一样的）
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').text
        if ele == "nextItem":
            print("挪动单词之后按钮是可以点击的，可以点击的那么属性是%s" % ele)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="nextItem"]').click()

    @teststep
    def chick_answer(self):
        # 点击答案
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="查看答案"]').click()

    @teststep
    def wrong_again(self):
        # 错题再练
        time.sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="错题再练"]').click()

    @teststep
    def return_btn(self):
        # 返回
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()
        time.sleep(1)

    @teststep
    def again_restore(self):
        # 再来一遍
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="再练一遍"]').click()

    @teststep
    def drag_paper(self):
        # 考试的连词成句想有滑动出发按钮
        Swipe().swipe_right_paper(1000)









class WordListen:
    """闪卡练习"""
    def __init__(self, driver):
        self.driver = driver

    def wait_check_page(self):
        """以“title:闪卡练习”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@index,1)]")
        element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(locator))[0]
        return element[0].text

    def flash_card_copy(self):
        """闪卡练习--抄写模式"""



class GuessWord:
    """猜词游戏"""

    def guess_word(self):
        """猜词游戏"""
        # TODO 猜词游戏


class VocabularySelection:
    """词汇选择"""

    def vocabulary_selection(self):
        """词汇选择"""
        # TODO 词汇选择
