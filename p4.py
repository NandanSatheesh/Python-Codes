import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


message = input("Enter a text message to start talking with Mitsuku!\n\nYou : ")

u = "https://kakko.pandorabots.com/pandora/talk?botid=87437a824e345a0d&skin=chat"


while True:


    post_parm = {
        "message":message
    }



    r = requests.post(url=u,data=post_parm)

    soup = BeautifulSoup(r.text,'html.parser')

    l1 = ['test element']

    for i in soup.find_all('p'):
        l1.append(i.get_text())


    l1 = l1[1:]
    reply = l1[0].strip()


    try:
        reply = reply[reply.index(message) + len(message) :].strip()
        reply = reply[:reply.index("You -")].strip()

        print(reply)
        print("\n\n")

    except:
        print("Conncetion Error. Poor Response Time!\n\n")

    message = input("You : ")
