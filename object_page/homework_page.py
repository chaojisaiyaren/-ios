#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN FEIFEI
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.screen_swipe import Swipe


class Homework:
    """作业包内 作业列表页面 元素信息"""
    def __init__(self, driver):
        self.driver = driver

    def homework_name(self, index):
        """抬头： 作业包的名称 、老师名 & 作业模式"""
        item = self.driver \
            .find_elements_by_class_name("android.widget.TextView")[index].text
        return item

    def imgames_type(self):
        """小游戏数目 """
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_type")
        return item

    def games_title(self):
        """小游戏title """
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_name")
        return item

    def tv_testbank_type(self, index):
        """小游戏类型"""
        item = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_type")[index].text
        return item

    def tv_testbank_name(self, index):
        """小游戏模式--匹配小括号内游戏模式"""
        item = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_name")[index].text
        m = re.match(".*\（(.*)\）.*", item)
        return m.group(1)

    def status(self):
        """题目状态"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_status")
        return item

    def count(self):
        """题目总数格式：共X题"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_testbank_count")
        return item

    def rank_icon(self):
        """排行榜icon"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_ranking")
        return item

    # 以下为排行榜页面元素
    def wait_check_rank_page(self):
        """以“title:排行榜”的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@index,1)]")
        element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        return element.text

    def class_name(self):
        """班级名称"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_title")
        return item

    def text_view(self):
        """所有排行榜TextView元素总数-包括班级名称+list条目"""
        item = self.driver \
            .find_elements_by_xpath("//android.support.v7.widget.RecyclerView/*/android.widget.TextView")
        return item

    def rank_index(self, index):
        """排名"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_index")[index].text
        return item

    def student_icon(self, index):
        """头像"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_student_icon")[index].text
        return item

    def student_name(self, index):
        """学生昵称"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_student_name")[index].text
        return item

    def accuracy_rate(self):
        """准确率最高的那次的正确率"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_accuracy")
        return item

    def spend_time(self, index):
        """准确率最高的那次 完成所用时间"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_spend_time")[index].text
        return item

    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton").click()

    def back_up(self):
        """从排行榜页面返回到作业list"""
        j = 0
        while j < 2:
            self.back_up_button()  # 结果页 返回按钮
            j += 1

    def swipe_screen(self, game_type):
        """小游戏页面滑屏"""
        item_1 = self.games_title()
        last_one = item_1[len(item_1) - 1].text  # 滑动前页面内最后一个小游戏title

        Swipe(self.driver).swipe_up(1000)
        item_2 = self.games_title()  # 滑动后页面内小游戏
        if item_2[len(item_2) - 1].text == last_one:
            print('到底啦', last_one)
            self.back_up_button()
        else:  # 滑动后到底，因为小游戏list最多只有两页，滑动一次即可到底
            print('滑动后到底，因为小游戏list最多只有两页，滑动一次即可到底')
            j = []
            for i in range(0, len(item_2)):
                if item_2[i].text == last_one:
                    j.append(i)
                    for index in j:
                        print('index:', index)
                        self.games_count(index, game_type)

    def games_count(self, index, game_type):
        """该类型小游戏的数量"""
        item = self.games_type()  # 页面内小游戏数目
        print('game_type:', index, game_type)
        count = []  # 单项选择 - 小游戏数目
        for i in range(index, len(item)):
            var = self.tv_testbank_type(i)  # 获取小游戏类型
            if var == game_type:
                count.append(i)
        print('小游戏 index:', count, len(count), '个')
        return count

    def content(self):
        """小游戏条目展示内容"""
        title = []
        for i in range(2):
            title.append(self.homework_name(i))
        print('小游戏抬头内容:', title)

        count = self.games_type()
        for j in range(len(count)):
            game_type = self.tv_testbank_type(j)
            game_status = self.status()[j].text
            count = self.count()[j].text
            icon = self.rank_icon()[j]
            print('小游戏条目内容:', game_type, game_status, count, icon)

    # 以下为排行榜功能
    def ranking(self, index, nickname):
        """排行榜icon"""
        status = self.status()[index].text
        print(status)
        self.rank_icon()[index].click()
        if self.wait_check_rank_page():  # 排行榜页面检查点
            class_name = self.class_name()
            for i in range(len(class_name)):
                print('班级：', class_name[i].text)
                if status == '未开始':
                    self.ranking_no_start(class_name, nickname)  # 排行榜 昵称
                else:
                    global own_info
                    own_info = self.ranking_list(i, class_name, nickname)
                print('============================================')
            self.back_up_button()
        else:
            print('未进入结果页')
        return own_info

    def list_item(self, class_name):
        """排行榜list条目内容"""
        class_count = []
        text_view = self.text_view()
        for j in range(len(class_name)):
            for i in range(len(text_view)):
                if text_view[i].text == class_name[j].text:
                    class_count.append(i)
        print(class_count)
        return class_count, text_view

    def ranking_no_start(self, class_name, nickname):
        """题目状态：未开始"""
        for i in range(len(class_name)):
            rank_name = self.student_name(i)  # 昵称
            if rank_name == nickname:  # todo 未开始状态时，排行榜条目不应出现本人信息
                print('Error--题目状态：未开始')
            else:
                print('题目状态：未开始 - no error')

    def info_statistic(self, i, class_name):
        """名次、昵称、最优准确率、所用时间各生成一个list"""
        a = 0
        rank_index = []  # 排名
        rank_name = []  # 昵称
        rank_rate = []  # 最优准确率
        rank_time = []  # 所用时间 - 带格式 xx:xx
        mat = []  # 所用时间 - 不带格式 xxxx
        text = []

        info = self.list_item(class_name)
        if i+1 < len(class_name):
            for index in range(info[0][i]+1, info[0][i+1]):
                text.append(info[1][index].text)
            print(info[0][i] + 1, info[0][i + 1], text)
        else:
            for index in range(info[0][i]+1, len(info[1])):
                text.append(info[1][index].text)
            print(info[0][i] + 1, len(info[1]), text)
        while a < len(text):  # 名次、昵称、最优准确率、所用时间各生成一个list
            rank_index.append(text[a])
            rank_name.append(text[a + 1])
            rank_rate.append(re.sub("\D", "", text[a + 2]))  # 最优准确率
            rank_time.append(text[a + 3])  # 带格式的时间 xxxx
            mat.append(re.sub("\D", "", text[a + 3]))  # 不带格式的时间 xx:xx
            a += 4
        return rank_index, rank_name, rank_rate, rank_time, mat

    def ranking_list(self, i, class_name, nickname):
        """排行榜列表的操作"""
        own_rate = []
        own_time = []
        item = self.info_statistic(i, class_name)
        for index in range(len(item[0])):
            if len(item[0]) > 1:  # 排行榜不只有一个人
                if item[1][index] == nickname:  # 本人
                    if index != 0:
                        if item[0][index] != 1:  # 说明不是第一名 - 排行榜不只有自己 且自己不是第一名，list第一条是自己的信息
                            print('本人成绩：', item[0][index], item[1][index], item[2][index] + "%", item[3][index])
                        else:  # 是第一名
                            print('Congratulations排行榜排名第一   成绩：', item[2][index] + "%", item[3][index])
                        own_rate.append(item[2][index])
                        own_time.append(item[3][index])
                else:  # 排行榜其他人
                    print(item[0][index], item[1][index], item[2][index] + "%", item[3][index])
            elif len(item[0]) == 1:  # 排行榜只有一个人
                print('排行榜只有一个人')
                if item[1][index] == nickname:  # 本人
                    print('本人成绩：', item[2][index] + "%", item[3][index])
                    own_rate.append(item[2][index])
                    own_time.append(item[3][index])
                else:
                    print('昵称 %s  成绩：%s %s', item[1][index], item[2][index] + "%", item[3][index])
            elif len(class_name) == 0:  # 排行榜暂无数据
                print('排行榜暂无数据')
            else:
                print('Error - 排行榜')

        print('检查排行榜排序:', item[0], item[2], item[4])
        for z in range(len(item[0])):
            if len(item[0]) > 1:  # 排行榜不只有一个人
                print('z:', item[0][0], z)
                if item[0][0] != 1:  # 不是第一名
                    if z != 0 and z+1 <= len(item[0])-1:  # 排除第一条信息
                        print('不是第一名 且 排除第一条信息:', z, item[2][z], item[4][z])
                        self.check_ranking(z, item[2], item[4])
                else:    # 是第一名
                    if z+1 <= len(item[0])-1:
                        print('是第一名:', z, item[2][z], item[4][z])
                        self.check_ranking(z, item[2], item[4])
            else:  # 排行榜只有一个人
                print('排行榜只有自己:', item[2][z], item[4][z])
        print('own_rate, own_time:', own_rate, own_time)
        return own_rate, own_time, class_name

    def check_ranking(self, j, rank_rate, rank_time):
        """排行榜排序逻辑检查"""
        print(rank_rate, rank_time)
        if rank_rate[j] > rank_rate[j + 1]:
            print('准确率高')
        elif rank_rate[j + 1] == rank_rate[j]:  # 准确率相等
            print(rank_time[j], rank_time[j + 1])
            if rank_time[j + 1] > rank_time[j]:  # 比较时间
                print('所用时间短')
            elif rank_time[j + 1] == rank_time[j]:
                print('准确率&所用时间均相同')
            else:
                print('排名逻辑有问题 - 所用时间')
        else:
            print('排名逻辑有问题 - 准确率')

