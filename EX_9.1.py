
class Restaurant():
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is named", self.restaurant_name.title(), "and the cuisine type is", self.cuisine_type)
    
    def open_restaurant(self):
        print("The", self.restaurant_name.title(), "is open")


restaurant = Restaurant("Peppinos","pizza")
print("\n",restaurant.restaurant_name,restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()