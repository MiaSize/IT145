
class Users():
    def __init__(self,first_name,last_name,age,location,access_rights):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.access_rights = access_rights

    def describe_user(self):
        print("The user's first name is",self.first_name.title(),"and last name is",self.last_name.title(),
        "their age is", str(self.age),
        "their location is", self.location.title(),
        "and their access rights are", self.access_rights
        )

    def greet_user(self):
        print("Have a good day",self.first_name.title(),self.last_name.title())

class Privileges():
    def __init__(self,privileges = ['can delete posts','can ban users','can import files','can change nickname','can export files']):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(Users):
    def __init__(self, first_name, last_name, age, location, access_rights):
        super().__init__(first_name, last_name, age, location, access_rights)
        self.privileges = Privileges()


show = Admin('mia','cusenza',18,'Ypsilanti','Admin')
show.privileges.show_privileges()

