class Department(object):
    """Parent class for all departments"""

    def __init__(self, name, supervisor, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.budget = 100000
        self.employees = set()

    @property
    def name(self):
        """ Gets the department name
        """
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        """ Sets the department name
        """
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a supervisor name")

    @property
    def supervisor(self):
        """ Gets the supervisor name
        """
        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        """ Sets the supervisor name
        """
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a department name")

    @property
    def employee_count(self):
        """ Gets the number of employees
        """
        try:
            return self.__employee_count
        except AttributeError:
            return ""

    @employee_count.setter
    def employee_count(self, val):
        """ Sets the number of employees
        """
        if not isinstance(val, int):
            raise TypeError('Please provide an integer value for employee count')

        if val is not "":
            self.__employee_count = val
        else:
            raise ValueError("Please provide an integer for employee count")

    def meet(self):
        """ Prints meeting place
        """

        print("Everyone meet in {}'s office".format(self.supervisor))

    def dept_budget(self):
        """ Sets the base budget for each department
        """

        return self.budget

    def add_employee(self, employee):
        self.employees.add(employee)
        return self.employees

    def remove_employee(self, employee):
        self.employees.remove(employee)
        return self.employess

    def get_employees(self):
        for employee in self.employees:
            print(employee.full_name)
