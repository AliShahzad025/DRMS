# models/sos_request.py
class SOSRequest:
    def __init__(self, requestID=None, victimID=None, location=None, latitude=None, longitude=None,
                 typeOfNeed=None, description=None, urgencyLevel=None, status=None,
                 priorityScore=None, createdAt=None, updatedAt=None, assignedVolunteerID=None, assignedNGO=None):
        self.requestID = requestID
        self.victimID = victimID
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.typeOfNeed = typeOfNeed
        self.description = description
        self.urgencyLevel = urgencyLevel
        self.status = status
        self.priorityScore = priorityScore
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.assignedVolunteerID = assignedVolunteerID
        self.assignedNGO = assignedNGO
