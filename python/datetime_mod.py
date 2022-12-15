from datetime import datetime

# import pytz
import os
import sys

# strftime.org

# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().month)
# print(datetime.now().hour)
# print(datetime.now().minute)
# print(datetime.now().strftime("%Y-%m-%d"))

# print(datetime.today())


# Find files that are older than 14 days

fileSetDay = 7
req_path = input("Enter the directory you want to search: ")
if not os.path.exists(req_path):
    print("You have provided an invalid path. Please provide a valid path.")
    sys.exit(1)

elif os.path.isfile(req_path):
    print("You have provided a filename. Please provide a valid path.")

else:
    # print(os.listdir(req_path))
    today = datetime.now()

    for item in os.listdir(req_path):
        file = os.path.join(req_path, item)
        if os.path.isfile(file):
            fileCtime = datetime.fromtimestamp(os.path.getctime(file))
            fileAge = (today - fileCtime).days
            if fileAge > fileSetDay:
                print(file, fileAge)
