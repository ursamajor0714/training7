a=input()
b = input()
sign=["+","-","*","/","//","%","**"]
i = 0;
while(i < len(sign)):
    hap=f"{a} {sign[i]} {b}"
    result=eval(hap)
    print(f"{hap} = {result})")
    i = i + 1