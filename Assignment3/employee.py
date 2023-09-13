"""
  File: employee.py
  Description: A class implementation of an employee management system

  Student Name: Quentin Schuelke
  Student UT EID: qcs86 

  Partner Name: Daniela Cordon
  Partner UT EID: dc47324

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09/11/23
  Date Last Modified: 09/xx/23
"""

class Employee:
    """General implementation of an employee class"""
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.identifier = kwargs.get("identifier", None)
        self.salary = kwargs.get("salary", None)
    

    def __str__(self):
        """String Representation of the employee"""
        return f"{self.name} (ID:{self.identifier}) is an employee"



############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """Permanent employee which inherits from employee and qualifies for benefits"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits", None)


    def cal_salary(self):
        """checks benefits and returns adjusted salary"""
        if "health_insurance" in self.benefits:
            if "retirement" in self.benefits:
                return float(self.salary * 0.7)
            else:
                return float(self.salary * 0.9)
        else: 
            return float(self.salary * 0.8)


    def __str__(self):
        """String representation of a permanent employee"""
        return f"{self.name} (ID:{self.identifier}) is a permanent employee"


############################################################
############################################################
############################################################

class Manager(Employee):
    """Manager, which inherits from employee, but gets a bonus"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus", None)

    
    def cal_salary(self):
        """returns adjusted salary after bonus"""
        return float(self.salary + self.bonus)
        


    def __str__(self):
        """String representation of a manager"""
        return f"{self.name} is a manager"



############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    """Temporary employee that inherits from employee and accounts for hours worked per month"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours", None)
        
    
    def cal_salary(self):
        """Returns salary adjusted for hours worked"""
        return float(self.hours * self.salary)
        

    def __str__(self):
        """String representation of a temporary employee"""
        return f"{self.name} (ID:{self.identifier}) is a temporary employee"
        

    
############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """Consultant which inherits from temprary employee and gets paid for travel"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel", None)
  

    def cal_salary(self):
        """Adjusts salary based on amount of travel"""
        return float(super().cal_salary() + 1000 * self.travel)
  

    def __str__(self):
        """String representation of Consultant"""
        return f"{self.name} (ID:{self.identifier}) is a consultant"
  
############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    """Consultant Manger, who inherits from both consultant and manager"""
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
 

    def cal_salary(self):
        """Returns adjusted salary based on bonus and travel"""
        return float(super().cal_salary() + self.bonus)
 
    def __str__(self):
        """String representation of Consultant Manager"""
        return f"{self.name} (ID:{self.identifier}) is a consultant manager"
 


############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()



