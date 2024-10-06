from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine


class ConnectorNotFound(Exception):
    '''Не корректный коннектор'''

    def __str__(self) -> str:
        return 'Введен не корректный коннектор'


class Urls:
    __USERNAME = 'root'
    __PASSWORD = 'ZXCPUDGE228NEKITvip123' #ZXCPUDGE228 на Kubuntu
    __HOST = '127.0.0.1'
    __DB_NAME = 'elections'
    __PORT = 3306
    
    def __init__(self, type_engine: str = 'async') -> None:
        if type_engine == 'async':
            self.engine = create_async_engine(self.async_connect)
            
        elif type_engine == 'simple':
            self.engine = create_engine(self.simple_connect)
            
        else:
            raise ConnectorNotFound()
        
    @property
    def simple_connect(self):
        return f'mysql+pymysql://{self.__USERNAME}:{self.__PASSWORD}@{self.__HOST}/{self.__DB_NAME}'
    
    @property
    def async_connect(self):
        return f'mysql+aiomysql://{self.__USERNAME}:{self.__PASSWORD}@{self.__HOST}:{self.__PORT}/{self.__DB_NAME}'