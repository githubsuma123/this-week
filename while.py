#program to display numbers from 1 to 5
i=1
n=5
while i<=n:
    print(i)
    i=i+1
#program to calculate the sum of numbers
# until the user enters zero
s=0
num=int(input('enter a number:'))
while num!=0:
    s+=num
    num=int(input('enter a number:'))
print('s =',s)
