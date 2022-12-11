from time import sleep
import random
from os import system
from getpass import getpass
import hashlib
system("cls")
print("Loading ToadOS...")
# Loading bar from https://www.youtube.com/watch?v=MtYOrIwW1FQ
def loadBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()
items = list(range(0, 75))
l = len(items)
loadBar(0, l, prefix='Progress: ', suffix="Complete", length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadBar(i + 1, l, prefix="Progress: ", suffix="Complete", length=l)

system("cls")

# to make a new password, generate its hash with the hashPassword() function
# and replace it below
# TODO: find a better way to do this than just a variable here, maybe a file?
adminHash = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
def hashPassword(password):
    return hashlib.sha512(password.encode("utf8")).hexdigest()
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
