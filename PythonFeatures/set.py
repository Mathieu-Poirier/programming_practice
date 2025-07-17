my_set = set('MyString')

print(my_set)

my_set.add('A')

print(my_set)

my_set.remove('A')

print(my_set)

for key in my_set:
    print(key)

print("amp" in "Example")

def mfunc(set1) -> None:
    print(set1)
    print("Set1 was aliased to", id(set1)) 
    # id gives the memory address of the object in CPython

mfunc(my_set)