import os
import requests
import urllib.error
import urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.path.basename(os.path.abspath(__file__))) #実行ファイル名抽出

### my library ###
def introduce(local_version):
    print(os.path.basename(__file__)+' ver '+str(local_version))
    print('Created By : VERSUS.log')
    print('Twitter : @227_VS')
    print('Blog : https://raspberrypi422.mydns.jp')
    print('Github : https://github.com/MayaYamato')

def download_file(url,path):
    try:
        file = urllib.request.urlopen(url).read()
        with open(path,'wb') as f0:
            f0.write(file)
    except urllib.error.URLError as __e:
        pass

def download_content(url,path):
    try:
        file = requests.get(url)
        with open(path,'wb') as f0:
            f0.write(file.content)
    except urllib.error.URLError as __e:
        pass

def update_check(local_version,url_version,url_github,path):
    print('Version Checking ... ')
    with urllib.request.urlopen(url_version) as response:
        html = response.read().decode() 
        remote_version = html[:-1]
    if float(remote_version) - float(local_version) > 0:
        print('New Version Released:'+str(remote_version)+'\n')
        tmp =input('Do Upgrade? yes or no\n>>')
        if tmp == 'yes':
            download_content(url_github,path)
            print('Download Complete')
        else:
            pass
    else:
        print('Latest Version\n')