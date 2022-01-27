def prime_num(num):
    #print(num)
    for i in range(2,num):
       #print(i)
       if(num%i == 0):
           return "It is not a prime number"

    return "It is a prime number"        
    
user_num=int(input("Enter number: "))
result = prime_num(user_num)
print(result)
        