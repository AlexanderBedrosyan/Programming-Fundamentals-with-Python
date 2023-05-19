class Town:

    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude):
        self.latitude = latitude
        return self.latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        return self.longitude

    def __repr__(self):
       return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
