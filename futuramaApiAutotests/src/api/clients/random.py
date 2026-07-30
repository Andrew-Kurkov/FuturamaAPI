suffix_url="api/random"
def get_random_character(client):
    return client.get(f'{suffix_url}/character')
def get_random_episode(client):
    return client.get(f'{suffix_url}/episode')
def get_random_season(client):
    return client.get(f'{suffix_url}/season')