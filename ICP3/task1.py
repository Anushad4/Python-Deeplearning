class Employee:
    countEmployees = 0
    salaries = []

    #Default constructor function
    #init method which allows to intilize the object and self attribute which can access methods and attributes
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #appending salaries to the list
        Employee.salaries.append(self.salary)
        Employee.countEmployees = Employee.countEmployees + 1

    #Average salary of all employess
    def avgsalary(self, salaries):
        length = len(salaries)
        totalsalary = 0
        for salary in salaries:
            totalsalary = totalsalary + salary
        print("Average Salary = ", totalsalary/length)


#Full time Employee class
class FulltimeEmployee(Employee):
    empId = 0
    def __init__(self, empId, name, family, salary, department):
        self.empId = empId
        Employee.__init__(self, name, family, salary, department)
        FulltimeEmployee.empId = FulltimeEmployee.empId + 1

Employee1 = Employee("anu", "muppalla", 5000, "CSE")
Employee2 = Employee("chikki", "somala", 8000, "ECE")
Employee3 = Employee("raj", "londiriki", 9000, "MPharmcy")
Employee4 = Employee("rajee", "medi", 8000, "BPharmcy")

FulltimeEmployee1 = FulltimeEmployee(1, "Sunny", "Vuyyala", 10000, "ECE",)
FulltimeEmployee2 = FulltimeEmployee(2, "Seetha", "vemuri", 15000, "civil")

print("Employee1 Name is: ", Employee1.name)
print("Employee2 Name is: ", Employee2.name)
print("Employee3 Name is: ", Employee3.name)
print("Employee4 Name is: ", Employee4.name)

print("Fulltime Employee1 Name is: ", FulltimeEmployee1.name)
print("Fulltime Employee2 Name is: ", FulltimeEmployee2.name)

# Access data member using FulltimeEmployee class
print("Number of Employees: ", Employee.countEmployees)
print("Fulltimeemployee id's:", FulltimeEmployee.empId)
FulltimeEmployee1.avgsalary(FulltimeEmployee.salaries)