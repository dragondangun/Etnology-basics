from ftp_settings import FTP_URL, FTP_USERNAME, FTP_PASSWORD 
from ftplib import FTP
from pathlib import Path

def uploadFile(path):
    with FTP(FTP_URL, FTP_USERNAME, FTP_PASSWORD) as ftp, open(path, 'rb') as file:
        ftp.cwd(ftp.pwd() + '/htdocs')
        ftp.storbinary(f'STOR {path.name}', file)

abstractFile = open("Abstract.html", "r", encoding="utf8")
textToAdd = abstractFile.read()
abstractFile.close()

citeCounter = 1
point = textToAdd.find('%cite%')
while(point != -1):
    textToAdd = textToAdd[:point] + str(citeCounter) + textToAdd[point+6:]
    point = textToAdd.find('%cite%')
    citeCounter += 1

textToAdd = textToAdd.replace('--', '�')

mainFile = open("index.html", "w", encoding="utf8")
title = '' # Enter title
mainFile.write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title>Конспект '+title+'</title>\n\t\t<link rel="stylesheet" href="style.css">\n\t</head>\n\t<body>\n\t\t<div class="MyDiv">\n')
mainFile.write(textToAdd)
mainFile.write('\n\t\t</div>\n\t</body>\n</html>')
mainFile.close()

uploadFile(Path('index.html'))
uploadFile(Path('style.css'))

