# performing the for loop in our programs 
for number in range(10):
    print(number)


for number in range(10):
    print(number *"#")



for number in range(10):
    if number %2 == 0:
     print (number )

for number in range(10):
    if number %2 == 1:
     print (number )

# performing the while loop in our program: checks access control
trial = 3
attempt = 0

while attempt <trial:
    value = input("Enter the passowrd") 
    if value == "raphael1234":
        print("login succesfully")
   
        break
    else:
         print("the password is wrong try again")
    attempt+=1
    
else: 
    print("you failed number of attempts are over!!")