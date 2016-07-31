#! /usr/bin/env python
"""Executable hello world example powered by click.

See http://click.pocoo.org/6/for more extensive details about how to use
click.
"""

import click


@click.command()
@click.argument('names', nargs=-1)  # See http://click.pocoo.org/6/arguments/
def hallo(names):
    """Print a German greeting for each name supplied."""
    for name in names:
        click.echo('Hallo {}!'.format(name.capitalize()))


if __name__ == '__main__':
    hallo()
