from abc import ABC
from Attack import *

class MoonFactory:
    def createMoon(self, moonType):
        if moon_type == "full":
            return FullMoon()
        elif moon_type == "partial":
            return PartialMoon()
        elif moon_type == "red":
            return RedMoon()
        else:
            raise ValueError("Invalid moon type")
    
    
class Moon(ABC):
    def __init__(self):
        self._capableAttacks = []
        
    def appendCapableAttacks(self, *args):
        self._capableAttacks + list(args)

    
class FullMoon(Moon):
    def __init__(self):
        super().__init__()
        self.appendCapableAttacks()

class PartialMoon(Moon):
    def __init__(self):
        super().__init__()
        self.appendCapableAttacks()

class RedMoon(Moon):
    def __init__(self):
        super().__init__()
        self.appendCapableAttacks()
