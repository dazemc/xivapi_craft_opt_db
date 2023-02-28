import requests
import json
from Buffs import Buffs

# Endpoint
url = "https://xivapi.com/search"
buff_type = ["Medicine", "Meals"]
buff_name = "Meals"

for buff in buff_type:
    buffs = []

    params = {
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

    for i in request.json()["Results"]:
        s_cp_percent = i.get("Bonuses", {}).get("CP", {}).get("Value")
        s_cp_value = i.get("Bonuses", {}).get("CP", {}).get("Max")
        s_craft_percent = i.get("Bonuses", {}).get("Craftsmanship", {}).get("Value")
        s_craft_value = i.get("Bonuses", {}).get("Craftsmanship", {}).get("Max")
        s_control_percent = i.get("Bonuses", {}).get("Control", {}).get("Value")
        s_control_value = i.get("Bonuses", {}).get("Control", {}).get("Max")
        s_name = i.get("Name")

        new_item = vars(
            Buffs(s_cp_percent, s_cp_value, s_craft_percent, s_craft_value, s_control_percent, s_control_value, s_name))

        # Remove None values from previous step
        for v in list(new_item):
            if new_item[v] is None:
                new_item.pop(v)
        buffs.append(new_item)

    with open(f"{buff_name}.json", mode="w", encoding="utf-8") as my_file:
        my_file.seek(0)
        my_file.write(json.dumps(buffs, indent=2, sort_keys=True, ensure_ascii=False))

    buff_name = "Medicine"
