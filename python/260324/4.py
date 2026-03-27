list1=list(map(int, input().split()))
sum1=sum(list1)
len1=int(len(list1))
ever=int(sum1/len1)
print(f"sum = {sum1}")
print(f"avg = {ever}")



list1 = list(map(int, input().split()))

print(f"sum = {sum(list1)}")
print(f"avg = {sum(list1) // len(list1)}")