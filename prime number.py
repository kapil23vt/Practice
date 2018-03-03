prime_numbers = 0

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    
    if x >= 2:
        for i in range(2,x):
            rem = x%i
            if rem == 0: # 6,8,15, 6%2, 8%2, 15%3, non primes
                return False
        return True

           
           
print (is_prime_number(4))