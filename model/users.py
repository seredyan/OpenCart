
from sys import maxsize


class User:

    def __init__(self, id=None, firstname=None, lastname=None, phone=None, username=None, password=None):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.username = username
        self.password = password



    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.username, self.phone)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.username == other.username and \
               self.phone == other.phone and self.firstname == other.firstname and self.lastname == other.lastname and self.phone == other.phone




    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
