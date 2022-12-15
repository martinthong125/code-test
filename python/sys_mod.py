import sys

# The sys module is used to work with python runtime environment

# print(sys.version)
# print(sys.version_info)
# print(sys.path) # sys.path is an env var for python
# print(sys.modules)

print(sys.argv)  # returns a list of command line arguments passed to a python script
print(sys.argv[0])  # return the filename

if len(sys.argv) != 3:
    print("You need to key in 3 arguments for the script to work.")
    sys.exit(1)


sys.exit(1)  # exit the script due to some error
print("This line will not be printed!")
