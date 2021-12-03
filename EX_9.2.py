
class Restaurant():
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is named", self.restaurant_name.title(), "and the cuisine type is", self.cuisine_type)
    
    def open_restaurant(self):
        print("The", self.restaurant_name.title(), "is open")


restaurant = Restaurant("Peppinos","pizza")
restaurant2 = Restaurant("Olive Garden","Everything")
restaurant3 = Restaurant("Five Guys","Burgers")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
