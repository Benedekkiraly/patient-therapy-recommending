from random import randrange

with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/names.txt", "w") as namesTXT:
    for i in range(9999):
        firstNames=open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/first_names.txt")
        indexFirst =randrange(164459)
        for position, line in enumerate(firstNames):
            if position is indexFirst:
                print(line)
                firstName = line
        lastNames=open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/last_names.txt")
        indexLast =randrange(98413)
        for position, line in enumerate(lastNames):
            if position is indexLast:
                print(line)
                lastName = line
        namesTXT.write(firstName + lastName)
        namesTXT.write('\n')

