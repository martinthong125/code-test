# create an exception
# raise Exception
# AssertionError
import sys

# raise Exception
age = 23

if age > 30:
    print("valid age")
else:
    raise ValueError("Age is less than 30")
    # cannot add sys.exit(1)

# AssertionError

try:
    age = 205
    assert age > 30
    print("valid age")
except AssertionError:
    print("Value is not accepted.")
    sys.exit(2)
