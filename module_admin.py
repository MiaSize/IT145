from module_user import Users

class Privileges():
    def __init__(self,privileges = ['can delete posts','can ban users','can import files','can change nickname','can export files']):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(Users):
    def __init__(self, first_name, last_name, age, location, access_rights):
        super().__init__(first_name, last_name, age, location, access_rights)
        self.privileges = Privileges()
        