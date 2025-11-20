class Admin:
    def __init__(self, adminID=None, office=None):
        self.adminID = adminID
        self.office = office

    def __repr__(self):
        return f"<Admin {self.adminID}: {self.office}>"
