filename = input("Enter filename: ")

search_string = input("Enter string to search for: ")

with open(filename, "r") as file:
    for line in file:
        if search_string in line:
            print(line)
