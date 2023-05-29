# Create a string variable.
str1 = "Hello, world!"

# Use square brackets to access the string items.
print(str1[0]) # Prints "H"
print(str1[1]) # Prints "e"

# Use the len() function to get the length of the string.
print(len(str1)) # Prints 13

# Use the in operator to check if a character is present
print("l" in str1) # Prints True

# Use the replace() method to replace a character in the
str2 = str1.replace("world", "universe")
print(str2) # Prints "Hello, universe!"

# Use the split() method to split the string into a list.
str3 = str1.split()
print(str3) # Prints ["Hello", "world!"]