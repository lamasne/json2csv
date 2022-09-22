import json
import os
import pandas as pd
from functions import *

# META PARAMETERS
input_path = os.path.normpath("C:/Users/Lamas/workspace/WS_cuy/inputs/")
output_path = os.path.normpath("C:/Users/Lamas/workspace/WS_cuy/outputs/")
input_file = os.path.join(input_path, "json_miembros.txt")
output_file = os.path.join(output_path, "output.csv")

# READ JSON INTO DICTIONNARIES
data = json.load(open(input_file, encoding="utf-8"))

cards_data = data["cards"]
lists_data = data["lists"]
members_data = data["members"]
labels_data = data["labels"]

# CHANGE FOREIGN KEYS (FK'S)
cards_data = change_foreign_keys(cards_data, lists_data, "idList", "name")
cards_data = change_multiple_foreign_keys(
    cards_data, members_data, "idMembers", "fullName"
)
cards_data = change_multiple_foreign_keys(cards_data, labels_data, "idLabels", "name")

# FORMAT DATES
for field_name in ["start", "dateLastActivity", "due"]:
    cards_data = format_date(cards_data, field_name)

# SELECT ATTRIBUTES OF INTEREST AND CHOOSE THEIR LABELS
fields_of_interest = {
    "name": "NAME CARD",
    "idList": "LIST NAME",
    "idMembers": "MEMBERS NAMES",
    "idLabels": "LABELS NAMES",
    # "id": "CARD ID",
    "start": "START DATE",
    "dateLastActivity": "LAST ACTIVITY DATE",
    "due": "DUE DATE",
    "shortUrl": "SHORT URL",
    "url": "URL",
}

df = pd.DataFrame.from_records(cards_data, columns=fields_of_interest.keys())
df.rename(fields_of_interest, axis=1, inplace=True)

# MAKE CSV (with right labels)
df.to_csv(output_file, index=False, encoding="utf-8-sig")
