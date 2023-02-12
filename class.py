class details:
    def email(self):
        print(self.a+"."+self.b+"@gmail.com")
    def names(self):
        a=str(input("Enter First name"))
        b=str(input("Enter Second name"))
        c=int(input("Enter Pay "))
        self.a=a
        self.b=b
        self.c=c
    
    
p1=details()
p1.names()
p1.email()
