# employee.py is a Module declaring the Employee class to be used in project 2
# the Employee class has 4 attributes, name, IDnumber, department,and jobTitle
# each of the attributes are protected with the '__' prefix.  Only a method of the object
# may change the value of the given attribute.
# there are 8 methods assigned to the Employee class.
# Each of the attributes has a dedicated method to assign a value from a parameter
# and a dedicated method to return the value assigned to the attribute.
#####################################################################################

# Define the class
class Employee:
    # initialize variales with default values (empty strings)
    def __init__(self):
        self.__name = ""
        self.__IDnumber = ""
        self.__department = ""
        self.__jobTitle = ""
    # set_name(parameter) takes the value of a parameter and assigns it to '__name'
    def set_name(self,employee_name):
        self.__name = employee_name
    # get_name() returns the value assigned to '__name' to the statement that calls it
    def get_name(self):
        return self.__name
    # set_IDnumber(parameter) takes the value of a parameter and assigns it to '__IDnumber'
    def set_IDnumber(self, employee_IDnumber):
        self.__IDnumber = employee_IDnumber
    # get_IDnumber() returns the value assigned to '__IDnumber' to the statement that calls it
    def get_IDnumber(self):
        return self.__IDnumber
    # set_department(parameter) takes the value of a parameter and assigns it to '__department'
    def set_department(self, employee_department):
        self.__department = employee_department
    # get_department returns the value assigned to '__department' to the statement that calls it
    def get_department(self):
        return self.__department
    # set_jobTitle(parameter) takes the value of a parameter and assigns it to '__jobTitle'
    def set_jobTitle(self, employee_jobTitle):
        self.__jobTitle = employee_jobTitle
    # get_jobTitle() returns the value assigned to '__jobTitle' to the statement that calls it
    def get_jobTitle(self):
        return self.__jobTitle