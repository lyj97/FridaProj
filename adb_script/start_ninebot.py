import os
import time


def kill_ninebot_and_demo_progress():
    cmd = 'adb shell am force-stop cn.ninebot.ninebot'
    os.popen(cmd)
    cmd = 'adb shell am force-stop com.lu.example.hello_xposed'
    os.popen(cmd)


def start_demo_for_start_ninebot():
    kill_ninebot_and_demo_progress()
    print("等待2秒后继续...")
    time.sleep(2)
    cmd = 'adb shell am start -n com.lu.example.hello_xposed/com.lu.example.hello_xposed.hello.app.StartNinebotActivity'
    os.popen(cmd)
