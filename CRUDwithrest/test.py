import requests,json
Base_url = "http://127.0.0.1:8000/"
End_point = 'api'
def get_data(id=None):
    data = {}
    if id is None:
        data ={
            'id':id
        }
    resp = requests.get(Base_url+End_point,data=data)
    print(resp.status_code)
    print(resp.json())
get_data()