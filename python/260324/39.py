# a=int(input())
# b=int(input())
# for i in range(b,a+1):
#     if (i**0.5) == int(i**0.5):
#         print(i)

# a,b=map(int, input().split())

# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# else:
#     print("==")


a=int(input())
b=int(input())

if (a>0) and (b>0):
    print(1)
elif (a<0) and (b>5):
    print(2)
elif (a<0) and (b<0):
    print(3)
else:
    print(4)