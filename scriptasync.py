import asyncio
import aiohttp
import time
import json

from functools import wraps
 
from asyncio.proactor_events import _ProactorBasePipeTransport
 
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper
 
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)




start = time.time()

def get_tasks(session):
    tasks = []
    for i in range(1,201):
        tasks.append(asyncio.create_task(session.get(f'https://xkcd.com/{i}/info.0.json')))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            f=open("jsonurlstorage.txt","a")
            f.write(json.dumps(await response.json(),indent =2))

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds".format(total_time))
#It took 6.260153293609619 seconds

