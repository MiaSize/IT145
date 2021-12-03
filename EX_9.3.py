
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

francisco = Users("francisco","magana",22,"grand rapids","Admin")
izzy = Users("izzy","artz",19,"east lansing",'Moderator')
katie = Users("katie","philipps",18,'east lansing','Guest')

francisco.describe_user()
francisco.greet_user()
izzy.describe_user()
izzy.greet_user()
katie.describe_user()
katie.greet_user()
