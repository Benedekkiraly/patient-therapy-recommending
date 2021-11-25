import json
from random import randrange
import datetime

with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/trials_JSON.JSON", "w") as jsonFile:
    i=1
    conditionCount = randrange(35)
    lstTrials = []
    for x in range(conditionCount):
        trialDate = datetime.datetime(2015, 1, 1)
        nextTrial = randrange(100)
        trialDate += datetime.timedelta(days=nextTrial)
        print(trialDate)
        timeStamp = str(trialDate.year) + str(trialDate)[5:7] + str(trialDate)[8:10]
        print(timeStamp)    
        lstTrials.append({'id': i, 'timestamp': "", 'condition': "xds", 'therapy':"xx", 'outcome' : "xx"}) 
    json.dump(lstTrials, jsonFile, indent = 4)  

