from bangazon import *

class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count):
        """ Initial setup of the subclass
        """
        super().__init__(name, supervisor, employee_count)
        self.policies = set()
        self.budget = super().dept_budget() - 50000

    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
            policy_name (string)
            policy_text (string)
        """

        self.policies.add((policy_name, policy_text))

    def meet(self):
        '''Prints a message identifying a meeting location specifically for the Human Resources department
        '''
        print("Everyone meet in the conference room #1.")



class IT(Department):
    """ Class for representing the IT department

    Methods: __init__, add_licensed_program
    """

    def __init__(self, name, supervisor, employee_count):
        """ Initial setup of the subclass
        """
        super().__init__(name, supervisor, employee_count)
        self.licensed_programs = list()
        self.budget = super().dept_budget() + 50000

    def add_licensed_program(self, software_name):
        """Adds a software program to the list of programs

        Arguments:
            software_name (string)
        """

        self.licensed_programs.append(software_name)

    def meet(self):
        '''Prints a message identifying a meeting location specifially for the IT department
        '''
        print("Everyone meet in the server room.")

class Operations(Department):

    """ Class for representing the Operations department

    Methods: __init__, add_truck_count
    """

    def __init__(self, name, supervisor, employee_count):
        """ Initial setup of the subclass
        """
        super().__init__(name, supervisor, employee_count)
        self.truck_count = 0
        self.budget = super().dept_budget() + 100000

    def add_truck_count(self, number_of_trucks):
        """Adds the number of trucks in the operations department.

        Arguments:
            number_of_trucks (integer)
        """

        self.truck_count = number_of_trucks

    def meet(self):
        '''Prints a message identifying a meeting location specifially for the Operations department
        '''
        print("Everyone meet in the motor pool.")

class Sales(Department):

    """ Class for representing the Sales department

    Methods: __init__, add_customer_count
    """

    def __init__(self, name, supervisor, employee_count):
        """ Initial setup of the subclass
        """
        super().__init__(name, supervisor, employee_count)
        self.customer_count = 0
        self.budget = super().dept_budget() - 75000

    def add_customer_count(self, number_of_customers):
        """Adds the number of customer accounts in the Sales department.

        Arguments:
            number_of_customers (integer)
        """

        self.customer_count = number_of_cusomers

    def meet(self):
        '''Prints a message identifying a meeting location specifially for the Sales department
        '''
        print("Everyone meet in conference room #2.")
