import json
import requests
from collections import defaultdict
from craftingclass import Meals

#This is still a work in progress and will be updated as I gain time/knowledge
#Bare with me, I'm new



#payload endpoing
url = "https://xivapi.com/search"

#Headers, duh
headers = defaultdict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

#json payloads meals/meds
meals = {
 "indexes": "item",
 "columns": "Name,Bonuses",
  "body": {
    "query": {
        "bool" : {
            "should" : [
                {"match" : { "Bonuses.CP.Relative" : "true" }},
                {"match" : { "Bonuses.Control.Relative" : "true" }},
                {"match" : { "Bonuses.Craftsmanship.Relative" : "true" }}

            ],
           "must_not": [
                 {"match" : { "ItemSearchCategory.Name_en" : "Medicine" }} 

            ]
        }
    },
    "from": 0,
    "size": 100
}
}

meds = {
 "indexes": "item",
 "columns": "Name,Bonuses",
  "body": {
    "query": {
        "bool" : {
            "should" : [
                {"match" : { "Bonuses.CP.Relative" : "true" }},
                {"match" : { "Bonuses.Control.Relative" : "true" }},
                {"match" : { "Bonuses.Craftsmanship.Relative" : "true" }}

            ],
           "must_not": [
                 {"match" : { "ItemSearchCategory.Name_en" : "Meals" }} 

            ]
        }
    },
    "from": 0,
    "size": 100
}
}


#Save the responses
meals_request = requests.post(url, headers=headers, json=meals)
meds_request = requests.post(url, headers=headers, json=meds)

#Clean it up a bit and prepping for class to convert to ffxiv crafters' data
def clean_up(resp):
    resp = (json.loads(resp.text))
    del resp["Pagination"]
    resp = resp["Results"]
    return resp

meals_request = clean_up(meals_request)
meds_request = clean_up(meds_request)



#print out responses into respective files, and make them if they are not there
with open("Meal.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    my_file.write(json.dumps(meals_request, indent=2, sort_keys=True, ensure_ascii=False))
    my_file.truncate()
with open("Medicine.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    my_file.write(json.dumps(meds_request, indent=2, sort_keys=True, ensure_ascii=False))
    my_file.truncate()