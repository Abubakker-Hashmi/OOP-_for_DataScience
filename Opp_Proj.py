class chatbook:
    def __init__(self):
        self.uname=""
        self.password=""
        self.loggedin=False
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
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()



obj1=chatbook()