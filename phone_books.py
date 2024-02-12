n=int(input())
phone_book={}
for i in range(n):
    names, phones = input().strip().split()
    phone_book[names]=phones
    

try:
    while True:
        name=input()
        if name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
except EOFError:
    pass