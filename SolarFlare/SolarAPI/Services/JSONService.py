from SolarAPI.Models.SolarPower import SolarPower
from multipledispatch import dispatch
import json

@dispatch(SolarPower)
def SolarPowerToJson(SolarObj: SolarPower):
    return json.dumps(SolarObj.asdict())

@dispatch(dict)
def SolarPowerToJson(SolarMap: dict):
    for key in SolarMap:
        SolarMap[key] = SolarMap[key].asdict()
    return json.dumps(SolarMap)