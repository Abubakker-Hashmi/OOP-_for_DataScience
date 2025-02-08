class employee:
    #Constructor  automatically called when object is created
    # self is act as a pointer to object or may be called a object
    def __init__(self):
        self.name="abubakker"
        self.salary=50000
        self.designation="Datascientist"
        # print("Name:",self.name,"Salary:",self.salary,"Designation:",self.designation)
    #Method       manually called by object
    def travel(self,destination):
        print(self.name,"is Traveling to ",destination)
Emp1=employee()
Emp2=employee()
Emp1.travel("Larkana")
 

