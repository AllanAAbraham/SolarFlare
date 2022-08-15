from abc import abstractmethod
from SolarAPI.Models.SolarPower import SolarPower

@abstractmethod
def getSolarPanelByID(id:int) -> SolarPower:
    pass

@abstractmethod
def getSolarPanelByState(state:str) -> dict:
    pass

@abstractmethod
def getSolarPanelByRange(minCap:float, maxCap:float) -> dict:
    pass

@abstractmethod
def getSolarPanelMaxMonth(id:int) -> dict:
    pass