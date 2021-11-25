import json
from random import randrange
import datetime

f = open ('/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/dataset.JSON', "r")
dataset = json.loads(f.read())

with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/trials_JSON.JSON", "w") as jsonFile:
    i=1
    conditionCount = randrange(35)
    lstTrials = []
    for x in range(conditionCount):
        startDate = datetime.datetime(2015, 1, 1)
        nextTrial = randrange(5000)
        endDate = startDate + datetime.timedelta(days=nextTrial)
        timeStampStart = str(startDate.year) + str(startDate)[5:7] + str(startDate)[8:10]
        timeStampEnd = str(endDate.year) + str(endDate)[5:7] + str(endDate)[8:10]
        conditions= dataset['Conditions']
        therapies= dataset['Therapies']
        conditionIndex = randrange(len(conditions))
        therapyIndex = randrange(len(therapies))
        success = randrange(99)
        lstTrials.append({'id': i,'start':  timeStampStart, 'end':timeStampEnd,'condition': conditions[conditionIndex]['name'], 'therapy': therapies[therapyIndex]['name'], 'successful' : success})
        i+=1
    json.dump(lstTrials,jsonFile, indent = 4)  

