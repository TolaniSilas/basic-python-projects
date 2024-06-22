# Define the CountingClicker class. 
class CountingClicker():
    """
    A class that represents a counting clicker used to track attendance at the 'Advanced Topics in Data Science' meetup.

    Attributes:
        count (int): Current count on the clicker, initialized to 0.

    Methods:
        __init__(self, count=0):
            Initializes the counting clicker with an optional initial count.

        click(self, num_times=1):
            Increases the count on the clicker by the specified number of times.

        read(self):
            Returns the current count on the clicker.

        reset(self):
            Resets the clicker count to zero.
    """
    
    def __init__(self, count=0):
        """Initialize the counting clicker with an optional initial count."""
        self.count = count
        
    def click(self, num_times=1):
        """
        Click the clicker a specified number of times.

        Args:
            num_times (int): Number of times to click the clicker. Default is 1.
        """
        self.count += num_times
        
    def read(self):
        """Return the current count on the clicker."""
        return self.count
    
    def reset(self):
        """Reset the clicker count to zero."""
        self.count = 0
        
        
        
# Assertions for CountingClicker.
clicker = CountingClicker()
assert clicker.read() == 0, "Clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "After two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "After reset, clicker should be back to 0"


# Create the NoResetClicker class. 
class NoResetClicker(CountingClicker):
    """
    A subclass that inherits all methods from CountingClicker except the 'reset' method.

    Methods:
        reset(self):
            Overrides the reset method to do nothing.
    """
    
    def reset(self):
        """Override the reset method to do nothing."""
        pass
        
   
# Assertions for NoResetClicker.
clicker2 = NoResetClicker()
assert clicker2.read() == 0, "NoResetClicker should start with count 0"
clicker2.click()
assert clicker2.read() == 1, "After one click, NoResetClicker should have count 1"
clicker2.reset()
assert clicker2.read() == 1, "Reset shouldn't do anything in NoResetClicker"

