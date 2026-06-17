# start=int(input("Enter the value a: "))
# for i in range(start,-1):
#     print(*range(start,i+1),sep='*')

# print(*range(2,40,2))

# for i in range(int(input('Enter the number : ')),0,-1):
#     print(*range(1,i+1),sep='*')

# sample=[1,2,3,4,5,6,7,8,9,10]
# for i in sample:
#      if i%2==0:
#       print(i, end=" ")

# n=int(input("Enter the value: "))
# result=[0]*n
# for i in range(n):
#     result[i]=int(input())
# print(result)

# a=int(input("Number : "))
# result=[]
# for i in range(a):
#     result.append(int(input()))
# print(result)

# a=[1,2,100,87,0]
# print(max(a),min(a))

# list=[1,1,2,2,4]
# number=int(input())
# print(list.count(number))

# number=[1,3,3,5,7,7]
# a=int(input("Enetr a number: "))
# count=0
# for i in number:
#      if i==a:
#         count=count+1
# print(count)


# list=[1,2,3,4,5]
# print([x**2 for x in list])

# num=int(input("Enter the value: "))
# # print('exists' if num in list else 'does not exists')

# for i in list:
#     if(num==i):print("exists");break;
# else:print("does not exists")


number=[1,3,3,5,7,7]
stream=[]
for i in number:
    if number.count(i)>1:
        print(i)
        break
    stream.append(i)
else:print('No duplicates found')

print("Git connected sucessfully")