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
    url1 = f"https://asiapacificbreweriestest.agiloft.com/ewws/EWSearch?$KB=Asia Pacific Breweries Test&$table=contract&$login=Admin1&$password=Integration@2025&$lang=en&query=id={final[i]}&field=wfstate&field=record_type&field=contract_type&field=contract_start_date&field=contract_end_date&field=contract_term_in_months&field=addendum_effective_date&field=new_sub_category"

    responce1 = requests.request("Get",url1)
    data1 = responce1.text
    whole_data.update({final[i]:data1.replace("\r", "").replace("\n", "").split(';')})
    count += 1
# print(whole_data)
pattern = re.compile(r"(?:ST_|EWREST_)?(\w+?)(?:_0)?\s*=\s*'([^']*)'")
dictonary = parser(whole_data)
print("JSON Parsed.")
print(dictonary)

#saved search - name given to preset filters to display subset of universe
#example = we have 2 types of contracts. BSA and BIP
#If the saved search is created with name 'active BSA' then it will only return 
# contract document type - BSA
# status = Active
