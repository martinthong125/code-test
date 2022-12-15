import os
import platform

# This is a platform independent script to clear the screen
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("Start of new screen.")
