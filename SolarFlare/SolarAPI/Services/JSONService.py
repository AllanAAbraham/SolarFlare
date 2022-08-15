from SolarAPI.Models.SolarPower import SolarPower
from SolarAPI.Models.SolarPower import SolarPower
from multipledispatch import dispatch
import json

#used dispatch for method overloading
@dispatch(SolarPower)
def SolarPowerToJson(SolarObj: SolarPower) -> json:
    return json.dumps(SolarObj.asdict())

@dispatch(dict)
def SolarPowerToJson(SolarMap: dict) -> json:
    for key in SolarMap:
        #if the value is the solarpower object, need to convert object to something that can be converted to json which is a dict
        if isinstance(SolarMap[key], SolarPower):
            SolarMap[key] = SolarMap[key].asdict()
    return json.dumps(SolarMap)

@dispatch(list)
def SolarPowerToJson(SolarList: list) -> json:
    return json.dumps(SolarList)