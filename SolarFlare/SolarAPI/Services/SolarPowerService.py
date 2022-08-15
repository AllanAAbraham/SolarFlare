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
# I used a HashMap to simulate a database where ID would be the primary key
SolarMap = {}
# Reading through the data in the projects json, makes a Solar Power Object and then maps the ID to the object
for x in data:
    temp = SolarPower(x["name"], float(x["capacity_kw"]), x["address"], x["city"], x["state"], x["zip"])
    SolarMap[int(x["id"])] = temp

#Checks if id exists if true return the object else send an error
def getSolarPanelByID(id:int):
    if id in SolarMap:
        return SolarMap[id]
    else:
        raise KeyError

#Since the Map isn't using id as the key, have to iterate through the entire map to find Solar Panels that match the query and then add them to a Map that is returned
def getSolarPanelByState(state:str) -> dict:
    SolarByStateMap = {}
    for key in SolarMap:
        
        if SolarMap[key].State == state:
            
            SolarByStateMap[key] = SolarMap[key]
    #if no matches
    if len(SolarByStateMap.keys()) > 0:
        return SolarByStateMap

    else:
       raise KeyError
    

#Since the Map isn't using id as the key, have to iterate through the entire map to find Solar Panels that is within the minCapacity and maxCapacity
def getSolarPanelByRange(minCap:float, maxCap:float) -> dict:
    
    SolarByCapacityMap = {}

    for key in SolarMap:
        
        if float(minCap) <= float(SolarMap[key].Capacity) and float(SolarMap[key].Capacity) <= float(maxCap):
            
            SolarByCapacityMap[key] = SolarMap[key]

    if len(SolarByCapacityMap.keys()) > 0:
        return SolarByCapacityMap

    else:
       raise ValueError


def getSolarPanelMaxMonth(id:int) -> str:
        
    if id in SolarMap:
        #Mapping the year-month to a summation of generated total power in that timestamp
        PowerByMonth = {}
        #building the file path
        csvFilePath = csvPath+str(id)+csvFile
        #checking if the file is real
        try:
            with open(csvFilePath, "r") as csvfile:
                #Used dict reader so that the column titles would be mapped to the column content for reach row.
                readCSV = csv.DictReader(csvfile)
                
                for row in readCSV:
                    #Pulling the date out of the row
                    splitDate =  str(row["ts"]).split("-")
                    #I chose to kept the year as well so that in the future if the file had multiple years of data, the could would still be able to keep up without more updates
                    dateKey = splitDate[0]+'-'+splitDate[1]
                    
                    if dateKey in PowerByMonth:
                        #Summation of all data in the same year and month
                        if "total" in row:
                            PowerByMonth[dateKey] = PowerByMonth[dateKey] + float(row["total"])
                        #had to use this else if as the data file for 56 does not have a total column. In the future, if there are generation_data files that do not use either total or generation meter rm -01, 
                        # it would be fairly esay to add another elif for the corresponding power column here and in the else block.
                        elif "Generation Meter RM - 01" in row:
                            PowerByMonth[dateKey] = PowerByMonth[dateKey] + float(row["Generation Meter RM - 01"])
                    else:
                        if "total" in row:
                            PowerByMonth[dateKey] = float(row["total"])
                        elif "Generation Meter RM - 01" in row:
                            PowerByMonth[dateKey] =float(row["Generation Meter RM - 01"])
            #Now to iterate through PowerByMonth and pull in all keys that correspond to the max value
            maxMonth = [key for key, value in PowerByMonth.items() if value == max(PowerByMonth.values())]
            #if want to return entire Map to see the summations of power generation to each month, uncomment line below 
            #return PowerByMonth
            return maxMonth

        except FileNotFoundError:
            raise FileNotFoundError

    else:
        raise KeyError