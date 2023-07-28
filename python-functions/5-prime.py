def is_prime(number):
    if number <= 1:
        return False # Numbers less than or equal to 1 are not prime so, return False
    
    # Check for the divisors from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False # If the number is divisibe by 'i', it has other divisors besides 1 and itself, so it's not prime.
    
    return True # If the loop completes without finding any divisors, the number is prime, so return True