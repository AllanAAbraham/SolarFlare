from SolarAPI.Models.SolarPower import SolarPower
import jsonpickle

#used jsonpickle instead of json.dumps as json.dumps cannot handle objects

#encoding Input to Json
def SolarPowerToJson(SolarInput):
    return jsonpickle.encode(SolarInput)

#decoding json into solar power
def JsonToSolarPower(JsonInput):
    return jsonpickle.decode(JsonInput)

