class Item:
    def __init__(self, name, prices, time = None):
        self._name = name
        self._prices = prices
        self._time = time
    
    def __str__(self):
        return f"{self._name}: {self._prices}"
    
    def __repr__(self):
        return f"Item(name='{self._name}', prices={self._prices}, time={self._time})"
    
    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._prices
    
    def getTime(self):
        return self._time