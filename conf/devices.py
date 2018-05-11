# coding=utf-8
import os
import subprocess
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径
import re

class Devices:
    """获取连接的设备的信息"""
    def __init__(self):
        # self.GET_ANDROID = "adb devices"
        self.GET_IOS = "instruments -s devices"

    def get_devices(self):
        value = os.popen(self.GET_IOS)
        device = []
        for v in value.readlines():
            iOS = {}

            s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")

            if v.rfind('Simulator') != -1:
                continue
            if v.rfind("(") == -1:
                continue

            iOS['platformName'] = 'iOS'
            iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
            iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
            iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
            iOS['bundleId'] = 'xxxx'

            device.append(iOS)
        return device
    #
    # def start_android_devices(self):
    #     """启动安卓模拟器"""
    #     command = r'start C:\Program" "Files" "^(x86^)\Nox\bin\Nox.exe'
    #     os.system(command)
    #     # time.sleep(10)
    #     print('模拟器启动成功')
    #     adb = 'adb devices'
    #     os.system(adb)
    #     print('\n')
    #
    # def stop_android_devices(self):
    #     """结束安卓模拟器进程"""
    #     command = r'taskkill -f -im Nox.exe'
    #     os.system(command)
    #     print('所有任务执行完毕，关闭模拟器')
    #     print('\n')
