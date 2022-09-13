import re
def check_pass(pswd):
    if (len(pswd) < 8): 
        print("the password is too short")
    if (len(pswd) > 8):
        print ("the password is too long")
    res = any(chr.isdigit() for chr in pswd)
    if res==False: 
        print("the password must have numbers in it")
        
    lc = re.search('[a-z]', pswd)
    if(lc is None):
        print("there must be at least one lowercase letter")
    uc = re.search('[A-Z]', pswd)
    if(uc is None):
        print("there must be at least one uppercase letter")

    special_chr = "*-#"
    if any(chr in special_chr for chr in pswd) == False:
              print("there must be at least one special character(*-#)")
              
    spec_chr = "!@$%^&()+?_=,<>/"
    if any(chr in spec_chr for chr in pswd):
        print("use only allowed special characters! *, - or #")


    x=0
    if (x==0):
        if (len(pswd)== 8 and res==True
            and any(chr in special_chr for chr in pswd)
            and (uc is not None) and (lc is not None)):
            print("password accepted")

while True:
    pswd = input("enter your password: ")
    check_pass(pswd)
