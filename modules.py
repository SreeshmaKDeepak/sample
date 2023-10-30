##   REDUCE

# import functools         ## WAY OF IMPORTING A MODULE

# i = [5 , 8 , 10 , 20 , 50 , 100]
# sum = functools.reduce((lambda value1 , value2 : value1 + value2) , i)
# print(sum)

# from functools import reduce     ## ANOTHER WAY OF IMPORTING A MODULE
# i = [5 , 8 , 10 , 20 , 50 , 100]
# sum = reduce((lambda value1 , value2 : value1 + value2) , i)
# print(sum)


###             STATISTICS MODULE

#import statistics

# A = [100 , 23 , 120 , 90 , 11 , 124 , 230 , 9 , 12]
# B = statistics.mean(A)
# print("THE MEAN OF GIVEN VALUES IS " , B)
# C=statistics.median(A)                                           ###  MEDIAN
# print("THE MEDIAN O FGIVEN VALUES IS " , C)

# A = [100 , 2, 9 , 9 , 120]
# B = statistics.mode(A)                                           ###  MODE
# print("THE MODE OF GIVEN LIST IS " , B)

# Radius = float(input("ENTER THE VALUE OF RADIUS = "))
# import math
# pi_val = math.pi
# pow_val = math.pow(Radius,2)
# Area = pi_val * pow_val
# print("THE AREA OF CIRCLE IS = " , Area)

# import statistics
# A = [1,7,13,24,35,37,42,44,53,55]
#A=[1 ,22,34,55,67,120,25,58,125,256]
# B = statistics.median_low(A)                                   ###  LOW MEDIAN
# print("THE LOWEST MEDIAN OF GIVEN ELEMENTS ARE = " , B)
# C = statistics.median_high(A)                                  ###  HIGH MEDIAN
# print("THE HIGHEST MEDIAN AMONG GIVEN ELEMENTS ARE = " , C)

# A = [5,10,6,21,13,17,14,8,3,9]
# Variance = statistics.variance(A)                             ###  VARIANCE
# print("THE VARIANCE IS = " , Variance)
# B = statistics.stdev(A)                                       ###   STANDARD DEVIATION
# print("STANDARD VARIANCE IS = " , B)

###             MATH MODULE


import math

#Value = int(input("ENTER THE VALUE = "))
# sqroot = math.sqrt(Value)                                     ###  SQUARE ROOT
# print(sqroot)

# absolute_value = math.fabs(Value)
# print(absolute_value)                                         ###  ABSOLUTE VALUE

# round_value = math.ceil(Value)                                ###  CEIL
# print(round_value)

#print("the floor of",Value,"is",math.floor(Value))              ### FLOOR

#print("THE FACTORIAL OF " , Value , "IS " , math.factorial(Value))         ### FACTORIAL
#print("EXPONENTIAL VALUE OF " , Value , "=" , math.exp(Value))              ###  EXPONENTIAL
#X = 2
#print("log of " , Value , "IS" , math.log(Value))
#print("log of " , Value , "IS" , math.log(Value,X))                 ###  LOGARITHM
#print("e Value is " , math.e)
#print("RADIAN OF 90 DEGREES " , math.radians(Value))            ###  RADIANS
#print("DEGREES OF pi/2  = " , math.degrees(math.pi/2))          ###  DEGREES

            ###  RANDOM MODULE

import random

# Result = random.randint(1,11)
# print("RANDOM INTEGER IN BETWEEN [1,11] IS " , Result)          ### RETURNS A RANDOM INTEGER BETWEEN THE GIVEN RANGE OF VALUES
X = list(range(1,11))
random.shuffle(X)
print("SHUFFLED LIST IS " , X)