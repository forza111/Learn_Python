class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())
    def open_restaurant(self):
        print(self.name.title() + ' открыт')
my_Restaurant_1 = Restaurant('Элеон', 'японкая кухня')
my_Restaurant_2 = Restaurant('ИБИЦА', 'европейская кухня')
my_Restaurant_3 = Restaurant('Forza', 'европейская кухня')


my_Restaurant_1.describe_restaurant()
my_Restaurant_2.describe_restaurant()
my_Restaurant_3.describe_restaurant()