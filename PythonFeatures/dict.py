my_dict = {"Name": 1, "Age": 2, "City": 3}

for key, value in my_dict.items():
    print(key, value)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

my_dict.clear()

my_dict["Love"] = 4

print(my_dict)

my_dict.pop("Love")

print(my_dict)
