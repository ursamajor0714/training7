class Chi:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def Q (self):
        return self.a+self.b

    def W (self):
        return abs(self.a-self.b)

    def E (self):
        print(f"두 수의 합 = {self.Q()}")
        print(f"두 수의 차 = {self.W()}")

hap,cha=map(int, input().split())

ZIP=[hap,cha]

p=Chi(hap,cha)

p.E()