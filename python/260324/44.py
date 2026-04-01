# n=int(input())
# width = 2 * n - 1
# for i in range(1,width+1,2):
#     print(("*"*i).center(width))

# print("It""'""s an apple.")
# print('He said ' '"Hello!"'' to me')


# A=["apple" , "orange" , "banana"]
# B='   "Hello world!"   '
# print(*A[::-1])
# print(B.replace('"', ""))
# print(B.replace('"', "").strip())


# A,B=input().split()
# print(f"{B} {A+B}")

# class S:
#     def __init__(self,name,high):
#         self.name=name
#         self.high=high
#     def __sub__(self,high):
#         return self.high - high
#     def re(self,other):
#         result = self.high - other.high
#         print(f"{self.name}'s age - {other.name}'s age = {result} ")

# ZIP=[]

# for i in range(2):
#     name,high=input().split()
#     ZIP.append(S(name,int(high)))
#     p=S(name,int(high))
# p1=ZIP[0]
# p2=ZIP[1]

# p1.re(p2)


# class Soccer:
#     def __init__(self,T,W):
#         self.T=T
#         self.W=W
#     def WIN_TEAM(self,i):
#         if i.win >= self.W :
#             return i.team
#         return None

# T,W=map(int, input().split())
# info=Soccer(T,W)

# teams=[]

# for _ in range(info.T):
#     t_name,t_win=input().split()
#     teams.append(Soccer(t_name,int(t_win)))

# for i in range(info.T -1,-1,-1):
#     result = info.WIN_TEAM(teams[i])
#     if result:
#         print(result)

# def f(a,b,c,x):
#     result = (a*(x**2)) + (b*x) + c
#     return result

# abc_input = list(map(int, input().split()))
# a, b, c = abc_input[0], abc_input[1], abc_input[2]

# list2=[2,3,5]

# for x in list2:
#     result = f(a, b, c, x)
#     print(result)



try:
    result=num1/num2
    print(f'연산 결과는 {result} 입니다')
except Exception as  err:
    print('에러가 발생했어요.')
except TypeError:
    print()
except ZeroDivisionError:
    print()
























