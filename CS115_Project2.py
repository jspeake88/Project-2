# CS115_Project2.py
# 'Employee prompt' OOP class/object practice
# source code developed by: Justin Speake
# ---------------------------------------------
# This program will import a module containing the declaration and structure for the
# 'Employee()' class that will be used to create the objects used in this program.
# The objects will then archive the input collected from the end-user and fetch the
# information to be output when the appropriate methods are called.
# A main function will be defined and ran to collect the input the data and create
# the objects that will be used.
# A function will be defined and ran to format the output in the style of a table.
# -------------------------------------------------------------------------------------

# Import the 'employee' module containing the definition of the 'Employee()' class.
import employee

# define the 'main()' function.
# 'main()' will create three objects of the 'Employee()' class
# 'main()' then collects input for all three objects and assigns it to the
# appropriate attribute using that object's 'set' methods
# 'main()' will then call 'displayEmployees()'
def main():
    # Create and initialize objects using 'Employee()' class
    employee1 = employee.Employee()
    employee2 = employee.Employee()
    employee3 = employee.Employee()

    # assign values to variables that will be passed to 'employee1'
    # as well as name of the business (to be used in output function)
    business_name = str(input("What's the name of the business? "))
    employee_name = str(input("What's the 1st employee's name? "))
    ID_number = str(input("What's the 1st employee's ID number? "))
    employee_department = str(input("What's the 1st employee's department? "))
    employee_jobTitle = str(input("What's the 1st employee's job title? "))

    # pass values of variables collected to object employee1 via parameters of input methods
    employee1.set_name(employee_name)
    employee1.set_IDnumber(ID_number)
    employee1.set_department(employee_department)
    employee1.set_jobTitle(employee_jobTitle)

    # assign values to variables that will be passed to 'employee2' object
    employee_name = str(input("What's the 2nd employee's name? "))
    ID_number = str(input("What's the 2nd employee's ID number? "))
    employee_department = str(input("What's the 2nd employee's department? "))
    employee_jobTitle = str(input("What's the 2nd employee's job title? "))

    # pass values of variables collected to object employee1 via parameters of input methods
    employee2.set_name(employee_name)
    employee2.set_IDnumber(ID_number)
    employee2.set_department(employee_department)
    employee2.set_jobTitle(employee_jobTitle)

    # assign values to variables that will be passed to 'employee2' object
    employee_name = str(input("What's the 3rd employee's name? "))
    ID_number = str(input("What's the 3rd employee's ID number? "))
    employee_department = str(input("What's the 3rd employee's department? "))
    employee_jobTitle = str(input("What's the 3rd employee's job title? "))

    # pass values of variables collected to object employee1 via parameters of input methods
    employee3.set_name(employee_name)
    employee3.set_IDnumber(ID_number)
    employee3.set_department(employee_department)
    employee3.set_jobTitle(employee_jobTitle)

    # Call 'displayEmployees(parameters)' function and pass object information through parameters
    displayEmployees(employee1, employee2, employee3, business_name)



# define the 'displayEmployees(parameters)' function to be called to provide output
def displayEmployees(employee_obj1, employee_obj2, employee_obj3, business):
    print()
    print('\t\t\t', business)
    print(format('EMPLOYEE NAME', '13'),'\t\t',\
            format('IDENTIFIER', '10'),'\t',\
            format('DEPARTMENT', '10'),'\t',\
            format('TITLE', '15'))
    print(format('_____________', '13'),'\t\t',\
            format('__________', '10'),'\t',\
            format('__________', '10'), '\t',\
            format('__________', '15'))
    # Display information for 1st 'Employee()' object
    print(format(employee_obj1.get_name(), '13'),'\t\t',\
            format(employee_obj1.get_IDnumber(), '10'),'\t',\
            format(employee_obj1.get_department(),'10'),'\t',\
            format(employee_obj1.get_jobTitle(),'15'))
    # Display information for 2nd 'Employee()' object
    print(format(employee_obj2.get_name(), '13'),'\t\t',\
            format(employee_obj2.get_IDnumber(), '10'),'\t',\
            format(employee_obj2.get_department(),'10'),'\t',\
            format(employee_obj2.get_jobTitle(),'15'))
    # Display information for 3rd 'Employee()' object
    print(format(employee_obj3.get_name(), '13'),'\t\t',\
            format(employee_obj3.get_IDnumber(), '10'),'\t',\
            format(employee_obj3.get_department(),'10'),'\t',\
            format(employee_obj3.get_jobTitle(),'15'))

# Call main function
main()