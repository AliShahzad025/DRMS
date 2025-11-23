# models/volunteer.py

class Volunteer:
    def __init__(self, volunteerID=None, roles=None, verified=False, status='available', last_active=None):
        """
        Matches the schema in your SQL file:
        Volunteer (
            volunteerID INT PRIMARY KEY,       -- references UserAccount(userID)
            roles VARCHAR(200),
            verified BOOLEAN DEFAULT FALSE,
            status ENUM('available','busy','inactive') DEFAULT 'available',
            last_active DATETIME,
            FOREIGN KEY (volunteerID) REFERENCES UserAccount(userID) ON DELETE CASCADE
        );
        """
        self.volunteerID = volunteerID
        self.roles = roles
        self.verified = bool(verified)
        self.status = status
        self.last_active = last_active

    def __repr__(self):
        return f"<Volunteer {self.volunteerID}: {self.roles}>"
# models/volunteer.py

class Volunteer:
    def __init__(self, volunteerID=None, roles=None, verified=False, status='available', last_active=None):
        """
        Matches the schema in your SQL file:
        Volunteer (
            volunteerID INT PRIMARY KEY,       -- references UserAccount(userID)
            roles VARCHAR(200),
            verified BOOLEAN DEFAULT FALSE,
            status ENUM('available','busy','inactive') DEFAULT 'available',
            last_active DATETIME,
            FOREIGN KEY (volunteerID) REFERENCES UserAccount(userID) ON DELETE CASCADE
        );
        """
        self.volunteerID = volunteerID
        self.roles = roles
        self.verified = bool(verified)
        self.status = status
        self.last_active = last_active

    def __repr__(self):
        return f"<Volunteer {self.volunteerID}: {self.roles}>"
