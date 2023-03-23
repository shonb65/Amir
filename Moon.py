

class MoonFactory:
    def create_moon(self, moon_type):
        if moon_type == "full":
            return FullMoon()
        elif moon_type == "partial":
            return PartialMoon()
        elif moon_type == "red":
            return RedMoon()
        else:
            raise ValueError("Invalid moon type")


class Moon():
    pass

class FullMoon(Moon):
    pass

class PartialMoon(Moon):
    pass

class RedMoon(Moon):
    pass

