import math

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,math.floor(math.sqrt(num))):
           if (num % i) == 0:
               break
       else:
           print(num)
