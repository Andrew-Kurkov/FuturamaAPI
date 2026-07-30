def get_token(client,grant_type: str=None,username = str,password = str,scope: str=None,client_id: str=None,client_secret: str=None):
    data = {
        'grant_type': grant_type,
        'username': username,
        'password': password,
        'scope': scope,
        'client_id': client_id,
        'client_secret': client_secret
    }
    return client.post('/api/tokens/users/auth', data=data)

def refresh_token(client, refresh_token: str):
    json_body = {
        'refresh_token': refresh_token,
    }
    return client.post('/api/tokens/users/refresh', json=json_body)