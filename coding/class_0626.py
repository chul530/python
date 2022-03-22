# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i,end=" ")
# print()

# for i in [11,1,5,10,15,6,3,9,14]:
#     print(i,end=" ")
# print()

# ls=[1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     print("i:",i)
# for i in ls:
#     print(i,end=" ")
# print()

# ls = [10,"test",123.123]
# print("list:",ls)
# print()
# for i in ls:
#     print("i에",i,"대입한 후 print() 실행")
#     print(type(i))
# print()

# st = "Hello Python"
# for i in st:
#     print("i:",i)
# print()

# a_ = 0
# s_ = 0
# i_ = 0 
# st = "It is a fun Python class"
# for i in st:
#     i_+=1
#     if i=="a":
#         a_+=1
#     elif i=="s":
#         s_+=1
# print(i_)
# print(a_)
# print(s_)
# print()

# print("{0}+{1}={2}".format(10,2,10+2))
# print("{2}+{1}={0}".format(10,2,10+2))
# print("{}+{}={}".format(10,2,10+2)) # 차례대로

# print("{:,}".format(1000000))

# print("{:<10},왼쪽정렬,{:0<10}".format('첫번째','두번째'))
# print("{:>10},오른쪽정렬,{:9<10}".format('첫번째','두번째'))
# print("{:^10},가운데정렬,{:5^10}".format('첫번째','두번째'))
# print()

# for i  in range (0,3,1):
#     for k in range(0,5,1):
#         print("이중 for 문(i:%d\tk:%d)"%(i,k))

# print("{:-^61}".format('구 구 단'))
# for i in range(2,10):
#     print("{:^5}".format('%d단'%i),end="\t")
# print()
# print("-"*64)
# for i in range(1,10):
#     for j in range(2,10,1):
#         print("%d*%d=%d\t"%(j,i,i*j),end="")
#     print()
# print()

# for i in range(0,5):
#     print("상위포문",i,"일때 하위 포문:",end=" ")
#     for j in range(0,5):
#         print(i*j,end="  ")
#     print()
# print()

for i in range(1,25,5):
    for j in range(0,5):
        print(i+j,end="\t")
    print()
