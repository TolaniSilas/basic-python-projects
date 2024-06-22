# Define the Users Class.
class Users:
    """A class to model a user profile.
    
    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        age (int): The age of the user, default is 26.
        gender (str): The gender of the user.
    """
    
    def __init__(self, first_name, last_name, gender):
        """Initialize the user profile's information.
        
        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            gender (str): The gender of the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = 26
        self.gender = gender 
        
    def describe_user(self):
        """Describe the user by printing their information."""
        print("The name of this user is " + self.first_name.title() + " " + self.last_name.title() +
              " (" + self.gender + ")" + ", he is " + str(self.age) + " years old.")
        
    def greet_user(self):
        """Send a greeting to the user."""
        print("Hi " + self.first_name.title() + " " + self.last_name.title() +
              ", it's great to have you here!")


# Define the Privileges Class.
class Privileges:
    """A class to represent privileges for an admin user.
    
    Attributes:
        privileges (list of str): A list of privileges assigned to an admin.
    """
    
    def __init__(self, privileges=["can add post", "can delete post", "can ban user", "can manage user's account"]):
        """Initialize the privileges.
        
        Args:
            privileges (list of str, optional): A list of privileges. Defaults to common admin privileges.
        """
        self.privileges = privileges
                  
    def show_privileges(self):
        """Display the privileges an admin is entitled to."""
        print("\nThe Admin is entitled to the following privileges: ")
        # Run a for loop to list the privileges.
        for privilege in self.privileges:
            print("\t- " + privilege)


# Define the Admin Class.
class Admin(Users):
    """A class to represent an administrator, inheriting from the Users class.
    
    Attributes:
        privileges (Privileges): An instance of the Privileges class.
    """
    
    def __init__(self, first_name, last_name, gender):
        """Initialize the attributes of the parent class and the privileges.
        
        Args:
            first_name (str): The first name of the admin.
            last_name (str): The last name of the admin.
            gender (str): The gender of the admin.
        """
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()

    def show_privileges(self):
        """Display the privileges an admin is entitled to."""
        print("The Admin " + "(" + self.first_name.title() + " " + self.last_name.title() + ")" + " is entitled to the following privileges: ")
        self.privileges.show_privileges()



# Create an instance of the Admin class.
administrator = Admin("osunba", "silas", "M")
administrator.describe_user()          
administrator.greet_user()
administrator.show_privileges()