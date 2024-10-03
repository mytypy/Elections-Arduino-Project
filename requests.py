import asyncio
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy import insert
from urls import Urls
from models import User, UserElection, Elections, ElectionsChoose


class Requests:
    
    def __init__(self) -> None:
        self.urls = Urls()
    
    def get_user(func) -> User|None:
        async def wrapper(*args, **kwargs) -> None:
            self = args[0]
            
            session = async_sessionmaker(self.urls.engine)
            
            try:
                async with session() as session:
                    user = await session.get(User, kwargs['user_id'])
                    if bool(user) is False:
                        return await func(self, kwargs['user_id'])
                    
                    
            finally:
                await self.urls.engine.dispose()
        return wrapper
    
    @get_user
    async def set_user(self, user_id: int) -> bool:
        session = async_sessionmaker(self.urls.engine)
        
        async with session() as session:
            query = insert(User).values(idCard=user_id)
            await session.execute(query)
            await session.commit()
    
    async def get_debug_user(self, user_id: int):
        session = async_sessionmaker(self.urls.engine)
        
        try:
            async with session() as session:
                user = await session.get(User, user_id)
                return user
        finally:
            await self.urls.engine.dispose()
 

async def main():
    requests = Requests()
    user = await requests.get_debug_user(1)
    user_election: UserElection = user.to_election[0]
    elections_for_user: Elections = user_election.election_id
    choose_election_user: ElectionsChoose = user_election.choose_id
    print(choose_election_user.name)
    
    
asyncio.run(main())