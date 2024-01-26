import math
tale = input()
# if tale != 'sum' and tale != 'average' and tale != 'lcd' and tale!= 'gcd' and tale!='min' and tale!='max':
#     print('Invalid command')
    
# else:
#     pass
while tale != 'sum' and tale != 'average' and tale != 'lcd' and tale!= 'gcd' and tale!='min' and tale!='max':
    print('Invalid command')
    break
else:
    adadha = 1
    a = []
    b = []
    while adadha != 'end':
        adadha = input()
        b.append(adadha)

        
    for i in b[0:len(b) - 1]:
        i= int(i)
        a.append(i)
        

    s = 0    
    if tale == 'sum':
        for i in a[0:len(a)]:
            s = s + (i)
        print(s)
            
    elif tale == 'average':
        for i in a[0:len(a)]:
            s = s + (i)
        nahayi = round(s/(len(a)),2)
        print(nahayi)
            
    elif tale == 'lcd':
        def compute_lcm(a):
            """
            This function takes a list of integers and returns their LCM.
            """
            def gcd(c, d):
                """
                This function calculates the greatest common divisor (GCD) of two integers.
                """
                while d:
                    c, d = d, c % d
                return c

            lcm = a[0]
            for i in range(1, len(a)):
                gcd_val = gcd(lcm, a[i])
                lcm = lcm * a[i] // gcd_val
            return lcm 
        
        lcm = compute_lcm(a)
        print(lcm)
        
    elif tale == 'gcd':
        a = tuple(a)
        from functools import reduce
        resault = reduce(math.gcd, a)
        print(resault) 

    elif tale == 'min':
        q = min(a)    
        print(q)
        
    elif tale == 'max':
        w = max(a)
        print(w)        
            
            