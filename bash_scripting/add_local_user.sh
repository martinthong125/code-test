#! /bin/bash

# This script creates a new user on the local system.
# You must supply a username as an argument to the script.
# A password will be automatically generated for the account.
# The username, password for the account will be displayed.

# Make sure script has superuser privileges
if [[ "${UID}" -ne 0 ]]
then
    echo "Please run with sudo or as root." >&2
    exit 1
fi

# if they don't supply at least one argument, give them help.
if [[ "${#}" -lt 1 ]]
then
    echo "Usage: ${0} USER_NAME [COMMENT] " >&2
    echo "Create an account with the name of USER_NAME and a comment field of COMMENT" >&2
    exit 2
fi

# The first parameter is USER_NAME
USER_NAME="$1"
echo $USER_NAME

# COMMENT="$2"
# echo $COMMENT

# drop $1 and add the rest of the argument to COMMENT
shift
COMMENT="$@"
echo $COMMENT

# Generate a password
# PASSWORD=$(date +%s%N | sha256sum | head -c48)
PASSWORD=$(echo $USER_NAME | cut -c 1-4 | sed 's/$/123!/')

# # Create the user with the password
# useradd -c "${COMMENT}" -m ${USER_NAME} &> /dev/null

# # Check if the useradd command succeeded.
# if [[ "$?" -ne 0 ]]
# then
#     echo "The account could not be created." >&2
#     exit 3
# fi

# # Set the password
# echo ${PASSWORD} | passwd --stdin ${USER_NAME} &> /dev/null

# # Check to see if the password command succeeded.
# if [[ $? -ne 0 ]]
# then
#     echo "The password for the account could not be set." >&2
#     exit 4
# fi

# # Force password change on first login
# passwd -e ${USER_NAME} &> /dev/null

# Display the USERNAME and PASSWORD
echo
echo "username: ${USER_NAME}"
echo "password: ${PASSWORD} "
exit 0
