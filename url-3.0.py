import requests
import os
url="https://iw233.cn/API/Random.php"
n=int(input('下载次数:'))
def geturl():
    r=requests.get(url,allow_redirects=False)
    url_s=r.headers.get('location')
    os.system('aria2c '+url_s)
    #os.system('cls')
for i in range (1,n+1,1):
    geturl()
print("{:-^40}".format("下载完成"))