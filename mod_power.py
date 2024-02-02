# Enter your code here. Read input from STDIN. Print output to STDOUT
def power(a, b):
    line1=1
    for i in range(b):
        line1*=a
    
    return line1
def mod_power(a, b, m):
    pow=power(a, b)
    return pow % m
   
    
    
if __name__=='__main__': 
    a=int(input())
    b=int(input())
    m=int(input())
    print(power(a, b))
    print(mod_power(a, b, m))