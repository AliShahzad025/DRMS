class PriorityZone:
    def __init__(self, zoneID=None, name=None, description=None, centerLat=None, centerLong=None, radius_km=None, priority_level='medium'):
        self.zoneID = zoneID
        self.name = name
        self.description = description
        self.centerLat = centerLat
        self.centerLong = centerLong
        self.radius_km = radius_km
        self.priority_level = priority_level

    def __repr__(self):
        return f"<PriorityZone {self.zoneID}: {self.name}>"
