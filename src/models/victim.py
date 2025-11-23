class Victim:
    def __init__(self, victimID=None, verified_contact=False, vulnerability_notes=None):
        self.victimID = victimID
        self.verified_contact = bool(verified_contact)
        self.vulnerability_notes = vulnerability_notes

    def __repr__(self):
        return f"<Victim {self.victimID}>"
