from msilib.schema import ServiceControl
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from SolarAPI.Services.SolarPowerService import *
from SolarAPI.Services.JSONService import *
import json

states = { 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'}

def getSolarPowerInfo(request):
    
    query = request.GET.dict()
    
    if "id" in query and len(query.keys()) == 1:

        if query["id"].isdigit():
            
            try:

                SolarPanels = getSolarPanelByID(int(query["id"]))
                SolarJson = SolarPowerToJson(SolarPanels)
                
                return HttpResponse(SolarJson)
                #return HttpResponse("<h1> {}</h1>".format(SolarPanels.asdict()))

            except KeyError:
                return HttpResponseBadRequest("Invalid ID Provided")

        else:
            return HttpResponseBadRequest("Invalid ID Provided")

    elif "state" in query and len(query.keys()) == 1:

        if query["state"].isalpha() and query["state"].upper() in states:
            
            try:

                SolarMap = getSolarPanelByState(query["state"].upper())
                SolarJson = SolarPowerToJson(SolarMap)
                return HttpResponse(SolarJson)

            except KeyError:
                return HttpResponseBadRequest("Invalid State Provided")

        else:

            return HttpResponseBadRequest("Invalid State provided")

    elif len(query.keys()) == 2 and "minCap" in query and "maxCap" in query:

        if query["minCap"].isdigit() and query["maxCap"].isdigit():

            try:

                SolarMap = getSolarPanelByRange(query["minCap"], query["maxCap"])
                SolarJson = SolarPowerToJson(SolarMap)
                return HttpResponse(SolarJson)

            except ValueError:
                return HttpResponseBadRequest("Invalid minimum and maximum capacities provided")
        else:

            return HttpResponseBadRequest("Invalid minimum and maximum capacities provided")
    else:

        return HttpResponseBadRequest("Invalid Parameters Provided")


def getSolarPowerMaxMonth(request):

    query = request.GET.dict()
    
    if "id" in query and len(query.keys()) == 1:

        if query["id"].isdigit():
            
            try:

                SolarPanelMaxGenMonByID = getSolarPanelMaxMonth(query["id"])
                if (type(SolarPanelMaxGenMonByID) is dict):
                    return HttpResponse(json.dumps(SolarPanelMaxGenMonByID))
                else:
                    return HttpResponse(SolarPanelMaxGenMonByID)
                

            except KeyError:
                return HttpResponseBadRequest("Invalid ID Provided")
            except FileNotFoundError:
                return HttpResponseBadRequest("Generation Data File Not Found")

        else:
            return HttpResponseBadRequest("Invalid ID Provided")

    else:

        return HttpResponseBadRequest("Invalid Parameters Provided")

    