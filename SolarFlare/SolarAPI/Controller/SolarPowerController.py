from msilib.schema import ServiceControl
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from SolarAPI.Abstract.ASolarPowerService import *
from SolarAPI.Services.JSONService import *

class SolarPowerController():
    
    states = { 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
            'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
            'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
            'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
            'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'}
   
    def __init__(self, SolarService: ASolarPowerService):
        self.__SolarService = SolarService


    #made 1 get method so that I could use the same URL but with different query string parameters
    def getSolarPowerInfo(self, request):

        #Maps query string parameters as key and value in the dictionary
        query = request.GET.dict()

        # checking if only 1 querystring parameter and if it is id
        if "id" in query and len(query.keys()) == 1:

            if query["id"].isdigit():
                
                try:

                    SolarPanels = self.__SolarService.getSolarPanelByID(int(query["id"]))
                    
                    return HttpResponse(SolarPowerToJson(SolarPanels))
            
                except KeyError:
                    return HttpResponseBadRequest("Invalid ID Provided")

            else:
                return HttpResponseBadRequest("Invalid ID Provided")

        # checking if only 1 querystring parameter and if it is state
        elif "state" in query and len(query.keys()) == 1:

            if query["state"].isalpha() and query["state"].upper() in self.states:
                
                try:

                    SolarMap = self.__SolarService.getSolarPanelByState(query["state"].upper())
                    
                    return HttpResponse(SolarPowerToJson(SolarMap))

                except KeyError:
                    return HttpResponseBadRequest("Invalid State Provided")

            else:

                return HttpResponseBadRequest("Invalid State provided")

        # checking if only 2 querystring parameter and if it is minCap and MaxCap
        elif len(query.keys()) == 2 and "minCap" in query and "maxCap" in query:

            if query["minCap"].isdigit() and query["maxCap"].isdigit():

                try:

                    SolarMap = self.__SolarService.getSolarPanelByRange(query["minCap"], query["maxCap"])
                    
                    return HttpResponse(SolarPowerToJson(SolarMap))

                except ValueError:
                    return HttpResponseBadRequest("Invalid minimum and maximum capacities provided")
            else:

                return HttpResponseBadRequest("Invalid minimum and maximum capacities provided")
        else:

            return HttpResponseBadRequest("Invalid Parameters Provided")

    # I used a different url for this GET so I used a different method
    def getSolarPowerMaxMonth(self, request):

        query = request.GET.dict()
        
        if "id" in query and len(query.keys()) == 1:

            if query["id"].isdigit():
                
                try:

                    SolarPanelMaxGenMonByID = self.__SolarService.getSolarPanelMaxMonth(int(query["id"]))
                    return HttpResponse(SolarPowerToJson(SolarPanelMaxGenMonByID))
                    

                except KeyError:
                    return HttpResponseBadRequest("ID not found")
                except FileNotFoundError:
                    return HttpResponseBadRequest("Generation Data File Not Found")

            else:
                return HttpResponseBadRequest("Invalid ID Provided")

        else:

            return HttpResponseBadRequest("Invalid Parameters Provided")

    