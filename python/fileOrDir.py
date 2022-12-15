import os

pathway = input("Enter your path: ")

if os.path.exists(pathway) and os.path.isfile(pathway):
    print(f"The given path: {pathway} is a file.")
elif os.path.exists(pathway):
    print(f"The given path: {pathway} is a directory.")
else:
    print(f"The given path: {pathway} is not a valid path.")
