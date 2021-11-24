import json
from random import randrange
import datetime

with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/trials_JSON.JSON", "w") as jsonFile:
    i=1
    conditionCount = randrange(35)
    lstTrials = []
    for x in range(conditionCount):
        trialDate = datetime.datetime(2015, 1, 1)
        nextTrial = randrange(50)
        trialDate += datetime.timedelta(days=nextTrial)
        timeStamp= str(trialDate.year()) + str(trialDate.month() + str(trialDate.day()))
        print(timeStamp)    
        lstTrials.append({'id': i, 'timestamp': "", 'condition': "xds", 'therapy':"xx", 'outcome' : "xx"}) 
    json.dump(lstTrials, jsonFile, indent = 4)  

