#coding=utf-8
import os
#from Public.Connect import *
import time


def start_android_devices():
    '''启动ios模拟器'''
    command = r'start C:\Program" "Files" "^(x86^)\Nox\bin\Nox.exe'
    os.system(command)
    time.sleep(20)
    print('模拟器启动成功')
    adb= 'adb devices'
    os.system(adb)
    print('\n')


def stop_android_devices():
    '''结束ios模拟器进程'''
    command = r'taskkill -f -im Nox.exe'
    os.system(command)
    print('所有任务执行完毕，关闭模拟器')
    print('\n')
