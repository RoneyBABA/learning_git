num=int(input("Enter a number to know its fibonacci value the the said sequence: \n"))
a=0
b=1
c=0
if (num < 3):
    print ('fibonacci Value at', num, 'palce of the sequnce is', num-1)
else:
    for i in range (num-2):
        c = a+b
        a=b
        b=c
    
print ('fibonacci Value at', num, 'palce of the sequnce is', c)

#i fixed the bug here