import random
import time
def getrandomdate(StartDate,EndDate):
    print("printing random date between",StartDate,"and",EndDate)
    genetrator=random.random()
    format ="%m/%d/%Y"

    
    sttime =time.mktime(time.strptime(StartDate,format))
    edtime =time.mktime(time.strptime(EndDate,format))
    randomtime=sttime+genetrator *(edtime-sttime)
    randomdates=time.strftime(format,time.localtime(randomtime))
    return randomdates
print("Random date =",getrandomdate("1/1/2026","2/2/2030"))