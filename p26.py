import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen



u = "http://results.vtu.ac.in/vitavirevalresultcbcs/index.php"



post_parm = {
        "lns":"1BG15CS059",
    }



r = requests.post(url=u,data=post_parm)

soup = BeautifulSoup(r.text,'html.parser')

print(r.text)