# models/resource.py

class ResourceType:
    def __init__(self, resourceTypeID=None, name=None, unit=None, description=None):
        self.resourceTypeID = resourceTypeID
        self.name = name
        self.unit = unit
        self.description = description


class ResourceStock:
    def __init__(self, resourceID=None, resourceTypeID=None, donorNGO=None,
                 quantity=None, status=None, lastVerifiedBy=None,
                 lastUpdated=None, location=None, latitude=None, longitude=None):
        self.resourceID = resourceID
        self.resourceTypeID = resourceTypeID
        self.donorNGO = donorNGO
        self.quantity = quantity
        self.status = status
        self.lastVerifiedBy = lastVerifiedBy
        self.lastUpdated = lastUpdated
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
