#  this programme checks on the user inputs and validate it 
print ("this programme needs the credentials to verify them to give grant access to users")

username = "rapahael"
password = "raphael2025"

if username == "raphael" and password == "raphael2025":
    print("signed in succesfully!!")

else:
    print("wrong credentials")


username = input("Enter your username")
password = input("Enter your password")

if username == "raphael" and password == "raphael2025":
    print("signed in succesfully!!")
elif username != "raphael" and password == "raphael2025":
    print("check your credentials and try again!!") 

else:
    print("Wrong credentials")