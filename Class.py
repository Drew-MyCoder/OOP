class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1
        
    # @property decorator, makes we access the email as an attribute 
    #instead of as a method
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last - last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # this is represntational and useful for debugging
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # this prints a strings form. user friendly and readable
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    # to create a method to add emps pay
    def __add__(self, other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str .split('-')
        return cls(first, last, pay)
    
    # with static method, no cls argument is passed
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'today is a weekend'
        return 'Today is a weekday'

emp_1 = Employee('Andrews', 'Osei', 5000)
emp_2 = Employee('Kyere', 'Dwomoh', 6000)

# print(emp_1)
# print(emp_2)


#fullname is a method instead of an attribute
# thats why we write it as fullname()
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.num_of_emps)

# emp_str_1 = 'John-Doe-7000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2023, 12, 9)

# print(Employee.is_workday(my_date))

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # instaed of super we can also be written as
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # to add new employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Andrews', 'Osei', 5000, 'Python')
dev_2 = Developer('Kyere', 'Dwomoh', 6000, 'Java')

# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# mgr_1 = Manager('Drew', 'Kofi', 9000, [dev_1])
# print(mgr_1.fullname())
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()

print(emp_1 + emp_2)
