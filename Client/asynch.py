import asyncio
import winsound
import requests
from datetime import datetime

async def periodic():
    while True:
        # get the api call here
        try:
            response = requests.get("http://10.0.0.193:7238/waterreminder")
            formatedTime = datetime.now().strftime("%I:%M:%S %p")
            status = response.json()
            print(formatedTime, "- Remind status: ", status)
            if (status) :
                delay = 5
                winsound.PlaySound("Client\\sicko.wav", winsound.SND_ASYNC)
            else:
                delay = 300
        except requests.ConnectionError:
            delay = 300
            print(datetime.now(),"- Network error")

        await asyncio.sleep(delay)

loop = asyncio.get_event_loop()
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
