# 윈도우 10 ctrl+alt+방향키로 여러 행 한번에 작성가능

print("저의 이름은 최연철입니다") # 1순위 error 확률 낮음
print("저의 나이는 24살입니다")
print("주소는 서울입니다")

print("저의 이름은 최연철입니다\n" # 2순위
      "저의 나이는 24살입니다\n"
      "주소는 서울입니다.")

print("저의 이름은 최연철입니다.\n저의 나이는 24살입니다.\n주소는 서울입니다") # 3순위
print()
# 숫자 영어는 1byte로 각 1칸 사용 한글은 2byte로 2칸 사용
print("123456781234567812345678123456781234567812345678")
print("대한민국\t"
      "만세\t"
      "대한독립만세\t"
      "만만세")
print("Have\t"
      "a\t"
      "Good\t"
      "Time.");
print("1234567\t"
      "1\t"
      "12345678\t"
      "123");
print()

# 따옴표를 그래도 사용하고 싶으면 \을 쓰거나 서로 다른 2개를 각각 사용
print("쌍 따옴표\"")
print("홑 따옴표'")
print('쌍 따옴표"')
print('홑 따옴표\'')
print()
# escape 문자(\)는 따로 떨어져있으면 작동 안함. 정해진 문자나 숫자와 함께 써야함
print('표현 \ 방식')
print('표현 \2 방식')
print('표현 \\2 방식')
# print('표현 방식\') # error code
print('표현 방식\\')
print()

print("=====================\n"
      "        /)/)         \n"
      "       (  ..)        \n"
      "       (  >♡        \n"
      "  Have a Good Time.  \n"
      "=====================")
print()

print("\t####회비 정보####\n"
      "========================================\n"
      "이름\t나이\t전화번호\t회비\n"
      "========================================\n"
      "홍길동\t\"15\"\t010-123-1234\t\\20,000\n"
      "임꺽정\t\"20\"\t010-234-2345\t\\30,000\n"
      "김말이\t\"28\"\t010-345-3456\t\\50,000\n"
      "----------------------------------------\n"
      "총합계\t\t\t\t\\100,000\n"
      "========================================")
print()

# ""안은 문자열로 취급, 연산되서 나오지 않는다
print(123+123)
print(542-242)
print(2*123)
print(120/3)
print()

# 숫자는 띄어쓰기 사용금지, 데이터와 데이터는(문자+문자,문자+숫자,숫자+숫자) , 로 나눠야한다
print("덧셈 결과:",123+123)
print("뺄셈 결과:",542-242)
print("곱셈 결과:",2*123)
print("나눗셈 결과:",120/3)
print()

print("12+54=",12+54,"입니다\n"
      "268-42=",268-42,"입니다\n"
      "2*23=",2*23,"입니다\n"
      "120/3=",120/3,"입니다")
print()

print(0b01111011) # 2진법
print(0o173) # 8진법
print(0x7b) # 16진법
print(123)
print()

print("2진수:",bin(0b01111011))
print("8진수:",oct(0b01111011))
print("16진수:",hex(0b01111011))
print("10진수:",0b01111011)