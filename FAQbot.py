'''
Pine64 Chat FAQ Bot
A very simple Matrix bot built on the matrix-nio API

Made by Matthew Petry (fireTwoOneNine/fire219) and contributors
This version is maintained and developed by FantasyCookie17
Based on matrix-nio code examples

See LICENSE.md
'''

import asyncio
from nio import (AsyncClient, RoomMessageText)
import json
import re

with open('login.json') as loginfile:
    logindata = json.load(loginfile)
    
with open('faq.json') as faqfile:
    faqdata = json.load(faqfile)

client = AsyncClient(logindata["homeserver"], logindata["username"])

async def sendMessage(room, responseText):
    await client.room_send(
        room_id=room.room_id,
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "format": "org.matrix.custom.html",
            "body": "[FAQbot] " + responseText,
            "formatted_body": "[FAQbot] <em>"+responseText+"</em>"
        }
    ) 

async def FAQupdate(room):
    global faqdata
    await asyncio.create_subprocess_shell("git pull")
    await sendMessage(room, "Pulled from repository.")
    try:
        faqtest = json.loads(stdout.decode())
        with open("faq.json") as faqtest:
            json.load(faqtest)
        faqdata = faqtest
        await sendMessage(room, "New FAQ file successfully loaded!")
    except JSONDecodeError:
        await sendMessage(room, "New FAQ file failed to load. Please check the JSON file on the repository for malformation.")
        

async def message_cb(room, event):
    bridge_prefix = r'^\[.\] <[^>]+> '
    if (re.match(bridge_prefix, event.body) is not None):
        event.body = re.sub(bridge_prefix, '', event.body)

    if (event.body.startswith('!faq')):
        try:
            if (event.body == "!faq shutdown" and event.sender == logindata["botadmin"]):
                print("shutting down by request")
                await sendMessage(room, "Shutting down!")
                await client.close()
                sys.exit(0)
            elif ("!faq update" in event.body):
                await sendMessage(room, "Pulling latest changes from repository...")
                await FAQupdate(room)
            elif (event.body == "!faq"):
                await sendMessage(room, "All loaded topics: " + ", ".join(faqdata.keys()))
            else:
                parseIndex = event.body.index("!faq")
                responseText = faqdata[event.body[parseIndex + 5:].lower()]
                await sendMessage(room, responseText)
        except KeyError:
            await sendMessage(room, "The question you requested does not exist.")
        

async def main():
    await client.login(logindata["password"])
    print("Logged in. Doing initial sync.")
    await client.sync(timeout=5000)
    print("Synchronized. Awaiting messages.")
    client.add_event_callback(message_cb, RoomMessageText)
    await client.sync_forever(timeout=30000)

asyncio.get_event_loop().run_until_complete(main())
