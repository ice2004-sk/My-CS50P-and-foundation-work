name = input("")

for i in range(len(name)):
    
    if 90 >= ord(name[i]) >= 65 and i > 0:
        print("_" + name[i].lower(), end="")

    elif 90 >= ord(name[i]) >= 65 and i == 0:
       print(name[i].lower(), end = "")

    else:
        print(name[i], end="")

print("")