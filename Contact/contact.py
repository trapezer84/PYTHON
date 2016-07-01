import contact_service


class Contact(object):
    def __init__(self, name, email, phone_number, address):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
