'''
Pine64 Chat FAQ Bot
A very simple Matrix bot built on the matrix-nio API

Made by Matthew Petry (fireTwoOneNine/fire219)
Based on matrix-nio code examples

See LICENSE.md
'''

import asyncio
from nio import (AsyncClient, RoomMessageText)
import json
import sys
import urllib.request
import os

with open('login.json') as loginfile:
    logindata = json.load(loginfile)
    
with open('faq.json') as faqfile:
    faqdata = json.load(faqfile)

client = AsyncClient(logindata["homeserver"], logindata["username"])

async def sendMessage(room, responseText):
    await client.room_send(
        room_id=room.machine_name,
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "body": responseText
        }
    ) 

async def FAQreload(room):
    urllib.request.urlretrieve("https://github.com/fire219/pine-faq-bot/raw/master/faq.json", "newfaq.json")
    try:
        with open('newfaq.json') as faqtestfile:
            faqtestdata = json.load(faqtestfile)
        os.replace("newfaq.json", "faq.json")
        faqdata = faqtestdata
        await sendMessage(room, "[FAQbot] New FAQ file successfully loaded!")
    except JSONDecodeError:
        await sendMessage(room, "[FAQbot] New FAQ file failed to load. Please check the JSON file on the repository for malformation.")
        

async def message_cb(room, event):
    if (event.body.startswith('!faq')):       
        try:
            if (event.body == "!faq shutdown" and event.sender == "@fire219:matrix.org"):
                print("shutting down by request")
                await sendMessage(room, "[FAQbot] Shutting down!")
                await client.close()
                sys.exit(0)
            if (event.body == "!faq reload"):
                await sendMessage(room, "[FAQbot] Now pulling latest FAQ file from repository...")
                await FAQreload(room)
            else:
                responseText = faqdata[event.body[5:]]
                await sendMessage(room, responseText)
        except KeyError:
            await sendMessage(room, "I could not find a response for your query.")
        

async def main():
    await client.login(logindata["password"])
    print("Logged in. Doing initial sync.")
    await client.sync(timeout=5000)
    print("Synchronized. Awaiting messages.")
    client.add_event_callback(message_cb, RoomMessageText)
    await client.sync_forever(timeout=30000)

asyncio.get_event_loop().run_until_complete(main())