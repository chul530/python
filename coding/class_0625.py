# for 변수 in range(초기값,끝값,증감값):
#     print("종속문장")
for i in range(1, 11, 1): # 보통 반복의 횟수를 결정
    print(i)
print()

for i in range(0,3,1):
    print("i:",i,"for 문 이해하기^^")
print()

for i in range(1,11,1):
    if i%2==0:
        print("i=",i,":값 확인")
print()

for i in range(0,11,2):
    print("i=",i,":값 확인")
print()

for i in range(10,-1,-1):
    print(i,":10~0까지 출력")

sum=0
for i in range(1,11,1):
    sum+=i
print(sum)
print()

for i in range(1,11,1):
    print(i,end=" ")  
# end를 사용해 뒤에 자동으로 오는 \n 대신 다른것을 넣을수 있다(단, 빈칸혹은 문자열만 가능)
print()

for i in range(1,31,1):
    if i%5==0:
        print(i)
    else:
        print(i,end="\t")
print

sum=0
num= int(input("값 입력:"))
for i in range(1,num+1,1):
    sum = sum +i
print("1에서 %d까지 합:%d"%(num,sum))
print()

sum = 0
start = int(input("시작값 입력:"))
en = int(input("끝값 입력:"))
grow  = int(input("증가값 입력:"))

for i in range (start,en+1,grow):
    sum= sum+i

print("%d에서 %d까지 %d씩 증가한 값의 합:%d"%(start,en,grow,sum))
print()

for i in range(0,10):
    print(i)
print()

for i in range(10):
    print(i)
print()

for i in range(10,2):
    print(i)
print()

for i in range(0,10,2):
    print(i)
print()

# 퀴즈
start=int(input("시작값:"))
end=int(input("끝 값:"))
increase=int(input("증가 값:"))
for i in range(start,end+1,increase):
    if i%7==0:
        print(i,end=" ")
print()

sum = 0
for i in range(1,101,1):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)
print()

num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자:"))
sum = 0
if num1>num2:
    for i in range(num1,num2-1,-1):
        sum+=i
else:
    for i in range(num1,num2+1):
        sum+=i
print(sum)
print()

day = int(input("날짜:"))
money = 10
sum = money
for i in range(0,day-1,1):
    money*=2
    sum+=money
print(money)
print(sum)
print()

# money = 10
# save = 10
# for day in range(2,31):
#     money*=2
#     save+=money
# print("마지막 입금액: %d원\n마지막 총 저축금액: %d원"%(money,save))