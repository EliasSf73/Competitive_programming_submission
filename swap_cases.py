def swap_case(s):
    st=''
    for x in s:
        if x.isupper():
            st+=x.lower()
        else:
            st+=x.upper()
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)