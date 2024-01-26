x = [1,2]
e =[]
adadha = []
mabnaha = []

while  x[0] != '-1' or x[1] != '-1':
    if int(x[1]) in range(2,10): 
        a = input()
        x = a.split()
        q = int(x[0])
        w = int(x[1])
        
        if q != -1:
            z = 0
            for i in range(1,q+1):
                if q%i == 0:
                    z = z + i
              
            
            
    
            
            list =[]
            while z !=0:
                list.append(z%w)
                z//=w    
            list = list[::-1]
            
        
        
            f = ''
            for g in list:
                f = f + str(g)
            r = int(f)
            e.append(r)
    else:
        print('invalid base!')
        
k = 0     
for v in e:
    k = k + v
print(k)    
            
            
            
            
    
# nahayi = []
# for n in jamha:
#     s=[]
#     for r in mabnaha:
        
#         while n != 0:
#             h = n%r
#             s.append(h)
#             n = n//r  
     
#         f = ''
#         for w in s:
#             f = f + str(w)
#         f = int(f)  
      
#         revers = 0
#         while f != 0:
#             digit = f % 10
#             revers = revers *10 + digit
#             f = f // 10
#         nahayi.append(revers)
#     print(nahayi)
      
# #         jamha.remove(n)
# #         mabnaha.remove(r)
# # u = 0       
# # for d in nahayi:
# #     u = u + d             











            
            