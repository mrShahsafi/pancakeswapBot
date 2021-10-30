from telethon.tl.functions.contacts import ResolveUsernameRequest

from telethon import TelegramClient, events, sync
# from telethon.sync import
from telethon.tl.functions.messages import GetHistoryRequest

import time
import asyncio
# # client = TelegramClient(
# #      'theFirst1819171',
# #      api_id=17791841,
# #      api_hash='fcdba5b1239da35a71d7e90ed6bb291d'
# # )
# # client.start()
#
#
#
# client = TelegramClient('session_name',
#                    api_id = 17791841,
#                    api_hash = 'fcdba5b1239da35a71d7e90ed6bb291d',
#                    # update_workers=1,
#                    # spawn_read_thread=False
#                    )
# assert client.start()
# if not client.is_user_authorized():
#     client.send_code_request(phone_number)
#     me = client.sign_in(phone_number, input('Enter code: '))
#
channel_username='vchannel16' # your channel
#
# channel_entity=client.get_entity(
#     channel_username
# )
#
# posts = client(GetHistoryRequest(
#     peer=channel_entity,
#     limit=100,
#     offset_date=None,
#     offset_id=0,
#     max_id=0,
#     min_id=0,
#     add_offset=0,
#     hash=0))
#
# # messages = client.get_messages('vchannel16')
#
# for _ in posts.messages:
#     print(_)
#
# while True:
#      time.sleep(2)
# response = client.invoke(ResolveUsernameRequest("IranintlTV"))
# print(response.channel_id)
# print(response.access_hash)


client = TelegramClient(
    'YOUR_SESSION_NAME',
     17791841,
    'fcdba5b1239da35a71d7e90ed6bb291d',
)
client.start()

@client.on(events.NewMessage())
async def main(event):
    channel = await client.get_entity(channel_username)
    messages = await client.get_messages(channel, limit= None) #pass your own args
    # await asyncio.sleep(5)
    # print(event.message)
    # #then if you want to get all the messages text
    for x in messages:
        print(x.text) #return message.text


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

while True:
    time.sleep(2)