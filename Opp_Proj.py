class chatbook:
    def __init__(self):
        self.uname=""
        self.password=""
        self.login=False
        self.menu()
    def menu(self):
        user_input=input("""Welcome ,Enter your choice:
                         1:Signup
                         2: signin
                         3:chat
                         4:message a frnd
                         5: any key to exit
                          """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        self.uname=input("Enter your username")
        self.password=input("Enter your password")
        print("Signup successfull")
        print()
        self.menu()

    def signin(self):
        if self.uname=="":
            print("You need to signup first")
            self.menu()
        else:
            uname=input("Enter your username")
            password=input("input your password")
            if self.uname==uname and self.password==password:
                self.login=True
                print("Login successfull")
                
            else:
                print("Invalid username or password")
                self.menu()
        self.menu()
obj1=chatbook()