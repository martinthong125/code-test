import os

# to work/interact with OS to automate many more tasks like creating directory, removing directory, identifying current directory and many more

# print(os.sep)
# print(os.getcwd())
# os.chdir("/Users/martin.thong/test/awk")
# print(os.getcwd())

# print(os.listdir())
# os.mkdir("newdir")
# print(os.listdir())

# os.makedirs("newdir2/newdir3")

# os.remove(file)
# os.rmdir("newdir")
# os.removedirs("newdir2/newdir3")

# print(os.environ)
# print(os.getuid())
# print(os.getpid())

# os.rename(src, dest)

# os.path is a sub module of os to work on paths
# pathway = "/Users/martin.thong/test/python/os_mod.py"
# path1 = "/home"
# path2 = "python/file.py"
# print(os.path.sep)
# print(os.path.basename(pathway))
# print(os.path.dirname(pathway))
# path3 = os.path.join(path1, path2)
# print(path3)
# print(os.path.split(path3))  # to split into (basename,filename)
# print(os.path.getsize(pathway))
# print(os.path.exists(pathway))
# print(os.path.isfile(pathway))
# print(os.path.isdir(pathway))
# print(os.path.islink(pathway))

# time module: getatime, getctime,getmtime

# os.system executes the command like in the os. Eg. linux
# os.system("pwd;ls")  # there is a return code
# return_code = os.system("pwd")
# print(return_code)
# os.system("pwd")


# os.walk find files in recurring directories
# it is used to generate director and filenames in a directory tree by walking
pathway2 = "/Users/martin.thong/test"  # a dir
# print(list(os.walk(pathway2)))
print("-------------------")
# for path in os.walk(pathway2):
#     print(path)

for root, directories, files in os.walk(pathway2):
    # print(root)  # all directories 1 level deep
    # print(directories) # all sub directories of 1 level deep directories
    print(root)  # all files including in sub directories

print("----------------------------------")
# use case to get the full path of the files in the directory
for root, directories, files in os.walk(pathway2):
    if len(files) != 0:
        for file in files:
            print(os.path.join(root, file))
