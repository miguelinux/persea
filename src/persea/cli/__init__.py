# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
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
@click.pass_context
def persea(ctx):
    """Execute test on a local or remote platform"""

    if ctx.invoked_subcommand is None:
        click.echo("Hola Mundo!")
    else:
        click.echo(f"Sigue: {ctx.invoked_subcommand}")


@persea.command()
def run():
    """Execute a test"""

    click.echo("Run test")
