# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-FileCopyrightText: 2024-present Intel Corporation
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Avocado-framework functions module file"""

import sys

from avocado.core.job import Job
from avocado.core.nrunner.runnable import Runnable
from avocado.core.suite import TestSuite


def run_test() -> None:
    bintrue = Runnable("exec-test", "/bin/true")
    echo = Runnable("exec-test", "/usr/bin/echo", "Hello World!")
    id_test = Runnable(
        "exec-test", "/usr/bin/echo", "Hello World!", identifier="echo-hello-world"
    )

    suite = TestSuite(name="exec-test", tests=[bintrue, echo, id_test])

    with Job(test_suites=[suite]) as j:
        sys.exit(j.run())
