# models/ngo.py
class NGO:
    def __init__(self, ngoID=None, orgName=None, verified=False, registration_doc=None, region=None, contact_person=None):
        self.ngoID = ngoID
        self.orgName = orgName
        self.verified = bool(verified)
        self.registration_doc = registration_doc
        self.region = region
        self.contact_person = contact_person

    def __repr__(self):
        return f"<NGO {self.ngoID}: {self.orgName}>"
