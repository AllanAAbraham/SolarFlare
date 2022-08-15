import json
import csv
from optparse import Values
from SolarAPI.Models.SolarPower import SolarPower
from SolarAPI.Abstract.ASolarPowerService import *

csvPath = 'generation_data/'
csvFile = '_data.csv'
f = open('projects.json',)
data = json.load(f)
f.close()

SolarMap = {}

for x in data:
    temp = SolarPower(x["name"], float(x["capacity_kw"]), x["address"], x["city"], x["state"], x["zip"])
    SolarMap[int(x["id"])] = temp

def getSolarPanelByID(id:int):
    if id in SolarMap:
        return SolarMap[id]
    else:
        raise KeyError


def getSolarPanelByState(state:str) -> dict:
    SolarByStateMap = {}
    for key in SolarMap:
        
        if SolarMap[key].State == state:
            
            SolarByStateMap[key] = SolarMap[key]

    if len(SolarByStateMap.keys()) > 0:
        return SolarByStateMap

    else:
       raise KeyError
    


def getSolarPanelByRange(minCap:float, maxCap:float) -> dict:
    
    SolarByCapacityMap = {}

    for key in SolarMap:
        
        if float(minCap) <= float(SolarMap[key].Capacity) and float(SolarMap[key].Capacity) <= float(maxCap):
            
            SolarByCapacityMap[key] = SolarMap[key]

    if len(SolarByCapacityMap.keys()) > 0:
        return SolarByCapacityMap

    else:
       raise ValueError


def getSolarPanelMaxMonth(id:int) -> dict:
    

    if id in SolarMap:

        PowerByMonth = {}

        csvFilePath = csvPath+str(id)+csvFile
        #2018-01 2018-02 2018-03 2018-04 2018-05 2018-06
        try:
            with open(csvFilePath, "r") as csvfile:
                readCSV = csv.DictReader(csvfile)
                #counter = ""
                for row in readCSV:
                    splitDate =  str(row["ts"]).split("-")
                    dateKey = splitDate[0]+'-'+splitDate[1]
                    if dateKey in PowerByMonth:
                        #PowerByMonth[dateKey] = "updatedstuff"
                        if "total" in row:
                            PowerByMonth[dateKey] = PowerByMonth[dateKey] + float(row["total"])
                        elif "Generation Meter RM - 01" in row:
                            PowerByMonth[dateKey] = PowerByMonth[dateKey] + float(row["Generation Meter RM - 01"])
                    else:
                        PowerByMonth[dateKey] = float(row["total"])
                   #counter = row["ts"] +" " +row ["total"] + "\n" + counter
            
            maxMonth = [key for key, value in PowerByMonth.items() if value == max(PowerByMonth.values())]
            #return PowerByMonth
            return maxMonth

        except FileNotFoundError:
            raise FileNotFoundError

    else:
        raise KeyError