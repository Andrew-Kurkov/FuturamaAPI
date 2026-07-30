suffix_url='/api/users'
def get_users_list(client,query: str = 'query',page: int = 1, size: int = 50):
    params = {
        'query': query,
        'page': page,
        'size': size,
    }
    return client.get(f'{suffix_url}', params=params)
def post_users(client, name: str,surname: str, middle_name: str, email: str,username: str, password: str, is_subscribed: bool =True):
    json_body = {
        'name': name,
        'surname': surname,
        'middleName': middle_name,
        'email': email,
        'username': username,
        'password': password,
        'isSubscribed': is_subscribed
    }
    return client.post(suffix_url, json=json_body)
def get_user_info(client,access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    return client.get(f"{suffix_url}/me", headers=headers)
def change_user_info(client,access_token: str, name: str =None, Surname: str =None, Middlename: str =None, Password: str =None, Issubscribed: bool = None):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    json_body = {}
    if name:
        json_body['name'] = name
    if Surname:
        json_body['surname'] = Surname
    if Middlename:
        json_body['middleName'] = Middlename
    if Password:
        json_body['password'] = Password
    if Issubscribed:
        json_body['isSubscribed'] = Issubscribed
    return client.put(suffix_url,headers=headers, json=json_body)
