import telegram
import os



def post_a_photo(photo, chat_id, bot_token):
  bot = telegram.Bot(token=bot_token)

  with open(photo, 'rb') as photo_id:
    bot.send_photo(chat_id, photo_id)