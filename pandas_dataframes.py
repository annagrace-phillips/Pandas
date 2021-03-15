import pandas as pd

grades_dict = {'Wally': [87,96,70], 
             'Eva': [100,87,90]
             'Sam': [94,77,90],
             'Katie': [100,81,82],
             'Bob': [83,65,85]}

print(grades_dict)

grades = pf.DataFrame(grades_dict)

print(grades)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

#print(grades['Eva'])

#print(grades.Sam)

#print(grades.loc['Test1'])

#print(grades.iloc[1])

'''Wally Eva Sam Katie Bob
Test1   87  100 94  100 83
Test2   96  87  77  81  65
Test3   70  90  90  82  85'''

#print(grades.loc['Test1':'Test3'])

#print(grades.iloc[0:2])

#print(grades.loc['Test1','Test3'])

#print(grades.iloc[0,2])

#view only Eva and Katie's grades for Test1 & Test2

print(grades.loc['Test1':'Test2', ['Eva', 'Katie']])

print(grades.iloc[0:1,[1,3]])

above_90 = grades[grades>90]

print(above_90)

b_grades = grades[(grades> 80 & (grades < 90)]

print(b_grades)

print(grades.at['Test2', 'Eva'])

print(grades.iat[1,2])

grades.at['Test2', 'Eva'] = 100

print(grades)

print(grades.describe())

pd.set_option('precision', 2)

print(grades.describe())

#grades = grades.T

print(grades.T.describe())

print(grades.T.mean())