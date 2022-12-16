#! /usr/bin/python3
# ssh to remote server and run commands
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname="", username="", password="", port=22)
ssh.connect(
    hostname="3.132.212.105",
    username="ec2-user",
    key_filename="/Users/martin.thong/.ssh/paramiko.pem",
    port=22,
)
# executing commands on remote server
# stdin, stdout, stderr = ssh.exec_command("whoami")
# # stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")
# print("The OUTPUT is: ")
# # print(stdout.read())
# print(stdout.readlines())

# print("The ERROR is: ")
# print(stderr.readlines())


# uploading and downloading files from remote server
sftp = ssh.open_sftp()
# download file from remote server
# sftp.get("/home/ec2-user/file1.txt", "/tmp/file1.txt")
# upload file to remote server
sftp.put("/tmp/demo.txt", "/home/ec2-user/demo1.txt")

sftp.close()
ssh.close()
