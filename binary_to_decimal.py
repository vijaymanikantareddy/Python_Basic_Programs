s=input('enter a binary number: ')
bin=s[::-1]
n=0
for i in range(len(bin)):
    if bin[i]=='1':
        n+=2**i
print('binary number is decimal number is :', n) 
