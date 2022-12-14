import subprocess

# subprocess module is used to execute OS commands
# shell=True, a new shell is started to run the commands. Hence it will take a longer time.
# cmd is a string, just like the os command.
# shell=False, no new shell is started to run the commands. Hence, it will be faster.
# cmd is a list. Hence, need to convert the string to a list by using .split()
# use shell=True if the cmd involves env.
# use shell=True for windows os

cmd = "ls"

# shell=True
sp = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
)

# shell=False
# cmd1 = "bash --version".split()
# sp = subprocess.Popen(
#     cmd1,
#     shell=False,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     universal_newlines=True,
# )

# output
return_code = sp.wait()
output, error = sp.communicate()

print(f"RETURN CODE: {return_code}")
print(f"OUTPUT: {output.splitlines()}")
print(f"ERROR: {error.splitlines()}")
