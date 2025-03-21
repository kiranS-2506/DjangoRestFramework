import requests
base_url = "http://127.0.0.1:8000/"
def api_view1():
    end_url = 'apijson1/'
    resp = requests.get(base_url+end_url)
    print(resp.json())
def api_view2():
    end_url = 'apijson2/'
    resp = requests.get(base_url+end_url)
    print(resp.json())
api_view1()
api_view2()