from System.passwords import hashPassword, adminHash
from System.ui import runLoadbar

from time import sleep
from os import system
from getpass import getpass
system("cls")
print("Loading ToadOS...")

runLoadbar()

system("cls")

login = False
for count in range(1, 4):
    print("Input password")
    p = getpass(prompt="$* ")
    if  hashPassword(p) == adminHash:
        login = True
        break
    else:
        print("That is not password. Please try again. " + str(count) + "/3")
if login:
    system("py main.py")
else:
    print("You have incorrectly typed password 3 times. Exiting...")
    sleep(3)
