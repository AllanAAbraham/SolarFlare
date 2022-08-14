class SolarPower:
    
    def __init__(self, name: str, capacity: float, address: str, city: str, state: str, zip: str) -> None:
        self.__name = name
        self.__capacity = capacity
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip

    @property
    def Name(self):
        return self.__name
    
    @property
    def Capacity(self):
        return self.__capacity

    @property
    def Address(self):
        return self.__address

    @property
    def City(self):
        return self.__city

    @property
    def State(self):
        return self.__state

    @property
    def Zip(self):
        return self.__zip

    def asdict(self):
        return {"name": self.__name, "capacity": self.__capacity, "address": self.__address, "city": self.__city, "state": self.__state, "zip": self.__zip}