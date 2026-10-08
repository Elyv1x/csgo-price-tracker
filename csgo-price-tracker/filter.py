import ast
from item import Item
import os

def read_items_from_file(filename = "C:\\Users\\fh2po\\Desktop\\Pro-ject1\\result.txt"):
    items =[]
    with open(filename, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("#"):
            _time = line[4:].strip()
        elif ":" in line:
            name, price_str = line.split(":",1)
            prices = ast.literal_eval(price_str.strip())
            temp = Item(name = name.strip(), prices = prices, time = _time)
            items.append(temp)
    return items

def get_item_data(filename, target):#shortcut
    results = []
    current_time = None
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                current_time = line[4:].strip()
            elif target.lower() in line.lower():
                try:
                    name_part, price_part = line.split(":",1)
                    prices = ast.literal_eval(price_part.strip())
                    results.append({"time": current_time, "name": name_part, "price": prices})
                except Exception as e:
                    print("fail; ", line, e)
    return results

def filter_records(records, target_name = None, target_date = None):
    results=[]
    for rec in records:
        match_date = True
        match_name = True
        if target_name:
            match_name = target_name.lower() in rec.getName().lower()
        if target_date:
            match_date = rec.getTime() and target_date in rec.getTime()
        if match_date and match_name:
            results.append(rec)
    return results

os.system("cls")
filename = "C:\\Users\\fh2po\\Desktop\\Pro-ject1\\result.txt"
items = read_items_from_file(filename)
a = get_item_data(filename, 'co')
b = filter_records(items, "gambit", "3-28")
print(b)