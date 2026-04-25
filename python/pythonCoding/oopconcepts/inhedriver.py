from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.teacher import Teacher

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('City: ')
rno = int(input('Roll No:'))
sn = int(input('S Name:'))
m1 = int(input('M1:'))
m2 = int(input('M2:'))
m3 = int(input('M3:'))
eid = int(input('Eid: ')
tn = input('Teach Name: ')
de = input('Dept Name: ')
bp = float(input('Bp: '))

# project = College(ccode=cc, cname=cn, ccity=ci)
#
# project.welcome_message()
# project.display_college_details()

project = StudentGrade(ccode=cc, cname=cn, ccity=cc, rno=rno, sname=sn, m1=m1, m2=m2, m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll no: {project.rollno} \t Name: {project.stuname} \n''Total: {project.calculate_total()} \nAverage: {project.calculate_average()}')
project.calculate_grade()
print(f'Result : {project.result} \t Grade: {project.grade}')

teach = Teacher(ccode=cc, cname=cn, ccity=ci, eid=eid, tn=tn, de=de, bp=bp)
print(f'Eid: {tech.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')
