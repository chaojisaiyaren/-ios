#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN FEIFEI


class DelEditText():
    def __init__(self, driver, edit_text):
        self.edit_text = edit_text
        self.driver = driver

    def del_text(self):
        self.edit_text.click()  # 激活该文本框
        self.edit_text.clear()
    #     context = self.edit_text.get_attribute('text')  # 获取文本框里的内容
    #     self.edit_text_clear(context)  # 删除文本框中是内容
    #
    # def edit_text_clear(self, text):
    #     """"
    #         清除EditText文本框里的内容
    #         @param:text 要清除的内容
    #     """
    #     self.driver.keyevent(123)
    #     for i in range(0, len(text)):
    #         self.driver.keyevent(67)
