import requests
import random
import os
from dotenv import load_dotenv
from telegram_bot import post_a_photo


def download_the_comic():

        current_com_url = 'https://xkcd.com/info.0.json'

        response = requests.get(current_com_url)
        response.raise_for_status()
        max_num = response.json()['num']
        comic_num = random.randint(1, max_num)

        comic = f'https://xkcd.com/{comic_num}/info.0.json'
        comic_response = requests.get(comic)
        comic_response.raise_for_status()

        img_url = comic_response.json()['img']
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        with open('comic.png', 'wb') as file:
                file.write(img_response.content)

  
def main():
        try:
                load_dotenv()
                bot_token = os.environ['TELEGRAM_TOKEN']
                chat_id= os.environ['TELEGRAM_CHAT_ID']

                download_the_comic()
                post_a_photo('comic.png', chat_id, bot_token)
        
        finally:
                os.remove('comic.png')


if __name__ == '__main__':
        main()
