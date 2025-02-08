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
                         3: post
                         4:message a frnd
                         5: any key to exit
                          """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.message()
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

    def post(self):
        if self.login:
            print("Enter your post")
            post=input()
            print("Post successfull :-->",post)
            self.menu()
        else:
            print("You need to login first")
            self.menu()
    def message(self):
        if self.login:
            message=input("enter your message")
            user=input("Enter username to send message")
            print("Message sent to",user)
            self.menu()
        else:
            print("You need to login first")
            self.menu()   
#obj1=chatbook()