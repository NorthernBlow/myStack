from asyncio import exceptions
from pyrogram import Client, filters
from pyrogram.methods.messages import send_message
import requests
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
import time





config = {
        'target_chat_id':-1001461338272
        }


dotenv_path = join(dirname(__file__), '.env')
load_dotenv()


app = Client('monitorbot', api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'), bot_token=environ.get('TOKENTG'))




@app.on_message()
def send_get():
    try:
        r = requests.get('https://projectgranit31.ru')
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(err)
        app.send_message(config['target_chat_id'], err.response.text)
    except requests.exceptions.HTTPError as errh:
        app.send_message(config['target_chat_id'], errh.response.text)
    except requests.exceptions.ConnectionError as errc:
        app.send_message(config['target_chat_id'], errc.response.text)
    except requests.exceptions.Timeout as errt:
        app.send_message(config['target_chat_id'], errt.response.text)
    finally:
        time.sleep(90000)
        #print('вроде все ок')
        #app.send_message(config['target_chat_id'], 'все ок')


def main():
    app.run()

    with app:
        send_get()



if __name__ == '__main__':
    main()
