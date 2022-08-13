# prompt user for filename
filename = input("Enter filename: ")

# prompt user for search_string
search_string = input("Enter string to search for: ")
# convert to open with syntax

file = open("sample.txt", "r")
for line in file:
    if "searchstring" in line:
        print(line)
