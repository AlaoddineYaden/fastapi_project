import datetime


class User:
    def __init__(self, name, email, hashed_password):
        self.id: int = 1
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.created_date = None
        self.last_login: datetime.datetime = None
        self.profile_image_url = ""
