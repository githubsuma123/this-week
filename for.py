#program to print first 10 NN using for loop
n=11
for i in range(1,n):
    print(i)
# program to print all the even numbers within the given range.
given_range=15
for i in range(given_range):
    if (i%2==0):
        print(i)
#program to calculate the sum of all numbers from 1 to a given number.
given_num=25
sum=0
for i in range(1,given_num+1):
    sum+=i
print(sum)
#program to calculate the sum of all the odd numbers within the given range.
given_range=10
sum=0
for i in range(given_range):
    if i%2!=0:
        sum+=i
print(sum)
#program to print a multiplication table of a given number
given_num=4
print("multiplication")
for i in range(11):
    print(given_num,"x",i,"=",5*i)
#program to display numbers from a list using a for loop.
list=[1,2,4,6,48,125]
for i in list:
    print(i)
#program to count the total number of digits in a number.
given_num=129765
given_num=str(given_num)
count=0
for i in given_num:
    count+=1
print(count)