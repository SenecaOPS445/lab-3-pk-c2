#!/usr/bin/env python3
# Lab 3d script - free disk space
# Author ID: [seneca_id]

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0].decode('utf-8').strip()
    return output

if __name__ == '__main__':
    print(free_space())
