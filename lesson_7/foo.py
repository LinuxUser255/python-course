#!/usr/bin/env python3

import subprocess

def exec_os_cmd(cmd):
    result = subprocess.check_output(cmd, shell=True, text=True)
    print(result)

exec_os_cmd('whoami')
