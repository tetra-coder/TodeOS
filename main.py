from getpass import getpass
from webbrowser import open_new_tab
from os import system
isAdmin = False
system("cls")
print("WARNING: UNDER CONSTRUCTION")
print("Type help for a list of commands.")
print("To get access to other commands, type getadmin and type the password.")
print("Type exit to quit.")
while True:
    cmd = input("$ ")
    if "sudo" in cmd:
        open_new_tab("https://sandspiel.club/#d4af60c811854a768c36")
    if cmd == "exit":
        break
    if cmd == "clear":
        system("cls")
    if cmd == "opc":
        link = input("Enter a link of your choice: ")
        system("start chrome.exe " + link)
    if cmd == "opms":
        link = input("Enter a link of your choice: ")
        system("start msedge.exe " + link)
    if cmd == "opmz":
        link = input("Enter a link of your choice: ")
        system("start firefox.exe " + link)
    if cmd == "help":
        print("Commands: exit, clear, help, banner")
        if isAdmin:
            print("opc - Opens a link of your choice in Chrome")
            print("opms - Opens a link of your choice in Microsoft Edge")
            print("opmz - Opens a link of your choice in Firefox")
    if cmd == "banner":
        print("""
           .--._.--.
          ( O     O )
          /   . .   \\
         .`._______.'.
        /(           )\\
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\\
         '-'|/   \|`-`

         ToadOS (a collaboration beetween tetra-coder and TodePond)
        """)
    if cmd == "getadmin":
        adminpass = input("Type in the password: ")
        while adminpass != "88**66h":
            print("Incorrect password. Try again.")
            adminpass = input("Type in the password: ")
        print("You are an admin!")
system("cls")
quit()
