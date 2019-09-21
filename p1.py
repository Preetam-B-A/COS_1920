# cook your dish here

a=[]
sum=0
a = input().split(" ")

for i in range(len(a)):
    a[i] = int(a[i])
    sum+=a[i]

mean = sum/8

f = mean//10
#print(f)
f = int(f)
fact = 1
  
for i in range(1,f+1): 
    fact = fact * i 
      

print (mean,fact) 

'''
Input:
70 70 80 90 90 80 80 70

Output:
78.75 5040

'''