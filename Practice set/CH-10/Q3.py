#Create a Class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def _init_(self , name , salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Shreya",120000000 , 250000000)
print(p.name, p.salary , p.pin , p.company)
r = programmer("Abhi",120000000 , 250000000)
print(r.name, r.salary , r.pin , r.company)
        




