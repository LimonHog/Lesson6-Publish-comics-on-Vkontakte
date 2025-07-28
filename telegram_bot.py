import telegram
import os



def post_a_photo(photo):
  bot_token = os.environ['TELEGRAM_TOKEN']
  bot = telegram.Bot(token=bot_token)
  chat_id= os.environ['TELEGRAM_CHAT_ID']

  with open(photo, 'rb') as photo_id:
    bot.send_photo(chat_id, photo_id)