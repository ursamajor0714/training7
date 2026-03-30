# class BlackBox:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def set_travel_mode(self,min):
#         print(f'{self.name}{min}분 동안 여행 모드 ON')

# b1=BlackBox('까망이',200000)
# b2=BlackBox('하양이',100000)
# BlackBox.set_travel_mode(b1,20)


class Z:
    def __init__(self,name,age):
        self.name=name
        self.age=int(age)

    def check_age(self) :
        if self.age>=18:
            print(f"{self.name}{(self.age)} : child")
        else:
            print(f"{self.name}{(self.age)} : adult")
for i in range(2):
    n,a=input().split()
C=Z(n,a)
D.append(C)
for p in C:
    p.check_ahe()