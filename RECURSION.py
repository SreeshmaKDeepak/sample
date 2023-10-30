# k=10
# def try_function(k) :

#     if ( k > 0 ): 

#         result = k+try_function(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("\n\n Recursion Example Results")

# try_function(6)

## FACTORIAL  USING RECURSION


# def fact(limit) :
#     if(limit > 0) :
#         value = limit * fact(limit - 1)
#         #print(value)                   ##  PRINT ALL VALUES RESULTS IN THE LOOP
#     else :
#         value = 1
#     return value

# result = fact(5)
# print(result)

# k="caption"
# limit=len(k)
# print(k[limit-1])
   
a=input("enter the word")
b=input("enter the word")
c=len(a)
d=len(b)
if c==d:
    for i in a:
        for j in b:
            a[i]==b[j]
    print("anagram")
else:
    print("not anagram")