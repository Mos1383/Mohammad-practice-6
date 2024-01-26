seton = int(input())
my_list = []
jahat = 0
while jahat != 'END':
    jahat = input().strip()
    my_list.append(jahat)
my_list.remove('END')    

q=1
for i in my_list:
    if i=='B':
        q+=1
        
noghteha = []        
for n in range(1,q+1):
    p=[]
    for m in range(1,seton+1):
        p.append('.')
    noghteha.append(p)
      
a=0
b=0      
for r in my_list:
    if r=='B':
        a+=1
        noghteha[a][b]='*'
    if r=='R' and b+1<seton:
        b+=1
        noghteha[a][b]='*'
    if r=='L' and b-1>=0:
        b-=1
        noghteha[a][b]='*'
 
noghteha[0][0]='*'
                       
for i in noghteha:
    print(' '.join(i))   
    
if a+1-seton!=0:
    print("There's no way out!")