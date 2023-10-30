#   REVERSE

# def reverse(k) :
#     Limit = len(k)

#     if (Limit == 0) :
#         return k
#     else :
#         for i in range(Limit) :
#             values=k[(Limit-i) - 1]
#             print(values , end=(""))

# reverse("caption")

##  FIBONACCI

# def fibonacci(k) :
#     a=0
#     b=1
    
#     for i in range(k) :
#         if i==0 :
#             print(a)
#         elif i==1 :
#             print(b)
#         else :
#             temp=b
#             b=a+b
#             print(b)
#             a=temp


# fibonacci(6)

## LONGEST WORD

# def longest(A) :
#     temp1 = len(A[0])
#     temp2 = A[0]

#     for i in (A) :
#         if (len(i) > temp1) :
#             temp1 = len(i)
#             temp2 = i

    #print("THE LONGEST WORD IN GIVEN LIST IS " , temp2)
A = ["CAT" , "COMPUTER" , "CAPTION" , "AMINITY" , "PARENTHESIS"]
#longest(A)

