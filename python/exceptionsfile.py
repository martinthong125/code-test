import sys

# using try exception block
# to handle runtime errors
# IndexError, ZeroDivisionError, ImportError, ValueError, TypeError, NameError, FileNotFoundError, IOError, ModuleNotFoundError
# not syntax errors


# try:
#     print(4 / 0)

# except ZeroDivisionError:
#     print("divide by 0 is not possible.")
# except Exception as e:
#     print(e)
#     # print("zero division error.")
#     sys.exit(1)


# try:
#     file = open("abc.txt", "r")
#     print(file.read())
#     file.close()
# except Exception as e:
#     print(e)
#     # print("Problem reading file")
#     sys.exit(2)


# if exception is known
try:
    # code block
    # open("abc.txt", "r")
    # print(abc)
    # print(4 + "abc")
    # print(4 / 0)
    # import bash_scripting
    pass

except FileNotFoundError:
    print("File is not present in path.")
    sys.exit(1)
except NameError:
    print("Variable is not defined.")
    sys.exit(2)
except TypeError:
    print("Operation on different datatype is not possible.")
    sys.exit(3)
except ZeroDivisionError:
    print("Division by zero is not possible.")
    sys.exit(4)
except ModuleNotFoundError:
    print("Please install the module before importing.")
    sys.exit(5)
except Exception as e:
    print(e)
    sys.exit(10)

finally:
    print("Finally, this will execute whether pass or fail.")

# try except else block
try:
    a = 10
    print(a)
except Exception as e:
    print(e)
else:
    print("Else: This will execute if there is no exception in try block")
finally:
    print("Finally:  This will always be printed.")


print("This line will always be printed.")
