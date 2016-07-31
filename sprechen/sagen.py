#! /usr/bin/env python
"""Executable hello world example that accepts arguments.

See https://docs.python.org/3/library/argparse.html for more extensive details
about how to use argparse.

In this example we focus on sub-commands, see
https://docs.python.org/3/library/argparse.html#sub-commands
"""

import argparse


def hallo(args):
    for name in args.names:
        print('Hallo {}!'.format(name.capitalize()))


parser = argparse.ArgumentParser(description='Speak messages to the cli')
subparsers = parser.add_subparsers(
    title='subcommands',
)


parser_hallo = subparsers.add_parser(
    'hallo', help='Print a German greeting to the cli')
parser_hallo.add_argument(
    'names',
    metavar='NAME', type=str, nargs='+',
    help='a persons name',
)
parser_hallo.set_defaults(func=hallo)


def bye(args):
    for name in args.names:
        print('Tschüss {}!'.format(name.capitalize()))


parser_bye = subparsers.add_parser(
    'bye', help='Print a German parting to the cli')
parser_bye.add_argument(
    'names',
    metavar='NAME', type=str, nargs='+',
    help='a persons name',
)
parser_bye.set_defaults(func=bye)


if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
