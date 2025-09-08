import requests
import json
import pandas as pd
import re
from saved_search import final

whole_data = {}

def parser(whole_data):
    parsed = {}
    for key, entries in whole_data.items():
        inner_dict = {}
        for entry in entries:
            entry = entry.strip()
            if not entry:  # skip empty strings
                continue
            match = pattern.match(entry)
            if match:
                field, value = match.group(1), match.group(2)
                inner_dict[field] = value if value is not None else None
        parsed[key] = inner_dict
    print("Parsing.")
    return parsed
count = 0
for i in range(len(final)):
    print(count)
    url1 = f""

    responce1 = requests.request("Get",url1)
    data1 = responce1.text
    whole_data.update({final[i]:data1.replace("\r", "").replace("\n", "").split(';')})
    count += 1
# print(whole_data)
pattern = re.compile(r"")
dictonary = parser(whole_data)
print("JSON Parsed.")
print(dictonary)

