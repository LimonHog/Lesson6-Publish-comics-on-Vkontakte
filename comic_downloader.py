import requests
import random
import os
import telegram
from telegram_bot import post_a_photo


def download_the_comic():

        current_com_url = 'https://xkcd.com/info.0.json'

        response = requests.get(current_com_url)
        response.raise_for_status()
        max_num = response.json()['num']
        comic_num = random.randint(1, max_num)

        different_comic = f'https://xkcd.com/{comic_num}/info.0.json'
        dif_res = requests.get(different_comic)

        img_url = dif_res.json()['img']
        img_res = requests.get(img_url)
        with open(f'comic{comic_num}.png', 'wb') as file:
                file.write(img_res.content)
        post_a_photo(f'comic{comic_num}.png')
        os.remove(f'comic{comic_num}.png')

download_the_comic()




