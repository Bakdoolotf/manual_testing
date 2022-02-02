import requests
#В словаре остутсвует first_name and "Janet"

def test_01_check_status_code():
    response = requests.get('https://reqres.in/api/single_user')
    js = response.json()
    name = ''
    for i in range(len(js['data'])):
        if js['data'][i]['name'] == 'cerulean':
            name += js['data'][i]['name']
    assert name == 'cerulean'
    assert response.status_code == 200

test_01_check_status_code()
#Запускать через терминал: pytest -v ApiAuthTest.py 