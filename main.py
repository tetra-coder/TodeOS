from getpass import getpass
from webbrowser import open_new_tab
from os import system
system("cls")
print("WARNING: UNDER CONSTRUCTION")
print("Type help for a list of commands.")
print("To get access to most commands, type getadmin and type the password.")
print("Type exit to quit.")
while True:
    cmd = input("$ ")
    if "sudo" in cmd:
        open_new_tab("https://sandspiel.club/#d4af60c811854a768c36")
    if cmd == "exit":
        break
    if cmd == "clear":
        system("cls")
    if cmd == "help":
        print("Commands: exit, clear, help")
        print("Admin commands: ")
system("cls")
quit()
