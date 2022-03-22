ls = [10,20,30,40]
arr = ls

arr[2]=20000

print("ls:{}ls,id:{}".format(ls,id(ls)))
print("arr:{}arr,id:{}".format(arr,id(arr)))
print()

ls = [10,20,30,40]
arr = ls[:]

arr[2] =20000

print("ls:{}ls,id:{}".format(ls,id(ls)))
print("arr:{}arr,id:{}".format(arr,id(arr)))
print()

import copy
ls = [10,20,30,40]
#arr=ls[:]
arr = copy.deepcopy(ls)
arr[2]='deepcopy'

print("ls:{}ls,id:{}".format(ls,id(ls)))
print("arr:{}arr,id:{}".format(arr,id(arr)))
print()

ls = [10,20,30]
arr = [40,50,60]

print("ls:",ls)
print("arr:",arr)

Str=ls+arr
print("ls+arr=>Str:",Str)

string = ls*3
print("ls*3=>string:",string)
print()

Str=[0,0,0]
for i in range(len(ls)):
    Str[i]=ls[i]+arr[i]
print(Str)

string=[0,0,0]
for i in range(0,3):
    string[i]=ls[i]*3
print(string)
print()

ls = [4,8,2,7,6]
for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            ls[i],ls[j]=ls[j],ls[i]
print(ls)
print()

score = [82,85,76,79,96]
rank = [1,1,1,1,1]
for i in range(len(score)):
    for j in range(len(score)):
        if score[i]<score[j]:
            rank[i]+=1
print(score)
print(rank)
print()
for k in range(len(score)):
    print("{}점: {}등".format(score[k],rank[k]))
print()

ls = [10,20,30]
ls.append(1000)

for i in range(len(ls)):
    print("ls[{}]:{}".format(i,ls[i]))
print("리스트의 총 개수:",len(ls))
print("ls:",ls)
ls=[]
print("ls초기화 후:",ls)
print()

ls =[]
for i in range(0,4):
    ls.append(0)
Sum= 0

for i in range(0,len(ls)):
    ls[i]=int(input(str(i+1)+"번쨰 숫자:"))
    Sum+= ls[i]

for i in range(0,len(ls)):
    print("입력 받은 값 ls[{}]:{}".format(i,ls[i]))
print("합계:%d"%Sum)
print()

num = int(input('몇개의 공간 만들겠습니까:'))
ls=[]
Sum = 0
for i in range(num):
    ls.append(int(input(str(i+1)+"번째 숫자:")))
    Sum += ls[i]

for i in range(0,len(ls)):
    print("입력 받은 값 ls[{}]:{}".format(i,ls[i]))
print("합계:",Sum)
print()

list = [30,20,10]
print("현재 리스트:",list)

list.append(40)
print("append(40)후 리스트:",list)

print("pop()으로 추출한 값:",list.pop())
print("pop()후 리스트:",list)

list.sort()
print("sort() 후 리스트:",list)

list.reverse()
print("reverse() 후 리스트:",list)
del(list[2])
print("del()후 리스트:",list)