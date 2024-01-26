ramz = input().split()
x=0
for i in ramz:
    x+=1
y=[]    
for i in range(0,x):
    y.append(ramz[i][0])
q=[]    
for i in range(0,x):
    q.append(ramz[i][1:])
w = []    
for i in range(0,x):
    i=str(i)
    e = q.index(i)
    w.append(y[e])
print(''.join(w))        