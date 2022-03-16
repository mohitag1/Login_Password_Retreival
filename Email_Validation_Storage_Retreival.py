# Python program to validate an Email
#An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, a “personal_info” and a domain, that is personal_info@domain.


import re

filename="data.txt"
regexForEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'


# Define a function for
# for validating an Email


def check(email):
        flag=0
	# pass the regular expression
	# and the string into the fullmatch() method
        if(re.fullmatch(regexForEmail, email)):
                print("Valid Email")
                flag=0
        else:
                print("Invalid Email")
                flag=1
        return flag


def Registration():
    
    email= input("Please enter email id you want to register eg. abc@gmail.com\n")
    password= input("Please enter password\n")
    flag=check(email)
    ret=password_check(password)
    #validate password
    if(flag==0 and ret==0):
            fh= open(filename,"w")
            #email+="\n"
            fh.write(email+"\c")
            fh.write(password)
            fh.close()
            return 0
##   else:
##           print("Cannot write to file, as password does not meet policy\n")
    
def ReadFileDetails():
    f = open(filename, "r")
    filedata=f.read()
    #print(filedata)
    filedata=filedata.split("\c")
    return filedata

def password_check(password):
        
        # Python program to check validation of password
# Module of regular expression is used with search()

        flag = 0
        while True:
                if (len(password)>16 or len(password)<5):
                        flag = -1
                        break
                elif not re.search("[a-z]", password):
                        flag = -1
                        break
                elif not re.search("[A-Z]", password):
                        flag = -1
                        break
                elif not re.search("[0-9]", password):
                        flag = -1
                        break
                elif not re.search("[_@$]", password):
                        flag = -1

                else:
                        flag = 0
                        print("Valid Password")
                        break
                print("IN LOOP\n")
        if flag ==-1:
                print("Not a Valid Password")

        return flag



############################# SKELETON OF MAIN PROGRAM

inp="y"
while(inp == "y"):
    usecase =int(input("Please provide input either of following numbers(0/1/2) \n 0: For Registration \n 1 For Login \n 2 For Password Retrieval\n"))
    match usecase:
        case 0:
            #Registration
            ret=Registration()
            if(ret==0):
                    print("Registration Successful\n")
            else:
                  print("Registration Failed\n")  
            #break# NO NEED OF BREAK IN PYTHON 
        
        case 1:
            #Login
             email= input("Please enter email id to  login  eg. abc@gmail.com\n")
             password= input("Please enter password\n")
             
             filedata=ReadFileDetails()
             emailIDInFile=filedata[0]
             passwdInFile=filedata[1]
             print(emailIDInFile)
             print(passwdInFile)
             if(email==emailIDInFile and password==passwdInFile):
                 print("LOGIN SUCCESSFUL \n")
             else:
                 print("LOGIN FAILED \n PLEASE REREGISTER")
                 Registration()
             
             
            #break

        case 2:
            #password Retrieval
            emailId= input("Please enter email id for to retrive password\n")
            filedata=ReadFileDetails()
            emailIDInFile=filedata[0]
            passwdInFile=filedata[1]
            if(emailId==emailIDInFile):
                 print(passwdInFile)
            else:
                    print("INVALID LOGIN ID") 
           
            #break

    #print("OUT OF MATCH CASE, IN WHILE LOOP")    

    inp=input("Do you want to continue type y if not type n\n")   
    #print(inp)
#print("OUT OF WHILE LOOP")     
