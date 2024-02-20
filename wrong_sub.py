inputs=input().split()
n=int(inputs[1])
# print(n)
# print(inputs)
initial=inputs[0]
for  i in range(n):
   
    if initial[-1]=='0':
        initial=initial[:-1]
    
    else:
        int_form=int(initial)-1
        initial=str(int_form)
    
    
  
print(initial)