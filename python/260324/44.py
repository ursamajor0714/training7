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

# num1=10
# num2=5

# try:
#     result=num1/num2
#     print(f'연산 결과는 {result} 입니다')
# except ZeroDivisionError:
#     print('0으로 나눌수 없어요.')
# except TypeError:
#     print('값의 형태가 이상해요.')
# except Exception as  err:
#     print('에러가 발생했어요.',err)




# class P:
#     def __init__(self,A):
#         self.A = A
#     def OK(self):
#         if 60<=self.A:
#             print("PASS")
#         else:
#             print("FAIL")
# a = int(input())
# p=P(a)
# p.OK()

from ast import Pass




#나+재미나이
class Body:
    def __init__(self,hi,wei):
        self.name=name
        self.hi=float(hi)
        self.wei=float(wei)
    def __add__(self,other):
        return Body("plus",self.hi + other.hi, self.wei + other.wei)
    def __sub__(self,other):
        return Body("minus",self.hi - other.hi, self.wei - other.wei)
    def __truediv__(self,other):
          return Body("avg", (self.hi + other.hi) / 2, (self.wei + other.wei) / 2)
    def print(self):
        print(f"{Pass} 키 : {self.hi:.1}, 몸무게: {self.wei:.1}")

raw_me = input("당신의 키와 몸무게를 입력하세요.")
my_hi=my_wei = raw_me.split()


raw_me = input("당신의 키와 몸무게를 입력하세요.")
f_hi=f_wei = raw_me.split()

me1=Body(my_hi,my_wei)
fr1=Body(f_hi,f_wei)

results=[me1,
fr1,
me1+fr1,
me1-fr1,
me1/fr1]

for res in results:
    res.print_info()








#재미나이
class Body:
    def __init__(self, name, hi, wei):
        self.name = name
        self.hi = int(float(hi))
        self.wei = float(wei)

    def __add__(self, other):
        return Body("plus", self.hi + other.hi, self.wei + other.wei)

    def __sub__(self, other):
        return Body("minus", abs(self.hi - other.hi), abs(self.wei - other.wei))

    def __truediv__(self, other):
        return Body("avg", (self.hi + other.hi) // 2, (self.wei + other.wei) / 2)

    def __str__(self):
        return f"{self.name} 키: {self.hi}, 몸무게: {self.wei:.1f}"

line1 = input("당신의 키와 몸무게를 입력하세요.").split()
m_h = line1[-2].split('.')[-1]
m_w = line1[-1]
me = Body("my", m_h, m_w)

line2 = input("친구의 키와 몸무게를 입력하세요.").split()
f_h = line2[-2].split('.')[-1]
f_w = line2[-1]
fr = Body("friend", f_h, f_w)

results = [me, fr, me + fr, me - fr, me / fr]

for res in results:
    print(res)














