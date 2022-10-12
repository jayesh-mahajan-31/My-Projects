import math   
PF=[]
def prime_factors(num):  
    while num % 2 == 0:  
        PF.append(2)  
        num = num / 2  
  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
  
        while num % i == 0:  
            PF.append(i)
            num = num / i  
    if num > 2:  
        PF.append(num)  
    print(PF)
  
num = int(input("Enter a number : \n")) 
prime_factors(num)