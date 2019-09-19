import random
list1 = []
x=int(input("Enter number of elements: "))
for i in range(0,x):
    list1.append(random.randint(10,100))
print(list1)
sum = 0
for i in list1:
    sum =sum+i
avg=sum/x
print("Sum: ",sum,"\t","Average:",avg)