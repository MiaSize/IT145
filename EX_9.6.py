
class Restaurant():
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is named", self.restaurant_name.title(), "and the cuisine type is", self.cuisine_type)
    
    def open_restaurant(self):
        print("The", self.restaurant_name.title(), "is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['mint chocolate chip', 'bubblegum', 'vanilla']

    def display_list(self):
        print(self.flavors)

flavors = IceCreamStand("ColdStone","Ice Cream")
flavors.display_list()
