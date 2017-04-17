import random

class Employee(object):
    """Parent class for employees

    Methods: __init__, eat
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name

    def eat(self, food=None, companions=None):
        """ Method to randomly choose a restaurant with possible variables of food eaten
        and companions.
        """

        restaurant = ["Pinewood Social", "Five Points Pizza", "Brown's Diner", "Hattie B's", "Biscuit Love"]
        self.restaurant = random.choice(restaurant)
        self.food = food
        self.companions = companions

        if food is None and companions is None:
            print("{} ate at {}".format(self.full_name, self.restaurant))
            return self.restaurant
        elif food is "sandwich" and companions is None:
            print("{} ate a {} at the office.".format(self.full_name, self.food))
        elif food is None:
            print("{} ate at {} with {}".format(self.full_name, self.restaurant, ", ".join(self.companions)))
        else:
            print("{} ate {} at {} with {}".format(self.full_name, self.food, self.restaurant, ", ".join(self.companions)))
