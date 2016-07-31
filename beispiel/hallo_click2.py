#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""Executable hello world example powered by click.

See http://click.pocoo.org/6/for more extensive details about how to use
click.
"""

import click


@click.command()
@click.argument('names', nargs=-1)  # See http://click.pocoo.org/6/arguments/
@click.option('--bye', is_flag=True)
def hallo(names, bye):
    """Print a German greeting for each name supplied."""
    if bye:
        msg = 'Tschüss {}!'
    else:
        msg = 'Hallo {}!'

    for name in names:
        click.echo(msg.format(name.capitalize()))


if __name__ == '__main__':
    hallo()
