# Create a dictionary variable.
dict1 = {"name": "John Doe", "age": 30}

# Use square brackets to access the dictionary values using keys.
print(dict1["name"])  # Prints "John Doe"
print(dict1["age"])  # Prints 30

# Use the get() method to access the dictionary values using keys.
print(dict1.get("name"))  # Prints "John Doe"
print(dict1.get("age"))  # Prints 30

# Use the keys() method to get a list of all the keys in the dictionary.
print(dict1.keys())  # Prints ["name", "age"]

# Use the values() method to get a list of all the values in the dictionary.
print(dict1.values())  # Prints ["John Doe", 30]