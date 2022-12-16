import sys

# using try exception block
# to handle runtime errors
# IndexError, ZeroDivisionError, ImportError, ValueError, TypeError, NameError, FileNotFoundError, IOError, ModuleNotFoundError
# not syntax errors


# try:
#     print(4 / 0)

# except ZeroDivisionError as e:
#     print(e)
#     print("Hint: You should not divide by 0.")
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

except FileNotFoundError as e:
    print(e)
    print("Hint: Check that the file is present in given path.")
    sys.exit(1)
except NameError as e:
    print(e)
    print("Hint: Define your variable before use.")
    sys.exit(2)
except TypeError as e:
    print(e)
    print("Hint: Change your datatype to int or float.")
    sys.exit(3)
except ZeroDivisionError as e:
    print(e)
    print("Hint: Did you intend to divide by 10 by key in 0 only?")
    sys.exit(4)
except ModuleNotFoundError as e:
    print(e)
    print("Hint1: Please install the module before importing.")
    print("Hint2: Please ensure that the module exists before importing.")
    sys.exit(5)
except Exception as e:
    print(e)
    sys.exit(10)

finally:
    print("Finally, this will execute whether pass or fail.")

# try except else block
# try:
#     a = 10
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("Else: This will execute if there is no exception in try block")
# finally:
#     print("Finally:  This will always be printed.")


print("This line will always be printed.")
