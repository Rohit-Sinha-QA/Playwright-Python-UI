a = "Hello World"

# Print Full String
print(a)

# Print any index of string
print(a[1])

# Print any value from end (negative index)
print(a[-1])

# Reverse a string
print(a[::-1])

# Print from x index to y index (x:y+1)
print(a[0:3])

# Print length of string
print(len(a))

# Print all words in lower case
print(a.lower())

# Print all words in upper case
print(a.upper())

# To remove spaces from beginning and end
print(a.strip())

# To remove spaces from beginning
print(a.lstrip())

# To remove spaces from end
print(a.rstrip())

# Count how many times a character occur
print(a.count("p"))

# Make first letter capital of a string
print(a.capitalize())

# To find Index of any character (output -1 means character is not present)
print(a.find("b"))

# To replace any character
print(a.replace("e", "T"))

# Function Concatenation
x = "apple"
y = "mango"
print(f"Hi can be replaced by {x} in nearby {y}")
