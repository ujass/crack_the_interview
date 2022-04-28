"""
Here we learn about propertu decorator. 
Use- When we have already code the things and we change the basic instance values.
    at that time, this thigns comes handy. 
"""


class Employee:

    def __init__(self, first, last):
        self.first = first 
        self.last = last 

    # we write propery like methods and access it like attribute. 
    @property
    def email(self):
        return "{}.{}.@email.com".format(self.first, self.last)
        # return f'{self.first}.{self.last}.@email.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)
        # return f'{self.first} {self.last}' 

emp = Employee('ujeshn', 'nada')

emp.first = 'ishan'
print(emp.first)    
print(emp.email)