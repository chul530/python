list = [30,20,10]
print("현재 리스트:",list)

print("10 값의 위치:",list.index(10))

list.insert(2,200)
print("insert(2,200)후 리스트:",list)

list.remove(200)
print("remove(200) 후 리스트:",list)

list.extend([555,666,555])
print("exted({555,666,555]) 후의 리스트:",list)

print("555값의 개수:",list.count(555))
print()

ls=[10,5,20,7,9,31,12,11,19,32]

odd=[0,0,0,0,0]
even = [0,0,0,0,0]
diff = [0,0,0,0,0]
for i in range(len(odd)):
    odd[i]=ls[2*i]
for i in range(len(even)):
    even[i]=ls[2*i+1]
for i in range(len(odd)):
    diff[i]=even[i]-odd[i]
print(diff)
print()

odd=[]
even=[]
diff=[]
for i in range(len(ls)):
    if i%2==0:
        odd.append(ls[i])
    else:
        even.append(ls[i])
for j in range(len(odd)):
    diff.append(even[j]-odd[j])
print(diff)
print()

odd_sum = 0
even_sum = 0
for i in range(len(ls)):
    if i%2==0:
        even_sum+=ls[i]
    else:
        odd_sum+=ls[i]
diff = even_sum - odd_sum
print(diff)
print()

invertls=[0,0,0,0,0]
for i in range(0,5):
    ls[i],ls[len(ls)-1-i]=ls[len(ls)-1-i],ls[i]
invertls=ls
print(invertls)
print()

invert=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(ls)):
    invert[i]=ls[len(ls)-1-i]
print(invert)
print()

for i in range(len(ls)-1,-1,-1):
    ls.append(ls[i])
    del(ls[i])
print(ls)
# print()

tmp=ls[:]
invert=[]
for i in range(len(ls)):
    invert.append(tmp.pop())
    print(invert)
print(ls)
print(invert)


sortls=[0,0,0,0,0]
for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            ls[i],ls[j]=ls[j],ls[i]
sortls=ls
print(sortls)
print()


reversels=[0,0,0,0,0]
for i in range(0,5):
    sortls[i],sortls[len(ls)-1-i]=sortls[len(ls)-1-i],sortls[i]
reversels=sortls
print(reversels)
print()

aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print('[0][0]',aa[0][0])
print('[0][1]',aa[0][1])
print('[0][2]',aa[0][2])
print('[0][3]',aa[0][3])
print('[1][0]',aa[1][0])
print('[1][1]',aa[1][1])

for i in range(len(aa)):
    for j in range(len(aa[i])):
        print(aa[i][j],end='\t')
    print()
print()

for i in aa:
    for j in i:
        print(j,end='\t')
    print()
print()   

aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a=aa[0]
a[1]=20000

print('[0]',aa[0])
print(a)
print(aa)

import copy
aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#a=aa[0][:]
a = copy.deepcopy(aa[0])

a[1]=200000000

print('[0]',aa[0])
print(a)
print(aa)