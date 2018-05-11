#!/usr/bin/env python
# encoding:UTF-8


def get_size(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']

    return x, y



def click_bounds(self, location_x, location_y, screen_x = 375, screen_y = 667):
    # 获取当前手机屏幕大小X,Y
    screen = get_size(self)
    # 设定系数
    a = location_x / screen_x
    b = location_y / screen_y

    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    self.driver.tap([(a * screen[0], b * screen[1])])




def games_keyboard(self, key):
    """小键盘 q w e等字母"""
    #yellow----ewfftq
    #qqffqq    ure

    screen = get_size(self)
    key = key.lower()
    keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'd', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    if key in keyboard:
        i = keyboard.index(key.lower())

        if i < 10:
            # print("字母index1:", i)
            # click_bounds(self, 0.08888 * screen[0] + 0.011 * screen[0]*(i+1), 1002) # 1002.5=970 + 47/2 + 9
            click_bounds(self, 20 + i * 36, 483)
        elif i in range(10, 19):
            # print("字母index2:", i, i - 9)
            # click_bounds(self, (0.08888+0.011) * screen[0] * (i - 9), 1080)  # =1002+ 47 +31
            click_bounds(self, 40 + (i-10) * 36, 536)
        elif i in range(19, 26):
            # print("字母index3:", i, i - 17)
            # click_bounds(self, (0.08888+0.011) * screen[0] * (i - 17), 1158)  # 1080 + 47 +31
            click_bounds(self, 77 + (i - 19) * 37, 586)
def guess_keyboard(self, key):
    """小键盘 q w e等字母"""
    #yellow----ewfftq
    #qqffqq    ure

    screen = get_size(self)
    keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'd', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    if key in keyboard:
        i = keyboard.index(key.lower())

        if i < 10:

            # click_bounds(self, 0.08888 * screen[0] + 0.011 * screen[0]*(i+1), 1002) # 1002.5=970 + 47/2 + 9
            click_bounds(self, 20 + i * 37, 527)
        elif i in range(10, 19):

            # click_bounds(self, (0.08888+0.011) * screen[0] * (i - 9), 1080)  # =1002+ 47 +31
            click_bounds(self, 40 + (i-10) * 38, 589)
        elif i in range(19, 26):

            # click_bounds(self, (0.08888+0.011) * screen[0] * (i - 17), 1158)  # 1080 + 47 +31
            click_bounds(self, 77 + (i - 19) * 37, 640)

