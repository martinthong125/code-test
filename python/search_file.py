import os
import string
import platform


# search for file in user directory and return the full path
# Platform independent
req_file = input("Enter the filename you want to find: ")

if platform.system() == "Windows":
    possible_drives = string.ascii_uppercase
    drives = []
    for drive in possible_drives:
        if os.path.exists(drive + ":\\"):
            drives.append(drive + ":\\")
    print(drives)
    for drive in drives:
        for root, directories, files in os.walk(drive):
            for file in files:
                if file == req_file:
                    print(os.path.join(root, file))

else:
    for root, directories, files in os.walk("/Users/martin.thong/test"):
        for file in files:
            if req_file == file:
                print(os.path.join(root, file))
