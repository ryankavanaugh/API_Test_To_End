import requests
import json
import selenium
from selenium import webdriver

#

# GET SESSION ID AND QUOTE ID
# use visit API
print('\n' + 'GET SESSION ID AND QUOTE ID:')
url = "https://release.onebox.thezebra.com/api/internal/v1/quote/session-based/"
initial_response = requests.request("GET", url)

print(initial_response.status_code)

initial_json = initial_response.text
json1_data = json.loads(initial_json)
# print('Quote ID:')
quote_id = json1_data.get('id')
# print(quote_id)

print('Session ID:')
session_id = json1_data.get('session_id')
print(session_id)


# CREATE A USER
print('\n' + 'CREATE A USER:')
create_user_url = "https://release.onebox.thezebra.com/api/v3/users/"
querystring = {"funnel_schema":"3"}
create_user_headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }
user_cookie = {'sessionid':str(session_id)}
create_user_response = requests.request("POST", create_user_url, headers=create_user_headers, cookies=user_cookie, params=querystring)
print(create_user_response.status_code)


# GET CREATED USER
print('\n' + 'GET CREATED USER:')
get_created_user_url = "https://release.onebox.thezebra.com/api/v3/users/current/"
querystring = {"foo":"bar"}
get_created_user_headers = {
    'Cache-Control': "no-cache",
    }
get_created_user_response = requests.request("GET", get_created_user_url, headers=get_created_user_headers, cookies=user_cookie, params=querystring)
print(get_created_user_response.status_code)
# print(get_created_user_response.text)
# print

get_created_user_response_json = json.loads(get_created_user_response.text)

user_id = get_created_user_response_json.get('id')

response_map = get_created_user_response_json.get('current_response_map')

user_cookie_2 = {'sessionid':str(session_id), 'id':user_id}

# SEND PAYLOAD TO API
print('SEND PAYLOAD TO API')
url = response_map

payload = {
    "status": {
        "start": {
            "start": True,
            "complete": True
        },
        "drivers": [
            {
                "details": False,
                "form": True,
                "complete": False
            }
        ],
        "vehicles": [
            {
                "details": True,
                "select": True,
                "complete": True
            }
        ],
        "discounts": {
            "discounts": True,
            "complete": True
        }
    },
    "id": str(user_id),
    "rate_analyzer": response_map + "/rate_analyzer/",
    "responses": {
        "start": {
            "currently_insured": 1
        },
        "drivers": [
            {
                "first_name": "Moo",
                "last_name": "Tester",
                "residence_ownership": 0,
                "credit_score": 1,
                "gender": 0,
                "marital_status": 1,
                "phone": "(512) 555-1234",
                "date_of_birth": "09/09/1989",
                "current_carrier": 1,
                "other_applicable": {},
                "email": "thezebratester@gmail.com"
            }
        ],
        "vehicles": [
            {
                "make": "Audi",
                "id": "vehicles-1384-6ffa-b994-53dfc5b733cb",
                "miles": 0,
                "ownership": 1,
                "year": 2016,
                "model": "A5",
                "garaging_address": "Austin, TX 78704",
                "primary_use": 0
            }
        ],
        "discounts": {
            "paperless": 1,
            "multi_vehicle": 1,
            "condo_owner": 0,
            "consecutive_insurance": 1,
            "active_military": 1,
            "no_violations": 0,
            "diploma": 1,
            "college_degree": 1,
            "pay_up_front": 1,
            "good_credit": 1,
            "home_owner": 1,
            "currently_insured": 1,
            "currently_employed": 1,
            "good_student": 1,
            "low_mileage": 1,
            "auto_pay": 1,
            "new_car_discount": 1
        }
    }
}

payload_test = {"responses":{"start":{"currently_insured":0},"vehicles":[{"vehicle_id":255273,"id":"vehicles-ba28-bd33-b258-001131ed3bba","year":2017,"make":"Audi","model":"A4","submodel":"2.0T Prestige 4dr Sedan","ownership":2,"primary_use":1,"miles":1,"garaging_address":"1122 South Lamar Boulevard"}],"drivers":[{"other_applicable":{},"id":"drivers-f8b4-6191-a4a6-1b7dcd4b60bc","first_name":"Derek","last_name":"Miles","date_of_birth":"09/17/1989","email":"abc@thezebra.com","phone":"(888) 888-8888","gender":0,"marital_status":1,"credit_score":2,"education":1,"residence_ownership":1,"violations":{"value":0,"incidents":[]}}],"discounts":{"currently_insured":0,"low_mileage":0,"multi_vehicle":0,"new_car_discount":1,"good_credit":0,"home_owner":0,"condo_owner":1,"no_violations":1,"currently_employed":1,"active_military":1,"pay_up_front":1,"auto_pay":1,"paperless":1},"zipcode":"78704","city":"Austin","state":"TX"}}

headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }

payload_json = json.dumps(payload_test)

response = requests.request("PUT", url, data=payload_json, headers=headers, cookies=user_cookie)

print(response.status_code)
print

# OPEN BROWSER AND INJECT COOKIE
print('OPEN BROWSER, INJECT COOKIE, HEAD TO START PAGE')
driver = webdriver.Chrome()
driver.get('https://release.onebox.thezebra.com/')
driver.delete_cookie('sessionid')
driver.add_cookie({'name': 'sessionid', 'value' : session_id})
# driver.get('https://release.onebox.thezebra.com/z/questions/start/')
# driver.get('https://release.onebox.thezebra.com/z/summary/')
driver.get('https://release.onebox.thezebra.com/z/rate-select')
# driver.get('https://release.onebox.thezebra.com/z/summary/')