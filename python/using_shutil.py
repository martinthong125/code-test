# Python Shutil module provide us high-level operations on files and folders/directories like, copy, move, remove and much more.

import shutil

src = "/Users/martin.thong/testCode/python/demo.txt"
dest = "/Users/martin.thong/testCode/python/demo3.txt"
# shutil.copyfile(src, dest)  # normal copy
shutil.copy(src, dest)  # copy with same permissions
# shutil.copy2(src, dest)  # copy with same permission and meta data ie creation date
# shutil.copymode(src,dest) # copy the file permissions only, not the content
# shutil.copystat(src,dest) # copy the meta data only, ie creation date, not the content

# copy file content to another file by opening it
# file1=open('abc.txt', 'r')
# file2=open('xyz.txt','a')
# shutil.copyfileobj(file1, file2)

# copy directory
# src_dir = "/Users/martin.thong/testCode/python"
# shutil.copytree(src, "/tmp/python")

# delete directory
# shutil.rmtree("/tmp/python")
