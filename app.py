filename = input("Enter filename: ")

search_string = input("Enter string to search for: ")
output = []

with open(filename, "r") as file:
    for line in file:
        if search_string in line:
            output.append(line)
            # print(line)

with open(f"{search_string}.txt", "w") as file:
    for line in output:
        file.write(line)
