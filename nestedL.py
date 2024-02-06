if __name__=='__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        scores = float(input())
        students.append((name,scores))
    students.sort(key=lambda x: (x[1],x[0]))
    grades=[grade for name,grade in students]
    grades=sorted(set(grades))
    sec_low_grade=grades[1]
    sec_low_name=[name for name,grade in students if grade==sec_low_grade]
    sec_low_name.sort()
    for name in sec_low_name:
        print(name)
            
        
   
    

