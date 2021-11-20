from bs4 import BeautifulSoup
import requests

with open("/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/condos.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    
print(soup.find_all(class_="module__title"))
conditionResults = soup.find_all(class_="module__title")

with open('/Users/bendo/Bendo_OneDrive/OneDrive - Kormányzati Informatikai Fejlesztési Ügynökség/Egyetem/Trento/Data_Mining/final_project/patient-therapy-recommending/create_dataset/conditions.txt', 'w') as f:
    for row in conditionResults:
            f.write("%s\n" % str(row))