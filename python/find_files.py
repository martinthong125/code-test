import os
import sys

# To find files with a certain extension

req_path = input("Enter your directory path: ")


if os.path.isfile(req_path):
    print(f"You have given a filename. Please enter a directory.")
    sys.exit(1)

else:
    files = os.listdir()
    if len(files) == 0:
        print("There are no files in this directory.")
    else:
        req_ext = input("Enter the file extension to search: [.py .txt .sh .log]: ")
        print("Searching for files...")
        filesList = []
        for file in files:
            if file.endswith(req_ext):
                filesList.append(file)

        if len(filesList) == 0:
            print(f"There are no files with the extension: {req_ext}")
        else:
            print(f"Files with the required extension: {filesList}")
            print(f"There are {len(filesList)} file(s) with the extension {req_ext}")
