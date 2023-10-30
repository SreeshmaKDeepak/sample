# class Sum:
    
#     def __init__(self,A):
        
#         self.A=A
#     def getlist(self):
#         Result=int(input("Enter the number "))
#         return Result

#     def Addition(self,Result):
#         Length=len(self.A)
#         for i in range(Length-1):
#             if(self.A[i]+self.A[Length-1]==Result):
#                 print(i," ",Length-1)
# A=[10,11,20,40,60,80]
# obj=Sum(A)
# Result=obj.getlist()
# obj.Addition(Result)

# ###    USING LOCAL VARIABLE
# class Alphabet:
#     def __init__(self):
#         pass
#     def get_string(self):
#         input_string=str(input("Enter the string "))
#         return input_string
#     def print_string(self,upper_case1):
#          upper_case1=input_string.upper()
#          print("The new string is ",upper_case1)
# obj=Alphabet()
# input_string=obj.get_string()
# obj.print_string(input_string)

#  ###  USING GLOBAL VARIABLE       
# class Alphabet:
#     def __init__(self):
#         self.str=" "
#     def get_string(self):
#         self.str=str(input("Enter the string "))
        
#     def print_string(self):
#          upper_case1=self.str.upper()
#          print("The new string is ",upper_case1)
# obj=Alphabet()
# obj.get_string()
# obj.print_string()

# def addition(Num):
#     if Num>0:
#         Result=Num+addition(Num-1)
#         print(Result)
#     else:
#         Result=0
#     return Result
# addition(10)

# input_String=str(input("Enter the sentence "))
# lower_case=input_String.lower()
# Alphabet="abcdefghijklmnopqrstuvwxyz"
# for i in Alphabet:
#     if i  in lower_case:
#         flag=1
#     else:
#         flag=0
# if flag==1:
#     print("The given sentence is pangram")
# else:
#     print("The given sentence is not pangram")

# def unique(A):
#     set_conv=set(A)
#     list_conv=list(set_conv)
#     print("The unique numbers are ",list_conv)
# unique([12,45,12,45,89,10,125,11])

# def unique(True_List):
#     New_List=[]
#     for Num in True_List:
#         if Num not in New_List:
#             New_List.append(Num)
#     for Num in New_List:
#         print(Num,end=("  "))
# True_List=[12,45,12,45,89,0,34,23]
# print("The unique numbers from given list are ")
# unique(True_List)

#### ANAGRAM SEQUENCE
# Word_1=str(input("ENTER THE FIRST WORD "))
# Word_2=str(input("ENTER THE SECOND WORD "))
# Length_1=len(Word_1)
# Length_2=len(Word_2)
# if Length_1==Length_2 and sorted(Word_1)==sorted(Word_2):
#     print("GIVEN WORDS ARE ANAGRAMS")
# else:
#     print("GIVEN WORDS ARE NOT ANAGRAMS")

# Num=int(input("ENTER THE NUMBER "))
#for i in Num:
   # for j in Num:
# if Num[0] % 10 == Num[1]:
#             print("THE GIVEN NUMBER IS UNIQUE")
# else:
#             print("THE GIVEN NUMBER IS NOT UNIQUE")
# A=Num%10
# B=Num//10
# C=B%10
# D=B//10
# print(A,C,D)
# A=Num%10
# B=Num//10
# print(A,B)
#### CHECK NUMBER UNIQUE OR NOT FOR TWO DIGIT NUMBERS
# Num=int(input("ENTER THE NUMBER "))

# if Num % 10 == Num // 10:
#     print("THE GIVEN NUMBER IS UNIQUE")
# else:
#     print("GIVEN NUMBER IS NOT UNIQUE")
#### CHECKING WHETHER GIVEN NUMBER IS PALINDROME OR NOT
# Num = int(input("ENTER THE NUMBER = "))
# Reverse_Num = 0
# Temp = Num
# while Temp != 0 :
#     New_Digit = Temp % 10
#     Reverse_Num = Reverse_Num * 10 + New_Digit
#     Temp = Temp // 10
# if Num == Reverse_Num :
#     print("THE GIVEN NUMBER " , Num , "IS PALINDROME")
# else :
#     print("THE GIVEN NUMBER " , Num , "IS NOT PALINDROME")

# Limit=6
# for i in range(1,Limit+1):
#     for j in range(Limit-i):
#         print(i,end=(" "))
#     print()
Input=('A','B','C','D')
Length=len(Input)
# for i in range(Length):
#     for j in range(Length):
#         # print(Input[i][j],end=(" "))
#         if j==Length-1 :
#             print('A')
#     print()
