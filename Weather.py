class Weather:
    def __init__(self, timestamp, speed, direction):
        self.windTimestamp = timestamp
        self.windSpeed = speed
        self.windDirection = direction


    def getWindTimeStamp(self):
        return self.windTimestamp
    def getWindSpeed(self):
        return self.windSpeed
    def getWindDirection(self):
        return self.windDirection

