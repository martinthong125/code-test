# working with csv, comma separated values
# It is a simple file format used to store tabular data, such as spreadsheet/EXCEL or database
import csv

req_file = "/Users/martin.thong/test/python/data.csv"

# Method 1
file = open(req_file, "r")
content = file.readlines()
file.close()

print(content)
for line in content:
    print(line.strip("\n").split(","))

print("------------------------")
# Method 2, better cos can choose delimiter
file = open(req_file, "r")
# data = csv.reader(file, delimiter=",")
# for line in data:
#     print(line)


# separate header from data and find the number of rows of data
data1 = csv.reader(file, delimiter=",")
header = next(data1)
print(header)
rows = len(list(data1))
print(f"There are {rows} rows of data.")

file.close()


# create a csv file at chosen location
req_file1 = "/Users/martin.thong/test/python/writeTo.csv"
header1 = ["No", "Name", "Age"]
data1 = ["1", "Jackie", "35"]
data2 = [["2", "James", "47"], ["3", "Clement", "46"]]

file1 = open(req_file1, "w", newline="")
writer = csv.writer(file1, delimiter=",")
# write single row
writer.writerow(header1)
writer.writerow(data1)
# write multiple rows
writer.writerows(data2)
file1.close()
