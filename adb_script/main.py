import time

from adb_script.phone_state import is_screenState, wakeup_screen
from adb_script.start_ninebot import start_demo_for_start_ninebot, kill_ninebot_and_demo_progress, reboot_device


def start_ninebot():
    if not is_screenState(None):
        wakeup_screen(None)
        print("等待2秒后继续...")
        time.sleep(2)
    start_demo_for_start_ninebot()
    count = 60
    while count > 0:
        print("等待" + str(count) + "秒后继续...")
        time.sleep(1)
        count = count - 1
    kill_ninebot_and_demo_progress()
    print("已完成.")
    reboot_device()


def start_at_time():
    started = False
    while True:
        localtime = time.localtime(time.time())
        t_hour = localtime.tm_hour
        if 9 == t_hour:
            if not started:
                print("9点多了，开始执行...")
                print("当前时间:")
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                started = True
                start_ninebot()
            else:
                print("9点多了，但已经执行过了...")
                print("当前时间:")
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            started = False
        print("当前时间:")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("等待1分钟后继续...")
        count = 60
        print("等待" + str(count) + "秒后继续...")
        for _ in range(count):
            print("-", end='')
        print()
        while count > 0:
            print("-", end='')
            time.sleep(1)
            count = count - 1
        print()


if __name__ == '__main__':
    start_at_time()
