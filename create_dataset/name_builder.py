from random import randrange
import linecache
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/names.txt", "w") as namesTXT:
    for i in range(9999):
        indexFirst =randrange(164459)
        indexLast = randrange(98413)
        firstName = linecache.getline("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/first_names.txt", indexFirst).strip()
        lastName = linecache.getline("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/last_names.txt", indexLast).strip()
        fullName= firstName +" "+ lastName
        print(fullName)        
        namesTXT.write(fullName + "\n")
