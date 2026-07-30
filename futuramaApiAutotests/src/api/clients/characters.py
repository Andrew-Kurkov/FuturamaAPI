suffix_url="api/characters"
def get_character(client,characters_id):
    return client.get(f'{suffix_url}/{characters_id}')
def get_characters_list(client,order_by: str="id",order_by_direction: str="asc",query:str="query",page:int=1,size:int=50,
                   gender: str = None, status:str = None, species: str = None):
    params = {
        'orderBy':order_by,
        'orderByDirection':order_by_direction,
        'query':query,
        'page':page,
        'size':size
    }
    if gender:
        params['gender']=gender
    if status:
        params['status']=status
    if species:
        params['species']=species
    return client.get(suffix_url,params=params)

