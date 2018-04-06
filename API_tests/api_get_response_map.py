import requests

url = "https://release.onebox.thezebra.com/api/v3/user_response_map/981332d5-923b-476d-b5d5-91247b6cd1fc/"

payload = "{\"responses\" : {\n    \"start\": {\n        \"currently_insured\": 1\n    },\n    \"vehicles\": [\n        {\n            \"year\": 2016,\n            \"make\": \"Audi\",\n            \"model\": \"A5\",\n            \"ownership\": 1,\n            \"primary_use\": 0,\n            \"miles\": 0,\n            \"garaging_address\": \"Austin, TX 78704\",\n            \"id\": \"vehicles-1384-6ffa-b994-53dfc5b733cb\"\n        }\n    ],\n    \"drivers\": [\n        {\n            \"current_carrier\": 1,\n            \"first_name\": \"Melt\",\n            \"last_name\": \"Game\",\n            \"date_of_birth\": \"09/09/1999\",\n            \"email\": \"meltgame@thezebra.com\",\n            \"phone\": \"(512) 555-1234\",\n            \"gender\": 0,\n            \"marital_status\": 1,\n            \"credit_score\": 1,\n            \"residence_ownership\": 0,\n            \"violations\": {\n                \"value\": 1,\n                \"incidents\": [\n                    {\n                        \"incidentId\": 7,\n                        \"incidentTypeId\": 7\n                    }\n                ]\n            },\n            \"other_applicable\": {}\n        }\n    ],\n    \"discounts\": {\n        \"consecutive_insurance\": 1,\n        \"paperless\": 1,\n        \"auto_pay\": 1,\n        \"diploma\": 1,\n        \"pay_up_front\": 1,\n        \"currently_insured\": 1,\n        \"low_mileage\": 1,\n        \"multi_vehicle\": 1,\n        \"new_car_discount\": 1,\n        \"good_credit\": 1,\n        \"home_owner\": 1,\n        \"condo_owner\": 0,\n        \"no_violations\": 0,\n        \"currently_employed\": 1,\n        \"college_degree\": 1,\n        \"active_military\": 1,\n        \"good_student\": 1\n    }\n}\n}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "9b0ff40a-6e96-4235-ada0-d1ba9a3b446e"
    }

session_id = 'tftbv4i0gpthekhvdxt26o4dmz0tt0i7'
user_cookie = {'sessionid':str(session_id)}

response = requests.request("GET", url, data=payload, headers=headers, cookies=user_cookie)

print(response.text)