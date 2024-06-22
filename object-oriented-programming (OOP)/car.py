# Define the Car Class.
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        
        Args:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
            year (int): The year the car was made.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name.
        
        Returns:
            str: A formatted string representing the car's name.
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        
        Args:
            mileage (int): The new mileage value.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        
        Args:
            miles (int): The number of miles to add.
        """
        self.odometer_reading += miles 



# Creating an instance of the Car class.
my_new_car = Car('Audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())

# Update the value of an attribute directly 
my_new_car.odometer_reading = 36
my_new_car.read_odometer()

# Updating an attribute's value through a method.
my_new_car.update_odometer(36)
my_new_car.read_odometer()

# Incrementing an attribute's value through a method.
my_new_car.increment_odometer(50)
my_new_car.read_odometer()


# Create the Battery class.
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """
        Initialize the battery's attribute.
        
        Args:
            battery_size (int): The size of the battery in kWh.
        """
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        """Upgrade the battery size to 85 kWh if it's less than 85."""
        if self.battery_size < 85:
            self.battery_size = 85


# Create a child class from the parent class(Car).
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        
        Args:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
            year (int): The year the car was made.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        self.battery.describe_battery()
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")



# Create an instance of the ElectricCar class.
my_tesla_car = ElectricCar("Tesla", "Model S", 2016)
print(my_tesla_car.get_descriptive_name())
my_tesla_car.battery.describe_battery()
my_tesla_car.battery.get_range()
my_tesla_car.battery.upgrade_battery()
my_tesla_car.battery.get_range()
