class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

def serialize_emp(emp, filename):
    data = f"{emp.empcode},{emp.empname},{emp.doj},{emp.salary}\n"
    file = open(filename, 'w')
    file.write(data)
    file.close()
    print(f"Saved to '{filename}'")

def deserialize_emp(filename):
    file = open(filename, 'r')
    data = file.readline().strip().split(',')
    file.close()
    if len(data) == 4:
        return Employee(data[0], data[1], data[2], data[3])
    else:
        print("Error reading data")
        return None

emp = Employee("101", "Rajesh", "2023-08-15", "50000")
file_name = "emp.txt"
serialize_emp(emp, file_name)
loaded_emp = deserialize_emp(file_name)

if loaded_emp:
    print(f"Code: {loaded_emp.empcode}, Name: {loaded_emp.empname}, Joined: {loaded_emp.doj}, Salary: {loaded_emp.salary}")
