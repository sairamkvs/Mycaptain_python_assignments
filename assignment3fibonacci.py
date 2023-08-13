nterms = int(input ("How many terms to print? "))

# First two terms  
a = 0  
b = 1  
count = 0  
while count < nterms:  
        print(a)  
        nth = a + b  
        a = b 
        b = nth  
        count += 1  
