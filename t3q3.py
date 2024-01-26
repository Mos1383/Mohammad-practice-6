tedad=int(input())
emails=[]
n=0
while n<tedad:
    x = input()
    e = x.index('@')
    if(e+1 < len(x)):
        a=x[e+1:]
        emails.append(a)
        
        # if a not in emails:
            # emails.append(a)
    n+=1
emails=set(emails)                
s = sorted(emails)       
for i in s:
    print(i)

# این کد رو جوری تغییر بده که زمان اجراش کمتر بشه
# tedad=int(input())
# emails=[]

# for i in range(0,tedad):
#     emails.append(input())
# import re
# z=[]
# for i in emails:
#     q= i.index('@')
#     w= i.index('.com')
#     e= w-q-1
#     s = re.findall('^@[A-Za-z]{e}.com')
#     z.append(s)
# for i in s:
#     print(i)        