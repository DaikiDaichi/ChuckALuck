import json
from objects import konto

with open("assets/profile.json", "r") as readfile:
    json_data = json.load(readfile)
    for x, i in enumerate(json_data["konten"]):
        if i["owner"] == konto.getAttr()[0]:
            print(json_data["konten"][x])
            del json_data["konten"][x]

    if konto.getAttr()[0] != "Demo":
        json_data["konten"].append({"owner": konto.getAttr()[0], "balance": konto.getAttr()[1]})

with open("assets/profile.json", "w") as wfile:
    json.dump(json_data, wfile)
