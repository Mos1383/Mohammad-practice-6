adad1 = int(input())
adad2 = int(input())

ekhtelaf1 = 32 - len(bin(adad1)[2:])
adad1 = ekhtelaf1*'0' +  bin(adad1)[2:]

ekhtelaf2 = 32 - len(bin(adad2)[2:])
adad2 = ekhtelaf2*'0' +  bin(adad2)[2:]

adad_nahayi = adad2 + adad1

tedad = int(input())
x = 0
list = []
while x < tedad:
    b = int(input())
    list.append(b)
    x += 1
    
for i in list:
    c = 63 - i
    if adad_nahayi[c] == '1':
        print('yes')
    else:
        print('no')