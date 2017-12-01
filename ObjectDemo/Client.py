from ObjectDemo.Employee import Employee

class Client:

    emp=Employee("Akash",10000)
    print(emp.getName()," ",emp.salary)
    emp.setName("Karan")
    print(emp.getName()," ",emp.salary)