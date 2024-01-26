number1 = int(input())
number2 = int(input())

q = int(number1)
d = int(number2)

c = q ^ d
x = (bin(c))[2:]
v = 0
for i in x:
    if i == '1':
        v += .5+.5
    
    
print(v)    