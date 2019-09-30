from ftplib import FTP
import datetime
import os

FTP_ADDRESS = 'ftp_address'
FTP_USERNAME = 'ftp_username'
FTP_PASSWORD = 'ftp_password'

sysDate = datetime.datetime.now()
date = str(sysDate.day) + '-' +  str(sysDate.month) + '-' + str(sysDate.year)

def start():
    os.mkdir('tip/'+date)
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
                os.mkdir('tip/'+date+'/'+file)
            except Exception as folderException:
                print(folderException)
            openFolder()
            ftp.cwd('..')
        except Exception as fileException:
            print('tip/' + date + ftp.pwd() + '/' + file)
            ftp.retrbinary('RETR '+file, open('tip/' + date + ftp.pwd() + '/' + file, 'wb').write)
    return

ftp = FTP(FTP_ADDRESS)
start()
