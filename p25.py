import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from fake_useragent import UserAgent


u = "http://cbseresults.nic.in/Jee_main_pzy/jee_cbse_2018.htm"


# while True:

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
post_parm = {
        "regno":17825558,
        "dob":"21/09/1997"
    }

ua = UserAgent()

print(ua.random)
header = {'User-Agent':str(ua.chrome)}
print(header)

r = requests.post(url=u,headers=header,data=post_parm)

soup = BeautifulSoup(r.text,'html.parser')

print(r)
