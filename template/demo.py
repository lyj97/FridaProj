import io
import sys

import frida


# python2.7

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def start_hook(js, pkg):
    jscode = io.open(js, 'r', encoding='utf8').read()
    device = frida.get_usb_device(timeout=5)
    pid = device.spawn(pkg)
    session = device.attach(pid)
    script = session.create_script(jscode)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()


def start_hook_attach(js, pkg):
    jscode = io.open(js, 'r', encoding='utf8').read()
    device = frida.get_usb_device(timeout=5)
    session = device.attach(pkg)
    script = session.create_script(jscode)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()


def main(argv):
    if len(argv) != 2:
        print("must input two arg")
        print("For exanple: python demo.py packName")
    else:
        start_hook(argv[0], argv[1])


if __name__ == "__main__":
    main(sys.argv)
