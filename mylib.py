import requests
import urllib.error
import urllib.request

### my library ###

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

def update_check(version,Github_url,path):
    print('Version Checking ... ')
    with urllib.request.urlopen(Github_url) as response:
        html = response.read().decode() 
        exever = html[:-1]
    if float(exever) - float(version) > 0:
        print('New Version Released:'+str(exever)+'\n')
        tmp =input('Do Upgrade? yes or no\n>>')
        if tmp == 'yes':
            download_content(Github_url,path)
            print('Download Complete')
        else:
            pass
    else:
        print('Latest Version\n')