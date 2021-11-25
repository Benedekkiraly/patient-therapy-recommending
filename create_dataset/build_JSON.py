import json
from random import randrange
import datetime

i = 1
lstConds = []
j = 1
lstTherapies = []
k = 1
lstPatients = []
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/dataset.JSON", "w") as jsonFile:

    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conditions.txt") as file:
        for line in file:
            lstConds.append(
                {'id': i, 'type': "Condition", 'name': line.rstrip()})
            i += 1
    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/therapies.txt") as file:
        for line in file:
            lstTherapies.append(
                {'id': j, 'type': "Therapy", 'name': line.rstrip()})
            j += 1

    myJSON = {'Conditions': lstConds, 'Therapies': lstTherapies}

    json.dump(myJSON, jsonFile, indent=4)
    
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/dataset.JSON", "w") as jsonFile:

    with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/names.txt") as file:
        for line in file:
            i = 1
            conditionCount = randrange(10)
            lstTrials = []
            for x in range(conditionCount):
                startDate = datetime.datetime(2015, 1, 1)
                nextTrial = randrange(5000)
                endDate = startDate + datetime.timedelta(days=nextTrial)
                timeStampStart = str(startDate.year) + \
                    str(startDate)[5:7] + str(startDate)[8:10]
                timeStampEnd = str(endDate.year) + \
                    str(endDate)[5:7] + str(endDate)[8:10]
                conditionIndex = randrange(len(lstConds))
                therapyIndex = randrange(len(lstTherapies))
                success = randrange(99)
                lstTrials.append({'id': i, 'start':  timeStampStart, 'end': timeStampEnd,
                                 'condition': lstConds[conditionIndex]['name'], 'therapy': lstTherapies[therapyIndex]['name'], 'successful': success})
                i += 1
            lstPatients.append(
                {'id': k, 'name': line.rstrip(), 'trials': lstTrials})
            k += 1

    myJSON = {'Conditions': lstConds, 'Therapies': lstTherapies, 'Patients': lstPatients}
    json.dump(myJSON, jsonFile, indent=4)
