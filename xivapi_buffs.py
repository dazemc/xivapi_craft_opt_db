import json
import requests
from collections import defaultdict
from craftingclass import Buffs

# Almost there!

# payload endpoint
url = "https://xivapi.com/search"

# Headers, duh
headers = defaultdict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

# json payloads meals/meds
meals = {
    "indexes": "item",
    "columns": "Name,Bonuses",
    "body": {
        "query": {
            "bool": {
                "should": [
                    {"match": {"Bonuses.CP.Relative": "true"}},
                    {"match": {"Bonuses.Control.Relative": "true"}},
                    {"match": {"Bonuses.Craftsmanship.Relative": "true"}}

                ],
                "must_not": [
                    {"match": {"ItemSearchCategory.Name_en": "Medicine"}}

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
            "bool": {
                "should": [
                    {"match": {"Bonuses.CP.Relative": "true"}},
                    {"match": {"Bonuses.Control.Relative": "true"}},
                    {"match": {"Bonuses.Craftsmanship.Relative": "true"}}

                ],
                "must_not": [
                    {"match": {"ItemSearchCategory.Name_en": "Meals"}}

                ]
            }
        },
        "from": 0,
        "size": 100
    }
}

# Save the responses
meals_request = requests.post(url, headers=headers, json=meals)
meds_request = requests.post(url, headers=headers, json=meds)


# Clean it up a bit and prepping for class to convert to ffxiv crafters' data
def clean_up(resp):
    resp = (json.loads(resp.text))
    del resp["Pagination"]
    resp = resp["Results"]
    return resp


# Rename keys
def shuffle(buff):
    for i in range(len(buff)):
        if i <= 0:
            temp_list = []
        else:
            s_cp_percent = buff[i].get("Bonuses", {}).get("CP", {}).get("Value")
            s_cp_value = buff[i].get("Bonuses", {}).get("CP", {}).get("Max")
            s_craft_percent = buff[i].get("Bonuses", {}).get("Craftsmanship", {}).get("Value")
            s_craft_value = buff[i].get("Bonuses", {}).get("Craftsmanship", {}).get("Max")
            s_control_percent = buff[i].get("Bonuses", {}).get("Control", {}).get("Value")
            s_control_value = buff[i].get("Bonuses", {}).get("Control", {}).get("Max")
            s_name = buff[i].get("Name")
            temp_list.append(vars(
                Buffs(s_cp_percent, s_cp_value, s_craft_percent, s_craft_value, s_control_percent, s_control_value,
                      s_name)))
    return temp_list


# Calls
meds_request = clean_up(meds_request)
meals_request = clean_up(meals_request)
meds = shuffle(meds_request)
meals = shuffle(meals_request)

# TODO: Remove None values

# print out responses into respective files, and make them if they are not there
with open("Meal.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    my_file.write(json.dumps(meals, indent=2, sort_keys=True, ensure_ascii=False))
    my_file.truncate()
with open("Medicine.json", mode="w+", encoding="utf-8") as my_file:
    my_file.seek(0)
    my_file.write(json.dumps(meds, indent=2, sort_keys=True, ensure_ascii=False))
    my_file.truncate()
