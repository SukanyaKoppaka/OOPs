class employee:
    company_name="TechSolution"
    def __init__(self):
        self.name=input("enter employee name:")
        self.emp_id=input("enter ID:")
        self.salary=int(input("enter salary:"))
    def display_details(self):
        print("company:",employee.company_name)
        print("employee:",self.name)
        print("employeee id:",self.emp_id)
        print("salary:",self.salary)
    @classmethod
    def change_company_name(cls,new_company):
        cls.company_name=new_company
    @staticmethod
    def validate_salary(obj):
        salary=obj.salary
        if salary>0:
            print("the salary is greater than zero and the salary is:",salary)
        else:
            print("invalid salary")

class developer(employee):
    def __init__(self,lang):
        self.pro_lang=lang
        super().__init__()
    def write_code(self):
        print(f"{self.name} is writing code using {self.pro_lang}")
        

class projectmanager(employee):
    def __init__(self):
        self.team_size = 5
        super().__init__()
    def task_logger(assign_task):
        def inner(self, task_name):
            print()
            print("task execution started")
            assign_task(self, task_name)
            print("task execution completed")
            print()
        return inner
    @task_logger
    def assign_task(self,task_name):
        print("task assigned :",task_name)

obj1=developer("python")
obj3=projectmanager()
obj1.display_details()
obj1.write_code()
obj3.assign_task("develop login page")
employee.change_company_name("codecraft solutions")
print("company name updated to ",obj1.company_name)

print("********************************************")
obj2=developer("java")
obj2.display_details()
obj2.write_code()
obj3.assign_task("develop login page")
obj2.change_company_name("tech mahindra")
print("company name updated to ",obj2.company_name)