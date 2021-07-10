string=input("Enter a string (length should be at least 3)\n")

print(string+"ing")

if string.endswith('ing'):
    print(string.replace("ing","ly"))