from ftplib import FTP
import datetime
import os
import pathlib

FTP_ADDRESS = 'ftp_address'
FTP_USERNAME = 'ftp_username'
FTP_PASSWORD = 'ftp_password'

sysDate = datetime.datetime.now()
date = str(sysDate.day) + '-' +  str(sysDate.month) + '-' + str(sysDate.year)

def start():
    pathlib.Path(date).mkdir(exist_ok=True)
    ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)
    openFolder()
    ftp.quit()
    return

def openFolder():
    filelist = ftp.nlst()
    for file in filelist:
        try:
            ftp.cwd(file)
            print(">"+file)
            try:
                pathlib.Path(date+'/'+file).mkdir(exist_ok=True)
            except Exception as folderException:
                print(folderException)
            openFolder()
            ftp.cwd('..')
        except Exception as fileException:
            ftp.retrbinary('RETR '+file, open(date + '/' + ftp.pwd() + '/' + file, 'wb').write)
            print(file)
    return

ftp = FTP(FTP_ADDRESS)
start()
