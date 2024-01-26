adadha= input()
adadha=adadha.split()
number1=int(adadha[0])
number2=int(adadha[1])

if number2<number1:
    
    c = 0
    for i in range(1 , number1 + 1):
        x=0
        for t in range(1 , i + 1):
        
            if i%t == 0:
                x += 1
        if x==2:
            c += 1

        
    s = 0
    for j in range(1 , number2):
        y=0
        for k in range(1 , j + 1):
        
            if j%k == 0:
                y += 1
        if y==2:
            s += 1

    v = c - s           
    print('reverse order - amount:', v)
else:
    c = 0
    for i in range(1 , number1):
        x=0
        for t in range(1 , i + 1):
        
            if i%t == 0:
                x += 1
        if x==2:
            c += 1

        
    s = 0
    for j in range(1 , number2 + 1):
        y=0
        for k in range(1 , j + 1):
        
            if j%k == 0:
                y += 1
        if y==2:
            s += 1
    v = s - c
    print('main order - amount:', v)           
                