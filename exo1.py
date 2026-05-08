import json
import csv

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("resultat.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["reel", "imaginaire"])

    for nombre in data:
        writer.writerow(nombre)