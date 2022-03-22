rice = 100*1000
mice = 2
eat = 20
day = 1
while rice>0:
    rice -= mice*eat
    day +=1
    if rice == 0:
        break
    if day%10== 0:
        mice*=2
print("쥐 마리:"mice)
print("날짜:"day)

#다시 할것
money = int(input("요금을 투입하세요:"))
while money < 250:
    print(money)
    print("================커피 자판기================")
    print("1. 커피(200)\t2. 코코아(250)\t3. 반환\t4. 종료")
    opt = int(input("메뉴:"))
    if opt == 1:
        money-=200
    if opt == 2:
        print("금액부족")
    if money == 0:
        break
else:
    print(money)
    if money<200:
        print("금액부족")
    print("================커피 자판기================")
    print("1. 커피(200)\t2. 코코아(250)\t3. 반환\t4. 종료")
    opt = int(input("메뉴:"))
    if opt == 1:
        money-=200
    if opt == 2:
        money-=250
print("잔돈:",money)
print()

ls = [500,200,300,400];Sum=0

print("ls:",ls)
print("ls[0]:",ls[0])
print("ls[1]:",ls[1])
print("ls[2]:",ls[2])
print("ls[3]:",ls[3])
print()

ls = [0,0,0,0];Sum=0
ls[0]=int(input("첫번쨰 숫자 입력:"))
ls[1]=int(input("두번쨰 숫자 입력:"))
ls[2]=int(input("세번쨰 숫자 입력:"))
ls[3]=int(input("네번쨰 숫자 입력:"))

Sum = ls[0]+ls[1]+ls[2]+ls[3]

print("ls[0]:",ls[0])
print("ls[1]:",ls[1])
print("ls[2]:",ls[2])
print("ls[3]:",ls[3])

print("리스트의 합:%d"%Sum)
print()

ls = [0,0,0,0]; Sum = 0

print("len(ls):",len(ls))
for i in range(len(ls)):
    ls[i]=int(input(str(i)+"째 숫자 입력:"))
    Sum += ls[i]

for i in rannge(len(ls)):
    print("ls[%d]:"%i,ls[i])
print("리스트의 합:",Sum)
print()

ls = [10,20,30,40]
print("ls:",ls)

print("\nls[1:3]=>ls[1]~[2]:",ls[1:3])
print("ls[0:3]=>ls[0]~[2]:",ls[0:3])
print("ls[2:]=>ls[2]~[끝까지]:",ls[2:])
print("ls[:2]=>ls[0]~[1]:",ls[:2])
print()