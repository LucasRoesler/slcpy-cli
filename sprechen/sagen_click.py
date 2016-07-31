#! /usr/bin/env python
"""Executable hello world example powered by click.

See http://click.pocoo.org/6/ for more extensive details about how to use
click.
"""

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option('1.0.0')
def cli():
    """Print a German phrases."""
    pass


@cli.command()
@click.argument('names', nargs=-1)  # See http://click.pocoo.org/6/arguments/
def hallo(names):
    """Print a German greeting to the cli"""
    for name in names:
        click.echo('Hallo {}!'.format(name.capitalize()))


@cli.command()
@click.argument('names', nargs=-1)  # See http://click.pocoo.org/6/arguments/
def bye(names):
    """Print a German parting to the cli."""
    for name in names:
        click.echo('Tschüss {}!'.format(name.capitalize()))


if __name__ == '__main__':
    cli()
