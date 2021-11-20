import json

i=1
lst =  []
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conds.JSON", "w") as jsonFile:
    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conditions.txt") as file:
        for line in file:
            lst.append({'id': i, 'type': "Condition", 'name': line.rstrip()})          
            i+=1
    json.dump(lst, jsonFile, indent = 4)