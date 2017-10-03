from flask import Flask, request
import requests
import json
import traceback
import random
import os

from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.data)
    #         print ('data: ', data)
    #         print ('request.data: ', request.data)
    #     except:
    #         print ('error?')
    # elif request.method == 'GET':
    #     print('get')
    #     print (request.data)
    #     return 'get'
    # return 'all fails\n'
    if request.method == 'POST':
        data = request.get_json()

        if data['name'] != 'My Man':
            # msg = '{}, you sent "{}".'.format(data['name'], data['text'])
            msg = 'https://media.giphy.com/media/qPVzemjFi150Q/giphy.gif'
            send_message(msg)
    elif request.method == 'GET':
        msg = 'https://media.giphy.com/media/3o7aCUqs54taGzqDWU/giphy.gif'
        send_message(msg)

    return ("My Man!!")

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('BOT_ID'),
        'text'   : msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


if __name__ == '__main__':
    app.run()
    
