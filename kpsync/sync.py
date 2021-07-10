import pysftp
import os

username = os.getenv("PI_USERNAME")
password = os.getenv("PI_PASSWORD")
host = os.getenv("PI_ADDR")
remotepath = os.getenv("PI_REMOTE_PATH")
localpath = os.getenv("LOCAL_PATH")

if __name__== "__main__":
    print("Remotepath: ", remotepath)
    print("Localpath: ", localpath)
    with pysftp.Connection(host, username=username, password=password) as sftp:
        sftp.get(remotepath=remotepath, localpath=localpath)