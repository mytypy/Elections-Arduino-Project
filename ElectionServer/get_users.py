import asyncio
import aiohttp
from random import randint
from asgiref.sync import sync_to_async


peoples = {}
semaphore = asyncio.Semaphore(10)


async def get_user():
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            response = await session.get('https://api.randomdatatools.ru/?count=1&gender=unset&params=LastName,FirstName,FatherName')
            response_json = await response.json(content_type=None)
            name = f'{response_json['LastName']} {response_json['FirstName']} {response_json['FatherName']}'
            peoples[name] = name
    

@sync_to_async
def to_db():
    
    for i in peoples:
        UserModel.objects.create(id_card=peoples[i], choice_id=randint(1, 2), election_id=1)
        

async def main():
    tasks = [asyncio.create_task(get_user(), name=randint(1, 1000000000)) for _ in range(1000)]
    
    await asyncio.gather(*tasks)
    await to_db()
            
        
asyncio.run(main())

