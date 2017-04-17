from departments import *

op_dept = Operations("Ops Department", "Johnny Incharge", 10)
op_dept.add_truck_count(9)

print(op_dept.name)
print(op_dept.truck_count)
print(op_dept.supervisor)
print(op_dept.employee_count)

it_dept = IT("IT", "Suzy Incharge", 5)
it_dept.add_licensed_program("Windows 10")

print(it_dept.name)
print(it_dept.licensed_programs)
print(it_dept.supervisor)
print(it_dept.employee_count)
