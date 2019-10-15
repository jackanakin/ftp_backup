from ftplib import FTP
import datetime
import os

FTP_ADDRESS = 'ftp_address'
FTP_USERNAME = 'ftp_username'
FTP_PASSWORD = 'ftp_password'

sysDate = datetime.datetime.now()
date = str(sysDate.day) + '-' +  str(sysDate.month) + '-' + str(sysDate.year)

def start():
    os.mkdir('/home/backup/TIP/'+date)
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
                os.mkdir('/home/backup/TIP/'+date+'/'+file)
            except Exception as folderException:
                print(folderException)
            openFolder()
            ftp.cwd('..')
        except Exception as fileException:
            print('/home/backup/TIP/' + date + ftp.pwd() + '/' + file)
            ftp.retrbinary('RETR '+file, open('/home/backup/TIP/' + date + ftp.pwd() + '/' + file, 'wb').write)
    return

ftp = FTP(FTP_ADDRESS)
start()
