import pandas as pd 

grades = pd.Series([87,100,94])

print(grades)

same_grade = pd.series(98.6, range(3))

print(same_grade)

#0 98.6
#1 98.6
#2 98.6
#dtype: float64

print(grades[0])
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

print(grades.describe())

#you can specify custome indices with the index keyword argument:
grades = pd.series([87,100,94], indexes=['Wally','Eva', 'Sam'])

print(grades)

#if you initialize a series with a dictionary, its keys become
#the series' indices, and its values become the series' element values

grades = pd.series({'Wally': 87, 'Eva': 100, 'Sam': 94})

#you can access individual elements via square brackets containing a 
#custom index value
print(grades['Eva'])
#100

print(grades.Wally)

print(grades.dtype)

print(grades.values)

'''0 Hammer
   1 Saw
   2 Wrench'''