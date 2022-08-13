# prompt user for filename
filename = input("Enter filename: ")

# prompt user for search_string
search_string = input("Enter string to search for: ")
# convert to open with syntax
with open(filename, "r") as file:
    for line in file:
        if search_string in line:
            print(line)
