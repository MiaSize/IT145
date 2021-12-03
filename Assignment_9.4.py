
class Restaurant():
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant is named", self.restaurant_name.title(), "and the cuisine type is", self.cuisine_type)
    
    def open_restaurant(self):
        print("The", self.restaurant_name.title(), "is open")

    def set_number_served(self):
        print("The customers served is currently",self.number_served)

    def new_number_served(self,customers):
        self.number_served = customers


restaurant = Restaurant("Peppinos","pizza")

print("\n",restaurant.restaurant_name,restaurant.cuisine_type)

print(restaurant.set_number_served())
restaurant.number_served = 3
restaurant.set_number_served()

restaurant.new_number_served(6)
restaurant.set_number_served()

restaurant.describe_restaurant()
restaurant.open_restaurant()
