from bangazon import *
from departments import *
from employee import *

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
