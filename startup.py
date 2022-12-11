from time import sleep
from os import system
from getpass import getpass
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
while True:
    p = getpass(prompt="Enter Password: ")
    if p == "9-*h":
        break
    else:
        print("Incorrect Password.")
        system("cls")
system("py main.py")
