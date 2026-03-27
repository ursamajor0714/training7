#set1={'다다다', '가가가', '나나나'}
#print(set1)

#set2={2345234234, 23423452536,67567567567567,8978697689789}
#print(set2)

#set3={"1","2","3","4"}
#print(set3)

set4={"1",1,"2",2,"3",3}
print(set4)
set4.add("33") #추가 (1개만됨)
print(set4)
set4.remove("33") #삭제(1개만됨)
print(set4)
set4.clear() #비우기 (전체)
print(set4)
del set4 #세트삭제 (오류뜸)
print(set4)
#copy() 세트복사
#discard() 값삭제(값 없어도 오류X)
#isdisjoint() 겹치는지 여부 T or F
#issubset() 다른 세트의 부분집합인지
#sisuperset() 다른 세트의 상위집합인지 여부
#update() 여러 값 추가

#discard() 값삭제(값 없어도 오류X)
#isdisjoint() 겹치는지 여부 T or F
#issubset() 다른 세트의 부분집합인지
#sisuperset() 다른 세트의 상위집합인지 여부
#update() 여러 값 추가