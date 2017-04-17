class Department(object):
    """Parent class for all departments"""

    def __init__(self, name, supervisor, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a supervisor name")

    @property
    def supervisor(self):
        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a department name")

    @property
    def employee_count(self):
        try:
            return self.__employee_count
        except AttributeError:
            return ""

    @employee_count.setter
    def employee_count(self, val):
        if not isinstance(val, int):
            raise TypeError('Please provide an integer value for employee count')

        if val is not "":
            self.__employee_count = val
        else:
            raise ValueError("Please provide an integer for employee count")
