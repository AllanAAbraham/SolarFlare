from abc import ABC, abstractmethod
from SolarAPI.Models.SolarPower import SolarPower

class ASolarPowerService(ABC):

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
    def getSolarPanelMaxMonth(id:int) -> str:
        pass