x = int(input())
jomle =input()
kalame =input()


def fasele (a,b):
    r=0
    if len(a)==len(b):
        for i in range(0,len(a)):
            if a[i]==b[i]:
                pass
            if a[i]!=b[i]:
                r+=1
        return(r)
    
    elif len(a)<len(b):
         ekhtelaf= len(b)-len(a)
         
         a = a + ekhtelaf * '_'
         for i in range(0,len(a)):
            if a[i]==b[i]:
                pass
            if a[i]!=b[i]:
                r+=1
         return(r)
     
    elif len(a)>len(b):
         ekhtelaf= len(a)-len(b)
         
         b = b + ekhtelaf * '_'
         for i in range(0,len(a)):
            if a[i]==b[i]:
                pass
            if a[i]!=b[i]:
                r+=1
         return(r)                
mylist = jomle.split()

for i in range(0,len(mylist)):
    q= mylist[i]
    if q[-1] == '.' or q[-1] == 'ØŒ' or q[-1] == '!' or q[-1] == '?' or q[-1] == '_' or q[-1] == '(' or q[-1]==':':
        q = q[0:len(q) - 1]
    w = fasele(kalame,q)
    if w<=x:
        print(q)