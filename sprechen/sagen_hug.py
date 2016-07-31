#! /usr/bin/env python
"""Executable hello world example powered by hug.

See https://github.com/timothycrosley/hug for more extensive details about
how to use hug.

Note kwargs are not support for cli usage, per
https://github.com/timothycrosley/hug/issues/321
"""

import hug

sagen = hug.get(
    output=hug.output_format.text,
    examples='names=Hanz&names=Franz',
)


@sagen
@hug.cli()
def hallo(names: hug.types.multiple):
    """Print a German greeting to the cli"""

    return '\n'.join(
        'Hallo {}!'.format(name.capitalize())
        for name in names
    )


@sagen
@hug.cli()
def bye(names: hug.types.multiple):
    """Print a German parting to the cli."""
    return '\n'.join(
        'Tschüss {}!'.format(name.capitalize())
        for name in names
    )
