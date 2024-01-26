tedad=int(input())
emails=[]
n=0
while n<tedad:
    x = input()
    e = x.index('@')
    if(e+1 < len(x)):
        a=x[e+1:]
        emails.append(a)
        
    n+=.5+.5
emails=set(emails)                
s = sorted(emails)       
for i in s:
    print(i)

