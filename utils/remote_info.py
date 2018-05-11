#!/usr/bin/env python
# encoding:UTF-8
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class RemoteInfo:
    def remote_info_511(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['deviceName'] = '127.0.0.1'
        # desired_caps['app'] = PATH('..\\student_debug_1.1.7.apk')
        # desired_caps['appPackage'] = "com.vanthink.student.debug"
        # desired_caps['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
        # desired_caps["automationName"] = "uiautomator2"
        # desired_caps["unicodeKeyboard"] = True
        # desired_caps["resetKeyboard"] = True
        desired_caps = {"platformName": "iOS",
                "deviceName": "iPhone 6",
                "app": "/Users/work/Vanthink_stu_test.app",
                "platformVersion": "11.2",

                }
        # desired_caps["platformName"] = "iOS"
        #
        # desired_caps["deviceName"] = "iPhone 6"
        # desired_caps["app"] = "/Users/work/Vanthink_stu_test.app",
        # desired_caps["platformVersion"] = "11.2"

        print(desired_caps)
        return desired_caps

    def remote_info_510(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['deviceName'] = '127.0.0.1'
        # desired_caps['app'] = PATH('..\\student_debug_1.1.7.apk')
        # desired_caps['appPackage'] = "com.vanthink.student.debug"
        # desired_caps['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
        # desired_caps["automationName"] = "uiautomator2"
        # desired_caps["unicodeKeyboard"] = True
        # desired_caps["resetKeyboard"] = True
        desired_caps = {"platformName": "iOS",
                "deviceName": "iPhone 6",
                "app": "/Users/work/Vanthink_tea_test.app",
                "platformVersion": "11.3",

                }
        # desired_caps["platformName"] = "iOS"
        #
        # desired_caps["deviceName"] = "iPhone 6"
        # desired_caps["app"] = "/Users/work/Vanthink_stu_test.app",
        # desired_caps["platformVersion"] = "11.2"

        print(desired_caps)
        return desired_caps

def remote_info_511():
    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1.1'
    # desired_caps['deviceName'] = '127.0.0.1'
    # desired_caps['app'] = PATH('..\\student_debug_1.1.7.apk')
    # desired_caps['appPackage'] = "com.vanthink.student.debug"
    # desired_caps['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
    # desired_caps["automationName"] = "uiautomator2"
    # desired_caps["unicodeKeyboard"] = True
    # desired_caps["resetKeyboard"] = True
    desired_caps = {"platformName": "iOS",
            "deviceName": "iPhone 6",
            "app": "/Users/work/Vanthink_stu_test.app",
            "platformVersion": "11.3",
            "automationName":"XCUITest"

            }
    print(desired_caps)
    return desired_caps

# {
#   "platformName": "iOS",
#   "playformVersion": "11.2",
#   "deviceName": "iPhone 6",
#   "automationName": "XCUITest",
#   "app": "/Users/work/Vanthink_stu_test.app"
# }

# automationName": "XCUITest