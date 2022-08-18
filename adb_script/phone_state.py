import os


def is_screen_lock(device_id):
    # ----------------------
    # 检测屏幕是否被锁，不同于屏幕点亮, 判断亮屏请使用 adbutils.is_screen_on
    # ----------------------
    try:
        if device_id is not None:
            cmd_1 = os.popen('adb -s ' + device_id + ' shell dumpsys window policy^|grep isStatusBarKeyguard').read()
            cmd_2 = os.popen('adb -s ' + device_id + ' shell dumpsys window policy^|grep mShowingLockscreen').read()
        else:
            cmd_1 = os.popen('adb shell dumpsys window policy^|grep isStatusBarKeyguard').read()
            cmd_2 = os.popen('adb shell dumpsys window policy^|grep mShowingLockscreen').read()
        if "isStatusBarKeyguard=true".strip() in cmd_1:
            return True
        elif "mShowingLockscreen=true".strip() in cmd_2:
            return True
        elif len(cmd_1) == 0 or len(cmd_2) == 0:
            command = 'adb -s ' + device_id + " shell dumpsys window policy"
            result = os.popen(command)
            lines = result.readlines()
            loc_flag = 0
            for i in range(len(lines)):
                # print('KeyguardServiceDelegate'.strip())
                if 'KeyguardServiceDelegate'.strip() in lines[i]:
                    loc_flag = i + 1
                    # print(lines[i])
            # print(lines[loc_flag])
            if 'showing=true' in lines[loc_flag] and loc_flag != 0:
                return True
            else:
                return False

        else:
            return False
    except Exception as e:
        print('获取手机lock状态异常', e)
        return False


####第一种方法
def is_screenState(device_id):
    try:
        if device_id is not None:
            cmd = 'adb -s ' + device_id + ' shell dumpsys power | grep "Display Power: state="'
        else:
            cmd = 'adb shell dumpsys power | grep "Display Power: state="'
        res = os.popen(cmd).read()
        print(res)
        if "state=ON" in res:
            return True
        else:
            return False

    except Exception as e:
        print('获取手机屏幕点亮状态异常', e)
        return False


####第二种方法

def is_screenState_bake(device_id):
    try:
        if device_id is not None:
            command = 'adb -s ' + device_id + " shell dumpsys window policy"
        else:
            command = 'adb shell dumpsys window policy'

        result = os.popen(command)
        lines = result.readlines()
        # print(lines)
        loc_flag = 0
        for i in range(len(lines)):
            # print('KeyguardServiceDelegate'.strip())
            if 'screenState'.strip() in lines[i]:
                loc_flag = i
                # print(lines[i])
        # print(lines[loc_flag])
        if 'screenState=SCREEN_STATE_ON' in lines[loc_flag] or 'screenState=2' in lines[loc_flag]:
            return True
        else:
            return False

    except Exception as e:
        print('获取手机屏幕点亮状态异常', e)
        return False


def wakeup_screen(device_id):
    try:
        if device_id is not None:
            command = 'adb -s ' + device_id + " shell input keyevent 26"
        else:
            command = 'adb shell input keyevent 26'
        os.popen(command)
    except Exception as e:
        print('点亮手机屏幕异常', e)
        return False
