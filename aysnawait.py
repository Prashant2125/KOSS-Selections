import asyncio
import time
from aiohttp import ClientSession
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

async def sleep_coro(el):
    url=f"https://reqres.in/api/users?page{el}"
    async with ClientSession() as session:
        async with session.get(url) as response:
            data =await response.json()
           
            return data


async def main():
    obj1 = asyncio.create_task(sleep_coro(1))
    obj2 = asyncio.create_task(sleep_coro(2))
    obj3 = asyncio.create_task(sleep_coro(3))

    
    print("fetching data....")
    start = time.time()

    await obj1
    await obj2
    await obj3

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))
    print(obj1)
    print(obj2)
    print(obj3)
    

asyncio.run(main())