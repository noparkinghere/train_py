# Requires "requests" to be installed (see python-requests.org)
import requests
import os

def RemoveBg(fileName):
    saveFile = fileName.split('.')[0] + '_mod.' + fileName.split('.')[-1]
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(fileName, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'rwLc72uEbgAsgUbZYWCnkniF '},
    )
    if response.status_code == requests.codes.ok:
        with open(saveFile, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
        
def RemoveAllFilesBg(path):
    os.chdir(path)
    files = os.listdir(os.getcwd())
    for i in files:
        if