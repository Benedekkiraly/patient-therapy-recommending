from random import randrange
import linecache
with open("create_dataset/names.txt", "w") as namesTXT:
    for i in range(9999):
        indexFirst =randrange(164459)
        indexLast = randrange(98413)
        firstName = linecache.getline("first_names.txt", indexFirst).strip()
        lastName = linecache.getline("last_names.txt", indexLast).strip()
        fullName= firstName +" "+ lastName
        print(fullName)        
        namesTXT.write(fullName + "\n")
