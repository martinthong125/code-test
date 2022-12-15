import getpass

# getpass() prompts the user for a password without echoing.
# getuser() displays the login name of the user.

login_password = "password123"
db_password = getpass.getpass("Enter your db password: ")
print(db_password)

while db_password != login_password:
    db_password = getpass.getpass("Enter your db password: ")
    print(db_password)
