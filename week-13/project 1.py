import pandas as pd

class smis():

        def input(self):
                num_students = int(input("Enter number of students: "))

                names = []
                matric_numbers = []
                departments = []
                levels = []
                for i in range(num_students):
                        print(f"\nEnter details for students {i + 1}:")
                        NAME = input("What is your name: ")
                        MATRIC_NO = input("Matric Number: ")
                        Department = input("What department are you in?: ")
                        LEVEL = input("LEVEL: ")

                names.append(NAME)
                matric_numbers.append(MATRIC_NO)
                departments.append(Department)
                levels.append(LEVEL)
                SMIS = {'STUDENT NAME': names,
                        'MATRIC NUMBER': matric_numbers,
                        'DEPARTMENT': departments,
                        'LEVEL': levels}
                df = pd.DataFrame(SMIS)
                print(df)
                df.to_csv("SMIS.csv")

S = smis()
S.input()