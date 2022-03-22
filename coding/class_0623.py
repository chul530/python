su1 = su2 = 5
su1 += 1
print("su1+1=",su1)
su1-=1
print("su-1=",su1)
su1*=su2
print("su1*su2=",su1)
su1//=su2
print("su1//su2=",su1)
su1%=su2
print("su1%su2=",su1)
print()

su1 = 5
su2 =3
su1**=su2
su1-=2
print("su1/4=",su1/4)
print("su1//4=",su1//4)
print("su1%4=",su1%4)
print()

print(0 or 0,":",False or False)
print(1 or 0,":",True or False)
print(0 or 1,":",False or True)
print(1 or 1,":",True or True)

print("not:",not(0 or 0),":",not(False or False))
print("not:",not(1 or 1),":",not (True or True))
print()

a = 20
b = 10
print(False or (a+b))
print(True or (a+b))
print(False and (a+b))
print(True and (a+b))
print()

# 비트 연산자
# | a와 b를 bit로 벼환하여 OR 연산
# & a와 b를 bit로 변환하여 AND 연산
# ^ a와 b를 bit로 변환하여 XOR 연산
# ~ a를 bit로 변환하여 NOT 연산 (양수에서 음수로 가면 -1, 음수에서 양수로 가면 +1)
# >> a를 bit로 변환하여 오른쪽으로 Shift
# << a를 bit로 변환하여 왼쪽으로 Shift

num1 = 3
num2 = 5
result = num1 | num2
print(result)
print()

num1 = 10
num2 = 5
if num1>num2:
     print("num1 이 num2 보다 크다")
print()

num1 = int(input("수 입력:"))
if num1 % 2  ==0:
    print("num1 : ",num1,"짝수다")
print("나는 다음 문장")

num1 = int(input("수 입력:"))
if num1%2 == 0:
    print("num1:",num1,"짝수다")
    print("num1:",num1,"2의 배수이다")
print("나는 다음 문장")
print()

print("1.easy game")
print("2.hard game")
print("3.exit")
num1 = int(input("선택:"))
if num1 == 1:
    print("easy game start")
if num1 == 2:
    print("hard game start")
if num3 == 3:
    print("game exit")
print()

num1 = int(input("날짜:"))
if num1 % 7 ==1:
    print("월요일")
if num1 % 7 ==2:
    print("화요일")
if num1 % 7 ==3:
    print("수요일")
if num1 % 7 ==4:
    print("목요일")
if num1 % 7 ==5:
    print("금요일")
if num1 % 7 ==6:
    print("토요일")
if num1 % 7 ==0:
    print("일요일")
print()

# 퀴즈
num = int(input("숫자:"))
if num % 3 == 0:
    print(num)
print()

num = int(input("숫자:"))
if num >= 0:
    print(num)
if num < 0:
    print(-1*num)
print()

num = int(input("숫자:"))
if num % 2 == 0:
    print("짝수")
if num % 2 == 1:
    print("홀수")
print()

num1 = int(input("숫자 1:"))
num2 = int(input("숫자 2:"))
if num1>=num2:
    print(num1)
if num1<num2:
    print(num2)
print()

num1 = int(input("숫자 1:"))
num2 = int(input("숫자 2:"))
num3 = int(input("숫자 3:"))
if num1 > num2 and num1 > nu3:
    print(num1)
if num2 > num1 and num2 > num3:
    print(num2)
if num3 > num1 and num3 > num2:
    print(num3)
print()

num1 = int(input("숫자 1:"))
num2 = int(input("숫자 2:"))
if num1 > num2 and num1 % 2 ==0:
    print(num1)
if num2 > num1 and num2 % 2 ==0:
    print(num2)
print()

num1 = int(input("숫자 1:"))
num2 = int(input("숫자 2:"))
if (num1 + num2) % 2==0 and (num1 + num2)%3==0:
    print(num1+num2)
print()