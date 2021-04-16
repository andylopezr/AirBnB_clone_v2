#!/usr/bin/python3
"""Deletes outdated archives"""

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ['35.190.169.147', '34.75.12.144']
env.user = "ubuntu"


def do_clean(number=0):
    """Deletes only unnecessary archives"""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
