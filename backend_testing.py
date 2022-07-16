import requests

user_id_input = 100
user_name_input = 'daniel'

res = requests.post('http://127.0.0.1:5000/users/{}'.format(user_id_input), json={"user_id":user_id_input, "user_name": user_name_input})
if res.ok:
    print(res.json())

res = requests.get('http://127.0.0.1:5000/users/{}'.format(user_id_input))
if res.ok:
    user_name_output = res.json()['user_name']
    if user_name_output != user_name_input:
        raise Exception("Failed to post user")
    print(user_name_output)

