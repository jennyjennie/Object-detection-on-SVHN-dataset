"""
Change category_id from 10 to 1 and generate the answer.json
"""

# Imports
import json
import os

ans_json_file = '../answer_corr_cat.json'

with open(ans_json_file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

for d in data:
    if d['category_id'] == 10:
        d['category_id'] = 0

json_file_path = '../answer_corr_cat.json'

os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
json_fp = open(json_file_path, "w")

json_str = json.dumps(data, indent=4)
json_fp.write(json_str)
json_fp.close()

print("Success")
