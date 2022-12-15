import subprocess

# subprocess module is used to execute OS commands
# shell=True, a new shell is started to run the commands. Hence it will take a longer time.
# cmd is a string, just like the os command.
# shell=False, no new shell is started to run the commands. Hence, it will be faster.
# cmd is a list. Hence, need to convert the string to a list by using .split()
# use shell=True if the cmd involves env.
# use shell=True for windows os

cmd = "bash --version"

# shell=True
sp = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
)


# output
return_code = sp.wait()
output, error = sp.communicate()

if return_code == 0:
    for line in output.splitlines():
        if "version" in line and "release" in line:
            version_num = line.split()[3].split("(")[0]
    print(f"The bash version number: {version_num}")

else:
    print("You have entered an invalid command.")
