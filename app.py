# prompt user for filename

# prompt user for search_string
# convert to open with syntax

file = open("sample.txt", "r")
for line in file:
    if "searchstring" in line:
        print(line)
