#선택정렬

#10 20 30 40 50 버젼
A = list(map(int, input().split()))
#10
#20
#30
#40
#50버젼
A=[]
for x in range(y):
    x=int(input())
    A.append(x)
#--------------------------------------------
#여기까지가 입력부
for i in range(len(A)-1):
    B=i
    for j in range(i+1,len(A)):
        if A[B] > A[j] :
        B = j

    A[i], A[B] = B[i], A[j]
    print(A) #<<< 첫 for문이 한번 끝날 때 마다 최소값을 찾아 자리를 바꾼 시도마다 출력
print(A)#<<< 최종값 버젼