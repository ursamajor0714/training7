#a=int(input())
#if a > 10 :
#    print("Big")

#a=int(input())
#print(a)
#if a < 0:
#    print("MINUS")

#a,b = [int(input())for _ in range(2)]
#print(a+b)
#if (a%2==1) or (b%2==1) :
#    print("ODD")



#a,b=map(int, input().split())
#if (a>b):
#    a,b=b,a
#    print(a)
#    print(b)
#else:
#    print(a)
#    print(b)

#a,b=map(int, input().split())
#A=a
#B=b
#if a>b:
#    print(A)
#elif b>a :
#    print(B)

#a=int(input())
#if a >=60 :
#    print("PASS")
#else:
#    print("FAIL")

#a=int(input())
#if a >= 13:
#    print("Middle School")
#else:
#    print("Elementary School")


#yellow_card=2
#foul=True
#if foul:
#    yellow_card+=1
#    if yellow_card==2:
#        print('경고 누적 퇴장')
#    else:
#        print('휴..조심해야지')
#else:
#    print('주의')

#for a in range (10):
#    print(f"팔 벌려 뛰기 {a*2}")

#range(이상,미만,범위)
#range(1,10,2)
#1,3,5,7,9

#for n in range(1, 31, 10):
#    print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')

#my_list = (1, 2, 3, 4, 5, 6)
#for x in my_list:
#    print(x)

#for x in range(2,3,1):
#    for y in range(1,10,1):
#        print(f"{x} * {y} = {x*y}")

#N=int(input())
#for i in range(9) :
#    print(f"{N} * {i+1} = {N*(i+1)}")

#N = int(input())
#for i in range(1, 10):
#    print(f"{N} * {i} = {N * i}")

#person={'이름':'나귀욤', '나이':7, '키':120,'몸무게':23}
#for v in person.values(): # 값만
#    print(v)
#for k in person.keys(): #목록만
#    print(k)
#for k, v in person.items(): #두개다
#    print(k, v)

#for x in range(1,101):
#    print(x, end=" ")


#print(" ".join(str(x) for x in range(1, 101)))
#print(" ".join(f"{x}" for x in range(1, 101)))

#print(x, for x in range(3, 301))

#print(*range(5,2001,5))

#for x in range(2,51,2):
#    print(x)

#9261 정올 문제 완
#N=int(input())
#print(*range(1,N+1))

#2741 백준 문제 완
#N=int(input())
#for x in range(1,N+1,1):
#    print(x)

#2742 백준 문제 완
#N=int(input())
#for x in range(N,0,-1):
#    print(x)

#9263 정올 문제 완
#N=int(input())
#for x in range(5, N+1):
#    print(x)

#9264 정올 문제 완
#N=int(input())
#for x in range(2,N+1,2):
#    print(x, end=" ")

#9265 정올 문제 완
#N=int(input())
#print(" ".join(f"{x}" for x in range(-10,N+1,1)))

#9266 정올 문제 완
#N=int(input())
#for x in range (10,N+1,10):
#    print(x)

#9267 정올 문제 완
#N=int(input())
#for x in range(N,0,-1):
#    print(x, end=" ")

#9268 정올 문제 완
#N=int(input())
#for x in range(N,4,-1):
#    print(x)

#9669 정올 문제 완
#N=int(input())
#for x in range(N,0,-3):
#    print(x,end=" ")

#S,E=map(int, input().split())
#for x in range(S,E+1,2):
#    print(x)

#S,E=[int(input()) for _ in range(2)]
#for x in range(S,E-1,-1):
#    print(x,end=" ")

x=1
y=0
while x <11:
    y+=x
    x +=1
print(y)

