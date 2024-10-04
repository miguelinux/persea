# SPDX-FileCopyrightText: 2024-present Intel Corporation
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Main persea module file"""

import click

from persea.__about__ import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="persea")
def persea():
    """Main and entry function with no arguments"""

    click.echo("Hola Mundo!")
