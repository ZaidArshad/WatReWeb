import asyncio
import winsound
import requests
from datetime import datetime

async def periodic():
    while True:
        # get the api call here
        try:
            response = requests.get("IPV4_ADDRESS/waterreminder")
            formatedTime = datetime.now().strftime("%I:%M:%S %p")
            status = response.json()
            print(formatedTime, "- Remind status: ", status)
            if (status) :
                delay = 5
                winsound.PlaySound("Client\\sicko.wav", winsound.SND_ASYNC)
            else:
                delay = 300
            await asyncio.sleep(delay)
        except requests.ConnectionError:
            print(datetime.now(),"- Network error")

loop = asyncio.get_event_loop()
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
