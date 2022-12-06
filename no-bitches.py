import requests
from os import mkdir, sep
from random import randint
from threading import Thread

api = 'https://api.waifu.pics/nsfw/waifu'


def get(directory="bitches", amount=randint(5, 10)):
    '''can choose directory name too'''
    try:
        mkdir(directory)
    except Exception:
        pass
    for i in range(amount):
        Thread(target=bitches, args=(directory, amount)).start()


def bitches(dir_, amount=randint(3, 7)):
    for i in range(amount):
        req_url = requests.get(api)
        url = req_url.json()['url']
        if not req_url.ok:
            print("error: "+req_url)
        with open(dir_+sep+url[21:], 'wb') as f:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                f.write(block)

get()
