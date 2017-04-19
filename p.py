from bangazon import *
from departments import *
from employee import *
from security import *

op_dept = Operations("Ops Department", "Johnny Incharge", 10)
op_dept.add_truck_count(9)

print(op_dept.name)
print(op_dept.truck_count)
print(op_dept.supervisor)
print(op_dept.employee_count)
op_dept.meet()
print(op_dept.dept_budget())
print("-----------------------------------")

it_dept = IT("IT Department", "Suzy Incharge", 5)
it_dept.add_licensed_program("Windows 10")

print(it_dept.name)
print(it_dept.licensed_programs)
print(it_dept.supervisor)
print(it_dept.employee_count)
it_dept.meet()
print(it_dept.dept_budget())

hr_dept = HumanResources("HR Department", "Tom Coughlin", 9)
sales_dept = Sales("Sales Department", "Jimmy John", 15)

print("-----------------------------------")

james_tonkin = Employee("James", "Tonkin")
print(james_tonkin.full_name)
james_tonkin.eat()
james_tonkin.eat(food="sandwich")
james_tonkin.eat(companions=["Sam", "Dean", "Alice"])
james_tonkin.eat("pizza", ["Sam", "Dean", "Alice"])
print("-----------------------------------")

Network_Switch("Harambe", "Gorilla")
print("-----------------------------------")

# Employees
bill_murray = Employee("Bill", "Murray")
john_candy = Employee("John", "Candy")
gilda_radner = Employee("Gilda", "Radner")
jane_curtain = Employee("Jane", "Curtain")
dan_akroyd = Employee("Dan", "Akroyd")
chevy_chase = Employee("Chevy", "Chase")
eddie_murphy = Employee("Eddie", "Murphy")
jim_belushi = Employee("Jim", "Belushi")

# Add Emps to departments
it_dept.add_employee(bill_murray)
it_dept.add_employee(john_candy)
op_dept.add_employee(gilda_radner)
op_dept.add_employee(dan_akroyd)
hr_dept.add_employee(jane_curtain)
hr_dept.add_employee(chevy_chase)
sales_dept.add_employee(eddie_murphy)
sales_dept.add_employee(jim_belushi)

print("{}:".format(hr_dept.name))
hr_dept.get_employees()
print()
print("{}:".format(it_dept.name))
it_dept.get_employees()
print()
print("{}:".format(op_dept.name))
op_dept.get_employees()
print()
print("{}:".format(sales_dept.name))
sales_dept.get_employees()
print()
