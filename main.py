import asyncio
from requests import Requests
from models import UserElection, Elections, ElectionsChoose


async def get_user(user_id: int) -> None:
    '''Получаем пользователя по user_id'''
    requests = Requests()
    inner = requests.get_user(None)
    user = await inner(requests, user_id=user_id)
    print(user)


async def get_user_other_info(user_id: int) -> None:
    '''Получаем остальную информацию'''
    requests = Requests()
    inner = requests.get_user(None)
    user = await inner(requests, user_id=user_id)
    if user:
        user_election: UserElection = user.to_election[0]
        elections_for_user: Elections = user_election.election_id.name
        choose_election_user: ElectionsChoose = user_election.choose_id.name
        print(f'''
Пользователь проголосовал в |-> {elections_for_user} <-|
Голос пользователя: {choose_election_user}''')
    else:
        print('Такого пользователя не существует')


async def set_user(user_id: int) -> None:
    '''Регистрируем пользователя по id'''
    requests = Requests()
    await requests.set_user(user_id=user_id)


asyncio.run(set_user(2))