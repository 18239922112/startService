# -*- coding: utf-8 -*-
"""
@Time ： 2024/12/24 15:58
@Auth ： 七月
@File ：startService.py
@IDE ：PyCharm

"""
import pyautogui
import time
import subprocess

def openMobaXterm():

    subprocess.Popen(r'"D:\MobaXterm\2\MobaXterm.exe"')
    time.sleep(3)


def openChrome():
    subprocess.Popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    time.sleep(3)

def openWechat():
    subprocess.Popen(r'"D:\微信\2\WeChat\WeChat.exe"')
    time.sleep(3)
    pyautogui.doubleClick(1281, 916)


def openFeishu():
    subprocess.Popen(r'"D:\飞书\2\Feishu\Feishu.exe"')
    time.sleep(3)



def openNavicat():
    subprocess.Popen(r'"D:\navicat\2\Navicat Premium 17\navicat.exe"')
    time.sleep(3)


def startMethod():
    openMobaXterm()
    openFeishu()
    openChrome()
    openWechat()
    #openNavicat()


if __name__ == '__main__':
    startMethod()