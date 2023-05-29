# Create a set variable.
fruits = {"apple", "banana", "cherry"}

# Use the add() method to add elements to the set.
fruits.add("orange")

# Use the remove() method to remove elements from the set.
fruits.remove("banana")

# Use the update() method to add elements from another set to the current set.
other_fruits = {"grapes", "kiwi"}
fruits.update(other_fruits)

print(fruits)  # Prints {'apple', 'orange', 'cherry', 'grapes', 'kiwi'}