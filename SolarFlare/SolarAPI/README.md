FILE STRUCTURE
- ASolarPowerService Abstract -> methods 
- SolarPowerService implements ISolarPowerService "backend" file -> hashmap, api calls these methods to access Map
- SolarPowerController "endpoint" file -> contains get endpoints
- SolarPower "object" class -> solar power object:
    -> properties:
        name (string)
        capacity kw (double)
        address (string)
        city (string)
        state (string)
        zip (string)
- JSONService class -> takes variety of inputs and returns json 


I used dependency injection in SolarPowerController.py, SolarPowerService.py, and in urls.py using ASolarPowerService. 
This keeps the code flexible as now the controller does not care what implementation the Service is in as long as 
the methods controller calls from service still exist. 
This, also, allows me to centralize, what implementation of the Service is, in the urls.py file.
Centralization of the Service classes in the url file allows a very clear understanding of which implementation of
Service that the controller is using instead of having to update the controller file. 
