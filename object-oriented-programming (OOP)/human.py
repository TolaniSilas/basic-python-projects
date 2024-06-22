# Human Class 
class Human:
    """
    A simple class to represent a human being.

    Attributes:
        fname (str): The first name of the human.
        mname (str): The middle name of the human.
        lname (str): The last name of the human.
        age (int): The age of the human.
        gender (str): The gender of the human.
        complexion (str): The complexion of the human.
        walk (int): The walking speed of the human in km/hr.
        run (int): The running speed of the human in km/hr.
    """
    
    def __init__(self, firstname, middlename, lastname, age, gender, complexion):
        """
        Initialize the attributes that describe the human.

        Args:
            firstname (str): The first name of the human.
            middlename (str): The middle name of the human.
            lastname (str): The last name of the human.
            age (int): The age of the human.
            gender (str): The gender of the human.
            complexion (str): The complexion of the human.
        """
        self.fname = firstname.title()
        self.mname = middlename.title()
        self.lname = lastname.title()
        self.age = age
        self.gender = gender.title()
        self.complexion = complexion.title()
        self.walk = 0
        self.run = 0
     
    def about_the_person(self):
        """
        Print all the information of the person.

        Returns:
            str: A string containing all the information about the person.
        """
        full_name = self.lname + " " + self.fname + " " + self.mname
        info = "My name is " + full_name + ". I'm {} years old, I am a {}, and I am {} in complexion.".format(self.age, self.gender, self.complexion)
        return info
    
    def get_some_walk(self, walk):
        """
        This method allows the human to walk.

        Args:
            walk (int): The walking speed in km/hr.
        """
        if self.gender == "Male":
            # This block of code will run if the gender is male.
            if self.walk == 0:
                self.walk += walk
                print('The man walks at a rate of ' + str(self.walk) + " km/hr.")
            else:
                self.walk += walk
                print("The man continues walking at a rate of " + str(self.walk) + " km/hr.")
        elif self.gender == "Female":
            # This block of code will run if the gender is female.
            if self.walk == 0:
                self.walk += walk
                print('The woman walks at a rate of ' + str(self.walk) + " km/hr.")
            else:
                self.walk += walk
                print("The woman continues walking at a rate of " + str(self.walk) + " km/hr.")
        else:
            print('You have provided the wrong gender information!!')
            
    def get_some_run(self, run):
        """
        This method allows the human to run.

        Args:
            run (int): The running speed in km/hr.
        """
        if self.gender == "Male":
            # This block of code will run if the gender is male.
            if self.run == 0:
                self.run += run
                print('The man runs at a rate of ' + str(self.run) + " km/hr.")
            else:
                self.run += run
                print("The man continues running at a rate of " + str(self.run) + " km/hr.")
        elif self.gender == "Female":
            # This block of code will run if the gender is female.
            if self.run == 0:
                self.run += run
                print('The woman runs at a rate of ' + str(self.run) + " km/hr.")
            else:
                self.run += run
                print("The woman continues running at a rate of " + str(self.run) + " km/hr.")
        else:
            print('You have provided the wrong gender information!!')


# Create an instance.
human = Human('silas', 'motolani', 'osunba', 16, "male", "chocolate")
info = human.about_the_person()
print(info)

human.get_some_walk(1)
human.get_some_walk(2)        
human.get_some_run(39)
human.get_some_run(20)
