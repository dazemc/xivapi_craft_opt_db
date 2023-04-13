import requests
import json
from Buffs import *

# Endpoint
url = "https://xivapi.com/search"
buff_type = ["Medicine", "Meal"]
buff_name = "Meal"

for buff in buff_type:
    buffs = []

    params = {
        "indexes": "item",
        "columns": "Name,Bonuses,Name_en,Name_de,Name_fr,Name_ja",
        "body": {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"Bonuses.CP.Relative": "true"}},
                        {"match": {"Bonuses.Control.Relative": "true"}},
                        {"match": {"Bonuses.Craftsmanship.Relative": "true"}}

                    ],
                    "must_not": [
                        {"match": {"ItemSearchCategory.Name_en": buff}}

                    ]
                }
            },
            "from": 0,
            "size": 100
        }
    }
    request = requests.post(url, json=params)
    request.raise_for_status()
    # print(request.text)

    for i in request.json()["Results"]:
        s_cp_percent = i.get("Bonuses", {}).get("CP", {}).get("Value")
        s_cp_value = i.get("Bonuses", {}).get("CP", {}).get("Max")
        s_craft_percent = i.get("Bonuses", {}).get("Craftsmanship", {}).get("Value")
        s_craft_value = i.get("Bonuses", {}).get("Craftsmanship", {}).get("Max")
        s_control_percent = i.get("Bonuses", {}).get("Control", {}).get("Value")
        s_control_value = i.get("Bonuses", {}).get("Control", {}).get("Max")
        s_name = i.get("Name")
        s_name_de = i.get("Name_de")
        s_name_fr = i.get("Name_fr")
        s_name_ja = i.get("Name_ja")

        new_item = vars(
            Buffs(s_cp_percent, s_cp_value, s_craft_percent, s_craft_value, s_control_percent, s_control_value, s_name, s_name_de, s_name_fr, s_name_ja))

        # Remove None values from previous step
        for v in list(new_item):
            if new_item[v] is None:
                new_item.pop(v)
        buffs.append(new_item)

    with open(f"{buff_name}.json", mode="w", encoding="utf-8") as my_file:
        my_file.seek(0)
        my_file.write(json.dumps(buffs, indent=2, sort_keys=True, ensure_ascii=False))

    # This is for the second iteration
    buff_name = "Medicine"
