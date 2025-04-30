import requests


data = {
    'id_card': 1231,
    'election': 5,
    'choice': 7
}
req = requests.post('http://127.0.0.1:8000/api/user/post_user_election/', json=data)
print(req.json())