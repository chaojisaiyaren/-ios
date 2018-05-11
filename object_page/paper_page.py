import re
import time

from utils.click_bounds import games_keyboard,click_bounds,guess_keyboard

from conf.basepage import BasePage
class Paper_page(BasePage):

    #试卷模块元素定位类

    #初始化属性


    def paper(self):
        # 点击进入试卷页面
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="试卷"]').click()

    def paper_list(self):
        # 点击试卷列表进入试卷
        #paper = []
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="译林牛津三起点六上 Unit6 单元测试卷（引用1）"]').click()

       # for i in range(len(ele)):
       #     paper.append(ele[i].text)
       # print("试卷列表",paper)
    def undone(self):
        time.sleep(2)
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="未完成"]').text
        return ele

    def verifi_paper(self):
        # 验证已经进入到了考试页面
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" 试卷 "]').text

        return  ele

    def click_paper(self):
        # 点击开始考试
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="开始考试"]').click()


    def paper_bound(self):
        #点击进入题目的选项

        x = 232
        y = 42


        click_bounds(self, x,y)

        # X掉考试
    def paper_close(self):

        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="close"]').click()

    def answer_sentence_text(self):
        # 进入强化句的条件
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="强化炼句"])[1]').text

        return ele
    # def all_topic_list(self):
    #     # 取到所有题的数量
    #     topic = []
    #     ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
    #     for i in range(len(ele)):
    #         topic.append(ele[i].text)
    #     print("试卷的所有Text是",topic)

    def topic_selection(self,index):
        # 参数化点击小题
        self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[index].click()

    def strengthen_text(self):
        # 强化炼句的name属性
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="强化炼句"])[1]').text
        return ele

    def strengthen_cycles(self):
        # 需要做的答题的题目数量
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="（共5题）"])[1]').text
        num = re.search(r'\d+', ele)
        return num.group()

    def conjunctions_sentence_text(self):
        # 连词成句的的name属性
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="连词成句"]').text
        return ele

    def conjunctions_sentence_cycles(self):
        # 连词成句需要做法的题目的数量
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="（共5题）"])[1]').text
        num = re.search(r'\d+', ele)
        return num.group()

    def single_text(self):
        # 单项选择的name属性
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="单项选择"])[1]').text
        return ele

    def single_cycles(self):
        # 单项选择需要做的题目的数量
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="（共5题）"])[2]').text
        num = re.search(r'\d+', ele)
        return num.group()

    def single_second_cycles(self):
        # 单项选择需要做的题目的数量
        ele = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="（共4题）"]').text
        num = re.search(r'\d+', ele)
        return num.group()

    def all_list(self):
        l = []
        ele = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        for i in range(len(ele)):
            l.append(ele[i].text)
        print("页面的所有数据为",l)
        return ele

    def read_comprehension(self):
        # 阅读理解的name属性
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="阅读理解"])').text
        return ele

    def read_cycles(self):
        # 需要做的答题的题目数量
        ele = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="（共5题）"])[3]').text
        num = re.search(r'\d+', ele)
        return num.group()


    def paper_reback(self):
        # 点击返回按钮
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="返回"]').click()

        #点击确定
    def sure(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="确定"]').click()

    def sure_cencl(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="取消"]').click()