import json

i=1
lstConds =  []
j=1
lstTherapies =  []
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/dataset.JSON", "w") as jsonFile:
    
    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conditions.txt") as file:
        for line in file:
            lstConds.append({'id': i, 'type': "Condition", 'name': line.rstrip()})          
            i+=1
    #json.dump(lstConds, jsonFile, indent = 4)
    
    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/therapies.txt") as file:
        for line in file:
            lstTherapies.append({'id': j, 'type': "Therapy", 'name': line.rstrip()})          
            j+=1
    #json.dump(lstTherapies, jsonFile, indent = 4)

    myJSON ={ 'Conditions': lstConds, 'Therapies' : lstTherapies}
    json.dump(myJSON, jsonFile, indent = 4)