class SolarPower:
    
    def __init__(self, name: str, capacity: float, address: str, city: str, state: str, zip: str) -> None:
        self.__name = name
        self.__capacity = capacity
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip

    @property
    def Name(self) -> str:
        return self.__name
    
    @property
    def Capacity(self) -> float:
        return self.__capacity

    @property
    def Address(self) -> str:
        return self.__address

    @property
    def City(self) -> str:
        return self.__city

    @property
    def State(self) -> str:
        return self.__state

    @property
    def Zip(self) -> str:
        return self.__zip
