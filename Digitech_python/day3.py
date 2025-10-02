my_dict = {"name": "Raphael", "age": 22, "tribe": "Luo"}
print (my_dict)


# # clear
# my_dict.clear()
# print(my_dict) 

# backup
backup = my_dict.copy()
print(backup)

# fromkeys
keys = ["name", "age", "city"]
values = "unknown"
default = dict.fromkeys(keys, values)
print(default)


getting = backup.get("age")
print(getting)


key1 = backup.keys()
print(key1)

value1 = my_dict.values()
print(value1)

all_item = backup.items()
print(all_item)


popping = backup.pop("name")
print(popping)
print(backup)



popitem = my_dict.popitem()
print(popitem)
print(my_dict)


new_dict = {"name": "lenox", "country": "kenya"}
setdefaulting = new_dict.setdefault("ethnicity", "Giriama")
print(setdefaulting)


new_dict = {"name": "lenox", "country": "kenya"}
setdefaulting = new_dict.setdefault("name", "Giriama")
print(setdefaulting)

# updating
updating = my_dict.update(new_dict)
print(my_dict)

# merging two separate lists into one list 
new_keys = ["school", "gender", "class"]
new_values = ["Barani", "Female", 8]
complete_dict = dict(zip(new_keys,new_values))
print(complete_dict)  