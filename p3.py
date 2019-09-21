# cook your dish here
count=0
t= int(input())
for x in range(t):
    s=[]
    r=[]
    count=0
    sc = input().split(" ")
    for i in range(len(sc)):
        sc[i] = int(sc[i])
    s=input().split(",")
    r=input().split(",")
    
    for j in range(len(s)):
        if s[j] == 'L' and r[j] == 'A':
            s[j]= 'O'
            
    for l in range(len(s)):
        count = s.count('O')
    
    if count<sc[1]:
        print("Session Cancelled")
    else:
        print("Session Running")
        
        
    
'''
Input:
2
8 7
O,L,O,L,L,O,O,O
A,NA,A,A,NA,A,A,A
8 6
O,L,O,L,L,O,O,O
A,NA,A,A,NA,A,A,A

Output:
Session Cancelled
Session Running


'''