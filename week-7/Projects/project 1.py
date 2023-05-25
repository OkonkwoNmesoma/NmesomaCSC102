import pandas as pd
data = pd.read_csv("jt-ventures.csv")
data
print("Program to verify employees oj jt-ventures")
name1 = str.casefold(input("What is your Surname?: "))
name2 = str.casefold(input("What is your first name?: "))
department = input("What is your department?: ")

if ((data["SURNAME"] == name1) & (data["DEPARTMENT"]  == department)).any():
    print(f"Welcome {name1,name2} to jt-ventures")
else:
    print("This User does not exist")