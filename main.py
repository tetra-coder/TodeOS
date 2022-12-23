from System.passwords import hashPassword, adminHash
from System.ls import ls
import Games
import getpass
import os
isAdmin = False
adminHash = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
os.system("cls")
print("Type help for a list of commands.")
print("To get access to other commands, type getadmin and type the password.")
print("Type exit to quit.")
while True:
    cmd = input("$ ")
    if "sudo" in cmd and not isAdmin:
        print("Sudo is only for admins... rickroll loading...")
        os.system("start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    elif cmd == "exit":
        break
    elif cmd == "clear":
        os.system("cls")
    elif cmd == "opc":
        link = input("Enter a link of your choice: ")
        os.system("start chrome.exe " + link)
    elif cmd == "opms":
        link = input("Enter a link of your choice: ")
        os.system("start msedge.exe " + link)
    elif cmd == "opmz":
        link = input("Enter a link of your choice: ")
        os.system("start firefox.exe " + link)
    elif cmd == "help":
        print("Commands: exit, clear, help, banner, ls, getadmin")
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
         TodeOS (a collaboration beetween tetra-coder, Magnogen and samclane)
        """)
    elif cmd == "getadmin":
        for count in range(1, 3):
            print("Input password:")
            p = getpass.getpass(prompt="$* ")
            if  hashPassword(p) == adminHash:
                print("You are an admin!")
                isAdmin = True
                break
            else:
                print("That is not password. Please try again. " + str(count) + "/3")
    elif cmd == "pong":
        Games.pong()
    elif cmd == "eldenring":
        Games.eldenring()
    elif cmd == "ls" or cmd == "cd":
        ls()
    elif cmd == "games":
        print("Games can be accessed by simple typing their name into the terminal. Eg. eldenring.")
        print("Available games: ")
        print("Pong - pong")
        print("Elden Ring (Terminal Edition) - eldenring")
    else:
        print("The command is invalid. Try the help command to get some help.")
os.system("cls")
