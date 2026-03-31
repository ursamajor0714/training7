# a=int(input())
# for i in range(a):
#     b,c=map(int, input().split())
#     print(b+c)



# a,b =map(int, input().split())
# print(f"{float(a/b)}")

# a=int(input())

# for i in range(1,a+1):
#     b,c=map(int, input().split())
#     print(f"Case #{i}: {b} + {c} = {b+c}")

# a=int(input())

# for i in range(1,a+1):
#     b,c=map(int, input().split())
#     print(f"Case #{i}: {b+c}")



# while True:
#     a,b=map(int, input().split())
#     if a+b>0:
#         print(a+b)
#     else:
#         break

# import sys

# while True:
#     a = sys.stdin.readline()
#     if not a:
#         break
#     try:
#         b, c = map(int, a.split())
#         print(b + c)
#     except ValueError:
#         break


# a=int(input())
# hap=[]
# for i in range(1,a+1):
#     hap.append(i)

# hap1=sum(hap)
# print(hap1)


# a=int(input())
# Z=["long ","int"]
# print((a // 4) * Z[0] + Z[1])


# a=int(input())
# for i in range(1,a+1):
#     print(i*"*")


# a=int(input())
# for i in range(1,a+1):
#     print((i*"*").rjust(a))


# a=int(input())
# list1=list(map(int, input().split()))
# b=int(input())
# hap=[]
# for i in list1:
#     if i==b:
#         hap.append(i)
# print(len(hap))


# a=int(input())
# list1=list(map(int, input().split()))
# print(min(list1),max(list1))


# list1 = [int(input()) for _ in range(9)]

# print(max(list1))
# print(list1.index(max(list1)) + 1)

# class parent:
#     def method_a(self):
#         print("method_a()")

# class children(parent):
#     def method_b(self):
#         super().method_a()
#         print("method_b()")

# p1=parent()
# p1.method_a()

# p2=children()
# p2.method_a()
# p2.method_b()


# class BlackBox:
#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
# class TravelBlackBox(BlackBox):
#     def __init__(self,name,price,sd):
#         BlackBox.__init__(self, name, price)
#         self.sd=sd
#     def set_travel_mode(self,min):
#         print(str(min) + '분 동안 여행 모드 ON')


# class BlackBox:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class VideoMaker:
#     def make(self):
#         print('추억용 여행 영상 제작')

# class mailsander:
#     def send(self):
#         print('메일전송')

# class TravelBlackBox(BlackBox,VideoMaker,mailsander):
#     def __init__(self, name, price, sd):
#         super().__init__(name,price)
#         self.sd=sd
#     def set_travel_mode(self,min):
#         print(str(min) + '분 동안 여행 모드 ON')

# class AdvancedTravelBlackBox(TravelBlackBox):
#     def set_travel_mode(self, min):
#         print(str(min) + '분 동안 여행 모드 ON')
#         self.make()
#         self.send()

# b1 = TravelBlackBox('하양이',100000,64)
# b1.set_travel_mode(20)

# b2 = AdvancedTravelBlackBox('까망이',200000,128)
# b2.set_travel_mode(160)



class Z:
    def __init__(self,name,age):
        self.name=name
        self.age=int(age)
		
    def D(self) :
        if self.age>=18:
            print(f"{self.name}({self.age}) : adult")
        else:
            print(f"{self.name}({self.age}) : child")
			
C = []
for x in range(2):
    a,b=input().split()
    C.append(Z(a,b))
	
for p in C:
    p.D()
