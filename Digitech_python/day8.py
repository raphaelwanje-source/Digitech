# #defining a function
# def get_pass(name, age):
#     if age <= 17:
#         return f"{name}, your are not allowed to go in!!"
#     else: 
#         return f"{name}, your are allowed to go in!!"
    
# #generate the actual name and age

# user_name = input ("Enter your name: ")
# user_age = int(input("Enter your age:"))


# final = get_pass(user_name, user_age)
# print(final)



def get_access():
    name = input("Enter your name:")
    age = int(input("Enter your age: "))
    if age <= 17:
        print(f"{name}, You are not allowed to go in!!")
    else: print (f"{name}, You are are allowed to go in!!")
get_access()


#error handling 1
def get_access():
    try:    
        name = input("Enter your name:")
        age = int(input("Enter your age: "))
        if age <= 17:
            print(f"{name}, You are not allowed to go in!!")
        else: 
            print (f"{name}, You are are allowed to go in!!")
    except ValueError:
        print("This is how we use error handling")

get_access()


#error handling 2
def get_access():
    try:    
        name = input("Enter your name:")
        age = int(input("Enter your age: "))
        if age <= 17:
            print(f"{name}, You are not allowed to go in!!")
        else: 
            print (f"{name}, You are are allowed to go in!!")
    except:
        print("Umekosea mahali jaribu tena")

get_access()

