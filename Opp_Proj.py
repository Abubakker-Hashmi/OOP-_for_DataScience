class chatbook:
    __user_id=1 #accesing this class name will be used 
    def __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.__name="edward"  # double underscore means private
        self._fnam="jinner" #protected
        self.uname="879"
        self.password="345"
        self.login=False
       # self.menu()
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
    @staticmethod
    def set_id(id):  # chatbook.set_id(9)     #static method access using class name
        chatbook.__user_id=id
    @staticmethod    
    def get_id():
        return chatbook.__user_id
    
    def get_name(self):
        return(self.__name)
    
    def set_name(self,name):
        self.__name=name
        return('')
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
#creating attributes outside of the class
