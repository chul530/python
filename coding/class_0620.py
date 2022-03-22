su = 100

print('type(su):',type(su))
print('type(str(su)):',type(str(su)))
print('type(float(su)):',type(float(su)))
print()

su = 100
num = '100'
flt = "1.111"
print(su+int(num))
print(su+float(flt))
print(int(str(su)+num))
print()

print("숫자 입력")
num1 = input()
print("입력 받은 값:",num1)
# print()

print("이름 입력")
name = input()
print("나이 입력")
age = input()
print(name,"님의 나이는",age,"살 입니다")
print()

print("두 수의 합을 구해 줍니다")
print("두 수 입력")

num1 = input()
num2 = input()
num3 = int(num1) + int(num2)
print("두 수의 합", num1,"+",num2,'=',num3)
print(type(num1));print(type(num2));print(type(num3))
print()
#비효율적이다 매번 형변환을 실시해야함

num1 = int(input())
num2 = int(input())

result = num1 + num2
print(num1,"+",num2,"=",result)

result = num1 - num2 
print(num1,"-",num2,"=",result)

result = num1 * num2 
print(num1,"*",num2,"=",result)

result = num1 / num2 
print(num1,"/",num2,"=",result)
print()

print("문자열 입력")
name = input()
print("정수 입력")
age = int(input())
print("실수 입력")
flt = float(input())

print("name 값:",name,"\t type:",type(name))
print("age 값:",age,"\t type",type(age))
print("flt 값:",flt,"\t tpye:", type(flt))
print()

name = input("이름을 입력 하세요:")
age = int(input("나이를 입력 하세요:"))
addr = input("주소를 입력 하세요:")
print("이름:",name,"\n나이:",age,"\n주소:",addr)
print()

year = int(input("올해의 연도를 4자리로 입력하세요:"))
birth = int(input("당신이 태어난 년도를 4자리로 입력하세요:"))
print("당신의 나이는",year +1 - birth,"살 입니다.")
print()

first = float(input("첫번째 물건의 무게를 입력:"))
second = float(input("두번째 물건의 무게를 입력:"))
result = 600-first-second
print("현재 엘리베이터에 허용 무게는",result,"입니다")
print()

height = float(input("키를 입력:"))
standard = (height-100)*0.9
print("표준체중은",standard,"kg입니다")
print()

height = float(input("키 입력:"))
standard = (height - 100)*0.9
weight = float(input("몸무게 입력:"))
rate = weight/standard*100
print("표준체중은%.2fkg이고 비만도는%.2f%%입니다"%(standard,rate))
print()
#%를 쓰고 싶을땐 \가 같이 2번 써주면 된다.

name = input("이름:")
korean = int(input("국어:"))
english = int(input("영어:"))
math = int(input("수학:"))
sum_ = korean+english+math
average = sum_/3
print("====================학생 정보====================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print(name,"\t",korean,"\t",english,"\t",math,"\t",sum_,"\t",average)
# print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name,korean,english,math,sum_,average))
print()

# '/' 나누기, '//' 몫, '%' 나머지 '**' 제곱수

num1 = 9; num2 =2
print(num1, "+", num2, "=",num1 + num2)
print(num1, "-", num2, "=",num1 - num2)
print(num1, "*", num2, "=",num1 * num2)
print(num1, "/", num2, "=",num1 / num2)
print(num1, "//", num2, "=",num1 // num2)
print(num1, "%", num2, "=",num1 % num2)
print(num1, "**", num2, "=",num1 ** num2)
print()

# '==' 같다, '!=' 같지않다 결과 값이 true인지 false인지로 나온다

su1=3.1;su2=3

print("su>=su2:",(su1>=su2))
print("su<=su2:",(su1<=su2))
print("su==su2:",(su1==su2))
print("su!=su2:",(su1!=su2))
print()
print("su>=su2:%d"%(su1>=su2))
print("su<=su2:%d"%(su1<=su2))
print("su==su2:%d"%(su1==su2))
print("su!=su2:%d"%(su1!=su2))