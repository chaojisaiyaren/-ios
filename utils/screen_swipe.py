from conf.basepage import BasePage
class Swipe(BasePage):
    """swipe screen"""

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_left(self, duration):
        """向左侧滑动"""
        screen = self.get_size()
        x1 = int(screen[0] * 0.75)
        y1 = int(screen[1] * 0.5)
        x2 = int(screen[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def swipe_right(self, duration):
        """向右侧滑动"""
        screen = self.get_size()
        x1 = int(screen[0] * 0.25)
        y1 = int(screen[1] * 0.5)
        x2 = int(screen[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def swipe_right_paper(self, duration):
        # 考试的页面向右侧滑动，Y值不变但是x值增大
        self.driver.swipe(182, 191, 327, 191, duration)

    def swipe_up(self, duration):
        """向上滑动"""
        screen = self.get_size()
        x1 = int(screen[0] * 0.5)
        y1 = int(screen[1] * 0.75)
        y2 = int(screen[1] * 0.25)
        self.driver.swipe(x1, y1, x1, -y2, duration)

    def swipe_down(self, duration):
        """向下滑动"""
        screen = self.get_size()
        x1 = int(screen[0] * 0.5)
        y1 = int(screen[1] * 0.25)
        y2 = int(screen[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, duration)
        print(x1,y1,y2)

    def swipe_up_bottom(self,duration):
        screen = self.get_size()
        x1 = 170
        y1 = 520
        y2 = -250
        self.driver.swipe(x1,y1,x1,y2,duration)
        print((x1,y1,y2))

    def swipe_up_restore(self, duration):
        #还原单词
        """向上滑动"""

        self.driver.swipe(190, 360, -100, 360, duration)

    def swipe_up_restore1(self, duration):
        # 还原单词
        """向上滑动"""

        self.driver.swipe(215, 382, -100, 382, duration)

    def swipe_up_conjunctions(self, duration):
        #连词成句
        """向上滑动"""

        self.driver.swipe(208, 275, 208, -300, duration)

    def swipe_up_conjunctions_re(self, duration):
        #连词成句
        """向上滑动"""

        self.driver.swipe(250, 242, -100, 242, duration)

    def swipe_up_flash(self, duration):
        # 连词成句
        """向上滑动"""

        self.driver.swipe(336, 324, -300, 324, duration)