# Will Hearn
import re
import os
import subprocess


def search(string):
    return re.search(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}", string)


if __name__ == '__main__':
    out = str(subprocess.check_output(['ipconfig']))
    print(search(out))

