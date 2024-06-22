# Define the Restaurant class.
class Restaurant:
    """
    A simple attempt to model a restaurant.

    Attributes:
        restaurant_name (str): The name of the restaurant.
        cuisine_type (str): The type of cuisine served by the restaurant.
    """
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant with a name and type of cuisine.

        Args:
            restaurant_name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine served by the restaurant.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """
        Print the name and cuisine type of the restaurant.
        """
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The range of food that is served in " + self.restaurant_name.title() + " restaurant is the " +
              self.cuisine_type.title() + " cuisine.")
    
    def open_restaurant(self):
        """
        Print a message indicating that the restaurant is open.
        """
        print("The " + self.restaurant_name.title() + " " + self.cuisine_type.title() + " restaurant is open!")
        

# Create a child class (IceCreamStand) having the attributes and methods like that of the parent class (Restaurant).
class IceCreamStand(Restaurant):
    """
    Represent the aspect of a restaurant specific to an ice cream stand restaurant.

    Attributes:
        restaurant_name (str): The name of the restaurant.
        cuisine_type (str): The type of cuisine served by the restaurant.
        flavors (list): A list of ice cream flavors available in the ice cream stand.
    """
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the attributes of the parent class and the ice cream stand-specific attributes.

        Args:
            restaurant_name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine served by the restaurant.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "vanilla", "chocolate", "raspberry"]
        
    def lists_of_flavors(self):
        """
        Print the list of ice cream flavors available in the ice cream stand.
        """
        print("\nThe flavors available in the restaurant are: ")
        for flavor in self.flavors:
            print("\t-" + flavor.title())
         
            
            
# Create an instance of the IceCreamStand class. 
my_icecream = IceCreamStand("tolani", "frozen delights")
my_icecream.describe_restaurant()
my_icecream.open_restaurant()
my_icecream.lists_of_flavors()




