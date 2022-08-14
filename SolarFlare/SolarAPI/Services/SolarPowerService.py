import json
from SolarAPI.Models.SolarPower import SolarPower
from SolarAPI.Abstract.ASolarPowerService import *

f = open('projects.json',)
data = json.load(f)
f.close()

SolarMap = {}

for x in data:
    temp = SolarPower(x["name"], float(x["capacity_kw"]), x["address"], x["city"], x["state"], x["zip"])
    SolarMap[int(x["id"])] = temp

def getSolarPanelByID(id):
    if id in SolarMap:
        return SolarMap[id]
    else:
        raise KeyError


def getSolarPanelByState(state):
    pass


def getSolarPanelByRange(minCap, maxCap):
    pass


def getSolarPanelMaxMonth(id):
    pass