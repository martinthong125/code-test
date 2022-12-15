# working with text files

# write to file
content = ["writelines1", "writelines2", "writelines3"]
file = open("demo.txt", "w")
# print(file.mode)
# print(file.readable())
# print(file.writable())

# file.write("This is the first line.\n")
# file.write("This is the second line.\n")
# file.write("This is the third line.\n")

for line in content:
    file.write(line + "\n")

file.close()

# read from file
file = open("demo.txt", "r")
# print(file.read())
# print(file.readline())
data = file.readlines()

file.close()
# print(data)
for line in data:
    print(line[:-2])

# copy the content of a file to another file

# src_file = "/Users/martin.thong/test/python/demo.txt"
# dest_file = "/Users/martin.thong/test/python/newdemo2.txt"
src_file = input("Enter your source file: ")
dest_file = input("Enter your destination file: ")


file1 = open(src_file, "r")

data = file1.read()

file1.close()

file2 = open(dest_file, "w")

file2.write(data)

file2.close()
