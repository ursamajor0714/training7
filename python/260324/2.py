# # #정올 9206 완
# # #a,b=map(int,open(0).read().split())
# # #print(f"{a-10} + {b*2} = {(a-10)+(b*2)}")


# # #정올9245 완
# # #a,b=[int (input()) for _ in range(2)]
# # #c=input()
# # #d=eval(f"{a}{c}{b}")
# # #print("ans =",d)

# # #정올 9246 역대급 극악의 난이도...완
# # #a,b,c=map(int,input().split())
# # ##print((a if a>=c else c if b>=c else b)-(a if a<=c else c if b<=c else b))
# # #print((a if a>b else c if a>c else b c>b else c) - (a if a<b else c if a<c else b c<b else c))
# # #a if a>c else b if b>a else c if c>a else c
# # #8 2 4
# # #8> 4 -> 2 -> 2>8 -> 4 -> 4>8 -> 4
# # #a,b,c=map(int, input().split())
# # #print((a if a>c else c if c>b else b if b>c else c)-(a if a<c else c if c<b else b if b<c else c))
# # #a if a>c else c if c>b else b if b>c else c
# # #a if a>b and a>c else b if b>c else c
# # #(a if a>b and a>c else b if b>c else c)-(a if a<b and a<c else b if b<c else c)


# # #max=25
# # #weight=0
# # #item=3

# # #while weight + item <= max:
# # #    weight +=item
# # #    print('짐을 추가합니다')
# # #print(f'총 무게는 {weight}입니다')

# # #drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
# # #for x in drama :
# # #    if x == '시즌3':
# # #        print('재미 없대, 그만 보자')
# # #        break
# # #    print(f'{x} 시청')

# # #drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
# # #for x in drama :
# # #    if x == '시즌3':
# # #        print('재미 없대, 건너뛰자')
# # #        continue
# # #    print(f'{x} 시청')

# # #for x in range(10):
# # #    if x % 2 == 1:
# # #        continue
# # #    print(x)

# # #정올 9275 완
# # #a=int(input())
# # #i=0
# # #hap=0
# # #while i <= a :
# # #    hap += i
# # #    i+=1
# # #rint(hap)


# # #while True :
# # #    a = int(input())
# # #    if a==0:
# # #        break
# # #    print(f"N = {a}")

# # #products=['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
# # #recall=[]
# # #for p in products:
# # ###    if p.startswith('SIRO'):
# # #        recall.append(p)
# # #print(recall)

# # #def show_price(customer):
# # #    print(f'{customer} 고객님')
# # #    print('커트 가격은 1500원 입니다.')

# # #customer1 = '나장발'
# # #show_price(customer1)

# # #customer2 = '나수염'
# # #show_price(customer2)

# # #def b(a):
# # #    print("=========================")
# # #    print(f'{a} 함수를 호출하였습니다. ')
# # #    print(f'{a} 함수를 다시 호출합니다. ')
# # #    print("=========================")
# # #a = "line"
# # #b(a)

# # #def get_price():
# # #    return 15000
# # #price=get_price()
# # #print(f'커트 가격은 {price}원 입니다.')


# # #def get_price(is_vip):
# # #    if is_vip == True:
# # #        return 10000
# # #    else:
# # #        return 15000#

# # #price=get_price(True)
# # #print(f'커트 가격은 {price}원 입니다.')
# # #price=get_price(False)
# # #print(f'커트 가격은 {price}원 입니다.')



# # def a(is_vip=False):
# #     if is_vip == True:
# #         return 10000
# #     else:
# #         return 15000

# # a1=a(True)
# # print(a1)
# # a2=a()
# # print(a2)
# # a3=a()
# # print(a3)
# # a4=a()
# # print(a4)

# def visit(today, *customers):
#     print(today)
#     for customer in customers:
#         print(customer)

# visit('2026년 3월 27일','나장발')
# visit('2026년 3월 27일','나장발','나수염','나김리','홍길동')



a=int(input())

if a>=90 :
    print("A")
elif a>=80 :
    print("B")
elif a>=70 :
    print("C")
elif a>=60 :
    print("D")
else :
    print("F")


def a():
    if a>=90 : "A"
    elif a>=80 : "B"
    elif a>=70 : "C"
    elif a>=60 : "D"
    else : "F"



