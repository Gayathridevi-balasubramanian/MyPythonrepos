def primefactors(num):
    factor = []
    divisor = 2
    while num > 1:
        while num % divisor == 0 :
            factor.append(divisor)
            num //= divisor
        else:
            divisor = divisor + 1
    return factor

# to find out all the prime numbers
s = primefactors(2470)
print(s)

''' the logic is
         factor is an empty list , divisor starts with 2
          the prime factor has to be found till it is 1 but not 1
           when mod of num%divisor == 0 then append to the factor list
            and update the number to the divisor '''
