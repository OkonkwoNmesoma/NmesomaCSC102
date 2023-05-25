import pandas as pd


def comp_science():
    jamb_score = float(input("What is your jamb score: "))
    math = float(input("Input result for your math WAEC result: "))
    eng = float(input("Input result for your English WAEC result: "))
    chem = float(input("Input result for your Chemistry WAEC result: "))
    phy = float(input("Input result for your Physics WAEC result: "))
    bio = float(input("Input result for your Biology WAEC result: "))
    if jamb_score >= 230 and math >= 60 and chem >= 60 and phy >= 60 and bio >= 60:
        print(f"CONGRATULATIONS {name} YOU HAVE BEEN ADMITTED INTO PAN-ATLANTIC UNIVERSITY")
        info = {'NAME':[{name}],
                'JAMB_SCORE':[{jamb_score}],
                'MATH':[{math}],
                'ENGLISH':[{eng}],
                'CHEMISTRY':[{chem}],
                'PHYSICS':[{phy}],
                'BIOLOGY':[{bio}]
        }
        df = pd.DataFrame(info)
        df.to_csv('admitted.csv')
    else:
        info = {'NAME':[{name}],
                'JAMB_SCORE':[{jamb_score}],
                'MATH':[{math}],
                'ENGLISH':[{eng}],
                'CHEMISTRY':[{chem}],
                'PHYSICS':[{phy}],
                'BIOLOGY':[{bio}]
        }
        df = pd.DataFrame(info)
        df.to_csv('not-admitted.csv')

def mass_comm():
    jamb_score = float(input("What is your jamb score: "))
    math = float(input("Input result for your math WAEC result: "))
    eng = float(input("Input result for your English WAEC result: "))
    econs = float(input("Input result for your Chemistry WAEC result: "))
    commerce = float(input("Input result for your Economics WAEC result: "))
    account = float(input("Input result for your Financial Accounting WAEC result: "))
    if jamb_score >= 220 and  math >= 60 and eng >= 60 and econs >= 60 and commerce >= 60 and account >= 60:
        print(f"CONGRATULATIONS {name} YOU HAVE BEEN ADMITTED INTO PAN-ATLANTIC UNIVERSITY")
        info = {'NAME': [{name}],
                'JAMB_SCORE': [{jamb_score}],
                'MATH': [{math}],
                'ENGLISH': [{eng}],
                'ECONOMICS': [{econs}],
                'COMMERCE': [{commerce}],
                'ACCOUNT':[{account}]
                }
        df = pd.DataFrame(info)
        df.to_csv('admitted.csv')
    else:
        print("You failed to meet the minimum requirement for admission")
        info = {'NAME': [{name}],
                'JAMB_SCORE': [{jamb_score}],
                'MATH': [{math}],
                'ENGLISH': [{eng}],
                'ECONOMICS': [{econs}],
                'COMMERCE': [{commerce}],
                'ACCOUNT': [{account}]
                }
        df = pd.DataFrame(info)
        df.to_csv('not-admitted.csv')

print("ADMISSION VALIDATOR")
name = input("NAME: ")
department = float(input("Pick 1 for Comp.Science and 2 for Mass comm."))
if department == 1:
    comp_science()
elif department == 2:
    mass_comm()
else:
    print("Invalid Input")