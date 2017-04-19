from employee import *

class Full_Time(object):
    """ Represents full time 40 hour work week employees.
    """

    def __init__(self):
        self.hours_per_week = 40

class Part_Time(object):
    """ Represents full time 40 hour work week employees.
    """

    def __init__(self):
        self.hours_per_week = 24

class Network_Switch_Access(object):
    """ Grants access card to Network Switch employees
    """

    def __init__(self):
        self.switch_access: True

class Network_Switch(Employee, Full_Time, Network_Switch_Access):
    """ Creates and employee that works in the Network Switch
    """

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        Full_Time.__init__(self)
        Network_Switch_Access.__init__(self)
        print("{} the {} has been granted access to the Network Switch".format(first_name, last_name))
