from msilib.schema import ServiceControl
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from SolarAPI.Services.SolarPowerService import *


def getSolarPowerByID(request):
    
    query = request.GET.dict()
    
    if "id" in query:

        if query["id"].isdigit():
            
            try:

                SolarPanels = getSolarPanelByID(int(query["id"]))
                
                #convert solarpanel to json later

                return HttpResponse("<h1> {}</h1>".format(SolarPanels.asdict()))

            except KeyError:
                return HttpResponseBadRequest("ID provided is not valid")

        else:
            return HttpResponseBadRequest("ID provided is not valid")
    
    else:
        return HttpResponseBadRequest("No id provided")


