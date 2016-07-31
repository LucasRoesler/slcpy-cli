#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""Executable hello world example that accepts arguments.

See https://docs.python.org/3/library/argparse.html for more extensive details
about how to use argparse
"""

import argparse

parser = argparse.ArgumentParser(description='Say Hello to someone')
parser.add_argument(
    'names',
    metavar='NAME', type=str, nargs='+',
    help='a person to speak to',
)
parser.add_argument('--bye', action='store_true', default=False)

if __name__ == '__main__':
    args = parser.parse_args()

    if args.bye:
        msg = 'Tschüss {}!'
    else:
        msg = 'Hallo {}!'

    for name in args.names:
        print(msg.format(name.capitalize()))
