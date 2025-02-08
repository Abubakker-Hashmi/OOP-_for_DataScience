                                ### Simple Inheritence 
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(self.name,"makes a sound")

# # Derived Class  can't iherit private methods
# class Dog(Animal):
#     def speak(self):
#         print(self.name,"barks")  #overrides the above speak method


# animal=Animal("Baby")
# c_animal=Dog("Dog")

# animal.speak()
# c_animal.speak() 

                            ## Constructor Overloading
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(self.name,"makes a sound")

# # Derived Class  can't iherit private methods
# class Dog(Animal):
#     def __init__(self):
#         self.behaviour="Freindly"
#     def speak(self):
#         print("bunny barks and his behavior is",self.behaviour)  #overrides the above speak method


# # animal=Animal("Baby")
# c_animal=Dog()

# # animal.speak()
# c_animal.speak()


                            ### Super Keyword   only be called within class(derived)
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(self.name,"makes a sound")

# Derived Class  can't iherit private methods,cant access attributes
class Dog(Animal):
    def __init__(self, name,age,breed):    # child class constructor
        super().__init__(name,age)         # parent class constructor 
        self.behaviour="Freindly"
        self.breed=breed
    def speak(self):
        super().speak()
        print(self.name," barks his age is",self.age," and his behavior is",self.behaviour,"breed is",self.breed)  #overrides the above speak method


# animal=Animal("Baby")
c_animal=Dog("Buddy",16,"gold digger")

# animal.speak()
c_animal.speak()