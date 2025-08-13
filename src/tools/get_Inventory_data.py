import requests



def get_inventory_data():
    
    
    res = requests.get("http://127.0.0.1:8583/store").text
    
    print(res)