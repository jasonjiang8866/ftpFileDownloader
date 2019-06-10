from ftplib import FTP
#setup config
host=
port=
remoteFolder=
localFolder=

ftp=FTP()
ftp.connect(host=host, port=port)
ftp.login()
fileList=ftp.nlst(remoteFolder)
for item in fileList:
    if 'key1' not in item and 'key2' in item:
        ftp.retrbinary('RETR {0}{1}'.format(remoteFolder, item), open('{0}{1}'.format(localFolder,item),'wb').write)
