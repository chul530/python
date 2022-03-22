ls_1 = []
ls_2 = []
value = 1
for i in range(3):
    for j in range(4):
        ls_1.append(value)
        value+=1
    ls_2.append(ls_1)
    ls_1=[]
for i in ls_2:
    for j in i:
        print(j,end='\t')
    print()
print()
print(ls_2)
print()

be = ['2019','12','31']
print(be)
print()

af=list(map(int,be))
print(af)
print()

tp=(10,20,30)
print("tp:",tp)
print("tp type:",type(tp))
print("tp len:",len(tp))
print()

tp1=10,20,30
print("tp1:",tp1)
print("tp type:",type(tp1))

print("tp1[0]type:",type(tp1[0]))
tp1[0]=100 #에러발생
print()

tpType = "문자열",100,1.111

print("tpType:",tpType)
print("type:",type(tpType))
print("tpType[0]:",type,(tpType[0]))
print("tpType[1]:",type,(tpType[1]))
print("tpType[2]:",type,(tpType[2]))
print()

tpInt=(10)
print("tpInt:",type(tpInt));#<class'int'>

tpT1=(10)
print("tpT1:",type(tpT1));#<class'tuple'>

tpT2=(10)
print("tpT2:",type(tpT2));#<class'tuple'>
print()

tt1 =(10,20,30,40)
tt2 =tt1[0]+tt1[1]+tt1[2]+tt1[3]
print("튜플 합:%d"%tt2)

print("tt1[1:3]:",tt1[1:3])
print("tt1[1:]:",tt1[1:])
print("tt1[:3]:",tt1[:3])

a=1,2,3
b=4,5,6
c=a+b
print("a:",a)
print("b:",b)
print("c:",c)

## *****
pack=1,2,"패킹"
print("packing\npack:",pack)

a,b,c = pack
print("unpacking\na:",a,"b:",b,"c",c)
print()

tp =100,200,"함수",100,'개수'

print("tp안의 200의 위치:",tp.index(200),"번째 인덱스")
print("tp안의 100의 개수:",tp.count(100,"개"))
print()

tp = ("회사정보","제품명",'가격정보','출시일')
ls = ('삼성전자','갤럭시','100원','미정')
for i in range(len(ls)):
    print(tp[i],':\t',ls[i])
print()

student={'학번':1234,'이름':'홍길동','학과':'it학과'}
print(student)

mobile = {'품명':'갤럭시','가격':100,'크기':10}
print(mobile)
print()

impo={}
impo['파이썬']="www.python.org"
impo['네이버']="www.naver.com"
impo['구글']="www.google.com"

print("파이썬:",impo['파이썬'])
print("네이버:",impo['네이버'])
print("구글:",impo['구글'])
print()

impo = {}
name = input('키 값 입력:')
val = input('값 입력:')
impo[name]=val

print(name,":",impo[name])
print(impo)

overwatch={}
for i in range(5):
    name = input('이름 입력:')
    skill = input('값 입력:')
    overwatch[name]=skill
print(overwatch)
print()

import collections
#순서있는 사전
overWatch = collections.OrderedDict()
i=0;name="";val=""
for i in range(5):
    name = input("이름 입력:")
    val = input("값 입력:")
    overWatch[name]=val
print(overWatch)