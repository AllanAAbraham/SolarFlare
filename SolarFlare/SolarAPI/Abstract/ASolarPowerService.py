from abc import abstractmethod


@abstractmethod
def getSolarPanelByID(id):
    pass

@abstractmethod
def getSolarPanelByState(state):
    pass

@abstractmethod
def getSolarPanelByRange(minCap, maxCap):
    pass

@abstractmethod
def getSolarPanelMaxMonth(id):
    pass