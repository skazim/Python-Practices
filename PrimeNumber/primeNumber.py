num = int(input("Enter any number"))
flag = False
if num >1:
    for i in range(2,num):
        if (num % i)  == 0:
            
            flag = True

if(flag):
    print(num, " is not a prime number")
else:
    print(num, " is a prime number")
print("End is entet hier")


