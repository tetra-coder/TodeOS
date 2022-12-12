# emulate the ls command on ToadOS

import os
import sys

def ls():
    if len(sys.argv) == 1:
        print(os.listdir(os.getcwd()))
    else:
        print(os.listdir(sys.argv[1]))