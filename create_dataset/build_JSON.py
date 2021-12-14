import datetime
import json
import random
from random import randrange

import pandas as pd

i = 1
lstConds = []
lstCondTypes = ["infectious disease", "deficiency disease", "hereditary disease", "physiological disease"] 
j = 1
lstTherapies = []
lstTherapyTypes = ["cognitive-behavioral therapy", "dialectical behavior therapy", "exposure therapy", "interpersonal therapy", "psychodynamic therapy"]
k = 1
lstPatients = []
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/UNITN/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conditionsshort.txt") as file:
        for line in file:
            lstConds.append(
                {'id': i,  'name': line.rstrip(), 'type': random.choice(lstCondTypes)})
            i += 1
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/UNITN/Data_Mining/final_project/patient-therapy-recommending/create_dataset/therapiesshort.txt") as file:
        for line in file:
            lstTherapies.append(
                {'id': 'th'+str(j),  'name': line.rstrip(), 'type': random.choice(lstTherapyTypes)})
            j += 1
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/UNITN/Data_Mining/final_project/patient-therapy-recommending/create_dataset/nameshort.txt") as file:
        for line in file:
            i = 1
            conditionCount = randrange(1, 20)
            lstTrials = []
            lstPreConds = []
            finishedConds = []
            for x in range(conditionCount):
                startDate = datetime.datetime(2015, 1, 1)
                nextTrial = randrange(5000)
                endDate = startDate + datetime.timedelta(days=nextTrial)
                timeStampStart = str(startDate.year) + \
                    str(startDate)[5:7] + str(startDate)[8:10]
                timeStampEnd = str(endDate.year) + \
                    str(endDate)[5:7] + str(endDate)[8:10]
                therapyIndex = randrange(len(lstTherapies))
                success = randrange(70, 101)
                conditionID = 'pc' + str(randrange(4))
                if conditionID not in finishedConds:
                    trialDict = {'id': 'tr'+str(i), 'start':  timeStampStart, 'end': timeStampEnd,
                                 'condition': conditionID, 'therapy': lstTherapies[therapyIndex]['id'], 'successful': success}
                    lstTrials.append(trialDict)
                    if success == 100:
                        finishedConds.append(conditionID)
                i += 1
            # preconditions
            dfx = pd.DataFrame(lstTrials)
            try:
                groupedConds = dfx.groupby("condition", as_index=False).agg(
                    start=("start", "min"),
                    end=("end", "max"),
                    success=("successful", "max"))
                indexMax = len(groupedConds.index)
                for ind in range(0, indexMax):
                    conditionIndex = randrange(len(lstConds))
                    if groupedConds.iloc[ind]['success'] == 100:
                        lstPreConds.append({'id': groupedConds.iloc[ind]['condition'], 'diagnosed': groupedConds.iloc[ind]
                                            ['start'], 'cured': groupedConds.iloc[ind]['end'], 'kind': lstConds[conditionIndex]['id']})
                    else:
                        lstPreConds.append(
                            {'id': groupedConds.iloc[ind]['condition'], 'diagnosed': groupedConds.iloc[ind]['start'], 'cured': "", 'kind': lstConds[conditionIndex]['id']})
            except:
                print("no conditions for patient")
            lstPatients.append(
                {'id': k, 'name': line.rstrip(), 'conditions': lstPreConds, 'trials': lstTrials})
            k += 1
            print(line)
with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/UNITN/Data_Mining/final_project/patient-therapy-recommending/create_dataset/dataset_short.JSON", "w") as jsonFile:
    myJSON = {'Conditions': lstConds, 'Therapies': lstTherapies, 'Patients': lstPatients}
    finalJSON = json.dumps(myJSON,  indent=4)
    print(len(finalJSON))
    jsonFile.write(finalJSON)
