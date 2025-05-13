##Lab 8: Handling None in Loops

#Checking for None in a List:
data = [1,2,None,4,5,6,None,9,10]

for item in data:
    if item is None:
        continue
    print(item)

##andling None in a Dictionary:

user_data = {"name": "Alice", "age": None, "email": "alice@example.com"}

for key, value in user_data.items():
    if value is None:
        print(f"{key} is missing.")
    else:
        print(f"{key}: {value}")