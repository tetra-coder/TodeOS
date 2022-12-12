from getpass import getpass
from webbrowser import open_new_tab
from os import system
import hashlib
isAdmin = False
adminHash = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
def hashPassword(password):
    return hashlib.sha512(password.encode("utf8")).hexdigest()
system("cls")
print("Type help for a list of commands.")
print("To get access to other commands, type getadmin and type the password.")
print("Type exit to quit.")
while True:
    cmd = input("$ ")
    if "sudo" in cmd:
        open_new_tab("https://sandspiel.club/#d4af60c811854a768c36")
    elif cmd == "exit":
        break
    elif cmd == "clear":
        system("cls")
    elif cmd == "opc":
        link = input("Enter a link of your choice: ")
        system("start chrome.exe " + link)
    elif cmd == "opms":
        link = input("Enter a link of your choice: ")
        system("start msedge.exe " + link)
    elif cmd == "opmz":
        link = input("Enter a link of your choice: ")
        system("start firefox.exe " + link)
    elif cmd == "help":
        print("Commands: exit, clear, help, banner")
        if isAdmin:
            print("opc - Opens a link of your choice in Chrome")
            print("opms - Opens a link of your choice in Microsoft Edge")
            print("opmz - Opens a link of your choice in Firefox")
    elif cmd == "banner":
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
         ToadOS (a collaboration beetween tetra-coder, TodePond and Magnogen)
        """)
    elif cmd == "getadmin":
        for count in range(1, 3):
            print("Input password:")
            p = getpass(prompt="$* ")
            if  hashPassword(p) == adminHash:
                print("You are an admin!")
                isAdmin = True
                break
            else:
                print("That is the not password. Please try again. " + str(count) + "/3")
    else:
        print("Whoops! Looks like you've been lost. This command is invalid. Try typing in help?")
system("cls")
