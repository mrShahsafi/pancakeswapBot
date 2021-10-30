import telepot
from telepot.loop import MessageLoop
import time
from config import (TELEGRAM_KEY,TELEGRAM_GROUP_ID)
from cakebot import (exchange_maker)

bot = telepot.Bot(TELEGRAM_KEY)


def on_chat_message(msg):   # Ver 2.1   26-Oct-2021
    # u = next(item for item in users if item['telegramId'] == msg['from']['id'])
    if msg["chat"]["id"] != -1001614604812:
        return

    # content_type, chat_type, chat_id = telepot.glance(msg)

    if 'edit_date' in msg:
        # به این معنی است که کاربر یک پیام قبلی را در بات، ادیت کرده است
        # این ادیت، غیرمجاز محسوب می شود
        bot.sendMessage(msg['from']['id'], "🚫 Sorry! You're NOT allowed to edit messages here! Hint: Please follow the command 'change'.", reply_to_message_id=msg['message_id'])
        return

    if time.time() - msg['date'] >= 5:
        bot.sendMessage(msg['from']['id'], "🚫 Sorry! You're msg recieved late. Plz try again.", reply_to_message_id=msg['message_id'])
        return
    com = msg['text'].lower()
    print(msg)
    # calling the trader bot
    token_contract, network, amount = msg["text"].split()
    exchange_maker(
        network,
        token_contract,
        amount
    )


'''msg = {
     'message_id': 30,
     'from':
        {'id': 280073886,
          'is_bot': False,
          'first_name': 'amirosen',
          'username': 'MRshahsafi'
        },
    'chat': {
      'id': -1001614604812,
      'title': 'PlatoonReward',
      'type': 'supergroup'
    },
     'date': 1635355800,
    'text': 'ox2525 eth'
  }'''
MessageLoop(
    bot, {'chat': on_chat_message}
).run_as_thread()

while True:
    time.sleep(2)
