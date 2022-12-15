import subprocess

cmd = "java --version"

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
        if "openjdk" in line:
            java_version = line.split()[1]

    print(f"The java version number: {java_version}")

else:
    print("You have entered an invalid command.")
# print(f"RETURN CODE: {return_code}")
# print(f"OUTPUT: {output.splitlines()}")
# print(f"ERROR: {error.splitlines()}")
