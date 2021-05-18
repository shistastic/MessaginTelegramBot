# importing all required libraries
import threading
from datetime import datetime, timedelta

import self as self
import telebot

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChat
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above
api_id = '4852532'
api_hash = '48cf551752e62a83effed8c43572151b'
token = '1841907425:AAEZNALnsRMSxUgWpxcNBI6pESSeiDyZ_ws'

# your phone number
phone = '+34693577989'

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    # receiver = InputPeerUser(-1001460601299, 231412)

    receiver = InputPeerUser(360376414, 231412)

    # Set Time Delay
    # now = datetime.now()
    # run_at = now + timedelta(seconds=10)
    # delay = (run_at - now).total_seconds()
    # print('dsafa1')

    # sending message using telegram client
    # threading.Timer(delay, self.update).start()
    # print('dsafa')

    for i in range(1000):
        client.send_message(receiver, 'Suerte x100 en los examenes nati! ^^', parse_mode='html')

except Exception as e:

    # there may be many error coming in while like peer
    # error, wwrong access_hash, flood_error, etc
    print(e)

# disconnecting the telegram session
client.disconnect()
