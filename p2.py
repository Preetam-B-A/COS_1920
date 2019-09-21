# cook your dish here

t = int(input())
ptr = 0
for i in range(t):
    es = []
    a = []
    
    es = input().split(" ")
    for i in range(len(es)):
        es[i] = int(es[i])
        
    #print(es)
    
    a = input().split(" ")
    for j in range(len(a)):
        a[j] = int(a[j])
        
    #print(a)
    
    etm = es[0]+es[1]*31
    atm = a[0]+a[1]*31
    
    dif = atm-etm
    
    if dif == 0:
        ptr+= 10
    elif dif>0 and dif<=2:
        ptr+=6
    else:
        ptr+=2
        
avg = ptr/t
avg = int(avg)

if avg == 10:
    g = 'A'
elif avg<=9 and avg >=7:
    g= 'B'
elif avg<=6 and avg >=5:
    g='C'
else:
    g='D'
print(avg,g)
    
'''
Input:
3
9 9 2019
9 9 2019
10 10 2019
11 10 2019
15 11 2019
19 11 2019

Output:
6 C

'''