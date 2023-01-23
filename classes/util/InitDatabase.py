import csv

class InitDatabase:
    def __init__(self):
        clean_data = {}
        file = open("dataset\pokemon_csv.csv")
        db = csv.DictReader(file, ["Number", "Name","Type1","Type2","Total","HP","Attack","Defense","SpAtk","SpDef","Speed","Generation","Legendary"])
        for row in db:
            if (row["Name"] == "Name" or len(row["Name"].split()) > 1):
                continue
            else:
                clean_data[row["Name"]] = row
        self.data = clean_data