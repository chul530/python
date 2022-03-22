num = int(input("수 입력:"))
if num==1:
    print("1 입력")
else:
    print("1이 아닌 값 입력")
print()

arr = [1,2,3,4,5]
na=int(input("찾을 숫자 입력:"))
if na in arr:
    print("arr:",arr,"찾는 숫자가 존재 합니다:",na)
else:
    print("arr:",arr,"안에는 찾고자 하는 숫자가 없습니다:",na)
print('결과:',na in arr)
print()

# if A in B
# B 안에 A가 존재하면 참 존재하지 않으면 거짓
# if A not in B
# B안에 A가 존재하지 않으면 참 존재하면 거짓

st = "Hello Python Fun"
na = input("찾고자 하는 문자열 입력:")
if na in st:
    print("st:",st,"찾는문자열:",na,"존재한다")
else:
    print("st 안에는",na,"존재 하지 않습니다")
print()

old_id = input("저장할 ID입력:")
print("인증 프로그램입니다")
print("ID 와 PW를 입력하세요")
new_id = input("ID 입력:")
if old_id==new_id:
    print("인증 통과 했습니다")
else:
    print("인증 실패")
print()

num = int(input("수 입력:"))
if num %3 ==0:
    if num%2 ==0:
        print("num은 3의 배수면서 짝수 입니다")
print("다음문장 실행")
print()

if num %3 ==0 and num%2==0:
    print("num은 3의 배수면서 짝수 입니다")
print("다음문장 실행")

순서가 상관 있을 경우 중첩을 사용

num = int(input("수 입력:"))
if num > 0:
    if num%2==0:
        print("num은 양의 짝수 입니다")
    else:
        print("num은 양의 홀수 입니다")
else:
    print("num은 음수 입니다")
print("다음 문장 실행")
print()

gb = int(input("Gbyte:"))
type = int(input("1:byte,2:Kbyte,3:Mbyte"))
if type == 1:
    gb *= 1024**3
if type == 2:
    gb *= 1024**2
if type == 3:
    gb *= 1024
print(gb)

old_id = input("id:")
old_pw = input("pw:")
print("id를 입력하세요")
new_id = input("id:")
if old_id == new_id:
    print("pw를 입력하세요")
    new_pw = input("pw:")
    if old_pw == new_pw:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다")
else:
    print("등록되지 않은 아이디 입니다")
print()

num = int(input("수 입력:"))
if num > 100:
    print("100보다 큰 수 입력")
elif num > 50:
    print("50보다 큰 수 입력")
elif num > 0:
    print("0보다 큰 수 입력") 
else:
    print("그 외의 값 입력")
print()

#퀴즈
name = input("이름:")
id = input("학번:")
score1 = int(input("성적1:"))
score2 = int(input("성적2:"))
score3 = int(input("성적3:"))
sum = score1+score2+score3
avg = float(sum/3)
if avg>=90:
    print("A")
elif avg>=80:
    print("B")
elif avg>=70:
    print("C")
elif avg>=60:
    print("D")
else:
    print("F")
print()


coffee = int(input("커피 개수:"))
price1 = 2000
price2 = 1500
if coffee > 10:
    price = price1 * 10 + price2 * (coffee-10)
else:
    price = price1 * coffee
print(price)
print()

num = int(input("정수 입력:"))
if num == 0:
    print("0은 3의 배수도 4의 배수도 아닙니다.")    
elif num % 3 == 0 and num % 4 ==0:
    print(num,"는 3의 배수이면서 4의 배수입니다.")
elif num % 3 == 0:
    print(num,"는 3의 배수입니다.")
elif num % 4 == 0:
    print(num,"는 4의 배수입니다.")
else:
    print(num,"는 3의 배수도, 4의 배수도 아닙니다")
print()

time = int(input("시간:"))
overtime = (time-31)//10
overprice = 5000
if time <= 30:
    price = 30000
else:
    price = (overtime+1)*overprice+30000
print(price)