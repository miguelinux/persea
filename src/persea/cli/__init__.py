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
from persea.connection import ssh_connect_with_config
from persea.palta import run_test


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="persea")
@click.option("--host", help="Host from SSH config file")
@click.option("--ssh-config", default="~/.ssh/config", help="SSH config file")
@click.option(
    "--test-suite-file",
    default="~/.config/persea/test-suite.txt",
    help="Test Suite file",
)
@click.option(
    "-c", "--config", default="~/.config/persea/config.txt", help="Persea config file"
)
@click.pass_context
def persea(ctx, host, ssh_config, test_suite_file, config):
    """Execute test on a local or remote platform"""

    click.echo("ssh = " + ssh_config)
    click.echo("tsf = " + test_suite_file)
    click.echo("cfg = " + config)
    if host is not None:
        click.echo("host = " + host)

    if ctx.invoked_subcommand is None:
        click.echo(f"Subcommand: {ctx.invoked_subcommand}")
        # ret = ssh_connect_with_config("noble", "~/.ssh/config-container")
        ret = -1
        click.echo("ssh = " + str(ret))
    elif ctx.invoked_subcommand == "pre-commit":
        # used only for pre-commit meanwhile developing
        ret = ssh_connect_with_config("noble", "~/.ssh/config-container")
    else:
        click.echo(f"Sigue: {ctx.invoked_subcommand}")


@persea.command()
@click.pass_context
def run(ctx):
    """Execute a test"""

    click.echo("Run test")
    pre_commit = 1
    if pre_commit == 0:
        # used only for pre-commit meanwhile developing
        run_test()
