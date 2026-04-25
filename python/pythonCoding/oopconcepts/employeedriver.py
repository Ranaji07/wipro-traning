from oopconcepts.employeedetails import EmployeeDetails

#driver
eno = int(input('Emp no : '))
name = input('Emp name : ')
bp = float(input('basic pay : '))
employee = EmployeeDetails(empno=eno, ename=name, basic_pay=bp)
print('Emp no : ',employee.empno)
print('Emp name : ',employee.ename)
print('Basic pay : ',employee.basic_pay)
print('Salary : ', employee.calculate_netsal())

