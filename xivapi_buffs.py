import json
import requests
from requests.structures import CaseInsensitiveDict

#This is still a work in progress and will be updated as I gain time/knowledge
#Bare with me, I'm new

#payload endpoing
url = "https://xivapi.com/search"

#Headers, duh
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

#json payloads meals/meds
meals = """
{
 "indexes": "item,achievement,instantcontent",
 "columns": "Name",
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
"""
meds = """
{
 "indexes": "item,achievement,instantcontent",
 "columns": "Name",
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
"""

#Save the responses
meals_request = requests.post(url, headers=headers, data=meals)
meds_request = requests.post(url, headers=headers, data=meds)

#print out responses into respective files, and make them if they are not there
with open("Meal.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    json.dump(meals_request.json(), my_file, indent=2, sort_keys=True, ensure_ascii=False)
    my_file.truncate()
with open("Medicine.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    json.dump(meds_request.json(), my_file, indent=2, sort_keys=True, ensure_ascii=False)
    my_file.truncate()