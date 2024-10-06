from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy import insert
from urls import Urls
from models import User, UserElection, Elections, ElectionsChoose


class Requests:
    
    def __init__(self) -> None:
        self.urls = Urls()
    
    @staticmethod
    def get_user(func) -> User|None:
        async def wrapper(*args, **kwargs) -> None:
            self = args[0]
            
            session = async_sessionmaker(self.urls.engine)
            
            try:
                async with session() as session:
                    user = await session.get(User, kwargs['user_id'])
                    
                    if bool(user) is False and func:
                        return await func(self, kwargs['user_id'])
                    else:
                        return user
                    
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