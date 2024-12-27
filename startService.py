# -*- coding: utf-8 -*-
"""
@Time ： 2024/12/25 14:08
@Auth ： 七月
@File ：stopService.py
@IDE ：PyCharm

"""
import subprocess
import threading
import time
import tkinter as tk
import pyautogui

start_process = [r'D:\MobaXterm\2\MobaXterm.exe',r'C:\Program Files\Google\Chrome\Application\chrome.exe',r'D:\飞书\2\Feishu\Feishu.exe',r'D:\微信\2\WeChat\WeChat.exe']
stop_process = ['MobaXterm.exe','chrome.exe','Feishu.exe','WeChat.exe']


def startService(root):
    for i in start_process:
        if 'chrome.exe' in i:
            subprocess.Popen(i)
            time.sleep(3)
            pyautogui.click(1297,885)
            continue
        elif 'WeChat.exe' in i:
            subprocess.Popen(i)
            time.sleep(3)
            pyautogui.click(1288, 918)
            continue
        else:
            subprocess.Popen(i)
    # subprocess.Popen(r'"D:\navicat\2\Navicat Premium 17\navicat.exe"')
    root.destroy()  # 关闭主窗口
def startMethod(root):
    threading.Thread(target=startService, args=(root,), daemon=True).start()

def closeMethod(root):
    for j in stop_process:
        threading.Thread(target=closeApp, args=(j, root), daemon=True).start()


def closeApp(app_name, root):
    try:
        # 使用 taskkill 命令关闭应用程序
        subprocess.run(['taskkill', '/IM', app_name, '/F'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass
    finally:
        root.after(0, root.destroy)  # 在主线程中关闭主窗口
def showWindow():
    # 创建主窗口
    root = tk.Tk()
    root.title("控制窗口")

    # 创建启动按钮
    start_button = tk.Button(root, text="启动", command=lambda: startMethod(root))
    start_button.pack(pady=10)

    # 创建停止按钮
    stop_button = tk.Button(root, text="停止", command=lambda: closeMethod(root))
    stop_button.pack(pady=10)

    # 运行主循环让打开的窗口一直显示
    root.mainloop()

if __name__ == '__main__':
    showWindow()