# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-FileCopyrightText: 2024-present Intel Corporation
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Connection persea module file"""

from os.path import exists
from os.path import expanduser

import paramiko
from paramiko.config import SSHConfig


def ssh_connect_with_config(hostname: str, ssh_config_file: str) -> int:
    """Connect to a server with SSH config"""

    config = SSHConfig()

    local_ssh_config_file = ssh_config_file.strip()

    if local_ssh_config_file[0] == "~":
        home_dir = expanduser("~")
        local_ssh_config_file = local_ssh_config_file.replace("~", home_dir)

    if not exists(local_ssh_config_file):
        return 1

    with open(local_ssh_config_file) as f:
        config.parse(f)

    # Get the config hostname
    host_config = config.lookup(hostname)

    connect_args = {
        "hostname": "",
        "username": "",
        "port": 22,
    }

    if "hostname" in host_config:
        connect_args["hostname"] = host_config["hostname"]

    if "user" in host_config:
        connect_args["username"] = host_config["user"]

    if "port" in host_config:
        connect_args["port"] = int(host_config["port"])

    if "identityfile" in host_config:
        connect_args["key_filename"] = host_config["identityfile"]

    if "connecttimeout" in host_config:
        connect_args["timeout"] = float(host_config["connecttimeout"])

    ##if 'proxycommand' in user_config:
    ##    cfg['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

    # Crear un cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # nosec B507

    try:
        client.connect(**connect_args)  # type: ignore
        print(f"Conexión SSH establecida a {hostname}")

        # Ejecutar un comando (ejemplo)
        # stdin, stdout, stderr = client.exec_command("persea run")  # nosec B601
        stdin, stdout, stderr = client.exec_command(
            "bash -lc 'persea run'"
        )  # fmt: skip # nosec B601 # noqa
        print("stdout: ", stdout.read().decode("utf-8"))
        print("stderr: ", stderr.read().decode("utf-8"))
        str_stderr = stderr.read().decode("utf-8")

        if "command not found" in str_stderr:
            str_command = "sudo apt-get -y install git pipx"
            # str_command = "sudo apt-get -y install git python3-pip python3-venv"
            print(str_command)
            # stdin, stdout, stderr = client.exec_command(str_command)  # nosec B601

            # print("stdout: ", stdout.read().decode("utf-8"))
            # print("stderr: ", stderr.read().decode("utf-8"))
            # stdin, stdout, stderr = client.exec_command(str_command)  # nosec B601

    except Exception as e:
        print(f"Error al conectar: {e}")
    finally:
        client.close()

    return 10


# Ejemplo de uso:
# hostname = "servidor_remoto"
# ssh_connect_with_config(hostname)
