import requests,json
Base_url = "http://127.0.0.1:8000/"
End_point = 'api/'
def get_data(id=None):
    data = {}
    if id is not None:
        data ={
            'id':id
        }
    resp = requests.get(Base_url+End_point,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#get_data(4)


def post_data(data):
    resp = requests.post(Base_url+End_point,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

new_emp = {
    'eno':105,
    'ename':'Radhika',
    'esal':19000,
    'eadd':'Delhi'
    }
#post_data(new_emp)
def update_resource(id):
    new_emp = {
    'id':id,
    'ename':'RGV'

    }
    resp = requests.put(Base_url+End_point,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#update_resource(5)
def delete_resource(id):
    data = {
    'id':id,
    }
    resp = requests.delete(Base_url+End_point,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#delete_resource()