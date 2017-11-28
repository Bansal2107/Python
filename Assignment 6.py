names=[]
age=[]
email=[]

for counter in range(0,3):
    names.append(input("Enter name "))
    age.append(input("Enter age "))
    email.append(input("Enter email "))

for counter in range(0,3):
    print("\nDetails of Person:",counter+1)
    print("Name: ",names[counter])
    print("Age: ", age[counter])
    print("Email: ", email[counter])


