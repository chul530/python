# for과 while의 특징
# for은 이미 몇번 반복 되는지 정해져있지만, while은 정해져있지 않다
# while은 특정 조건에 맞는다면 반복이 끝이난다 (if와 for가 합쳐져있는 느낌...?)

i=0
while i<5:
    print(i,"종속 문장")
    i+=1
print()

for i in range(0,5):
    print(i)
print()

i=1
odd,even=0,0
while i<=10:
    if i%2==0:
        even+=i
    else:
        odd+=i
    i+=1
print("1-10 짝수의 합:",even)
print("1-10 홀수의 합:",odd)

odd,even=0,0
for i in range(1,11):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even)
print(odd)
print()

i=0
while i<5:
    print(i,"종속 문장")
    i+=1
else:
    print("조건식이 거짓일 경우:",i)
print()

i=1
while True:
    print(i,"종속 문장",end=" ")
    i+=1

i=1
flag = True
while flag:
    print(i,"종속 문장")
    if i ==10:
        flag = False
    i+=1
print()

i=0
while True:
    if i ==3:
        break
        print("3출력")
    print(i,"출력")
    i+=1
print()

i=0
while i<5:
    i+=1
    if i==3:
        continue
        print("3출력")
    print(i,"출력")
print()

for i in range(1,6):
    if i==3:
        continue
    else:
        print(i,"출력")

num,result,i=0,0,1
while True:
    num = int(input("1~10사이의 숫자 입력:"))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    break
else:
    print("next...") # next가 안나오는 bug
while i<=num:
    result+=i;i+=1
else:
    print("1~",num,"까지의 합:",result)
print()

while flag:
    num = int(input("1~10사이의 숫자 입력:"))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    else:
        flag=False
else:
    print("next...")
while i<=num:
    result+=i;i+=1
else:
    print("1~",num,"까지의 합:",result)
print()

i,sum =1,0
num = int(input("10~20사이의 숫자 입력:"))
while True:
    if num<=11 or num>20:
        print("잘못 입력 다시")
        continue
    break
while i<=num:
    sum+=i
    i+=1
else:
    print("10~",num,"까지의 합:",sum)
print()

for i in range(0,3,1):
    for k in range(0,5,1):
        if k==3:
            break
        print("(i:%d\tk:%d)"%(i,k))
print()

i = 0
while i<3:
    k= 0
    while k<5:
        if k==3:
            break
        print("(i:%d\tk:%d)"%(i,k))
        k+=1
    i+=1
print()