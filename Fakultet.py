# Victoria Lee, grudat24 uppg 1.1

def factorial(n):
    """Calculate the factorial of n"""

    if not isinstance(n,int) or isinstance(n, bool) or n < 0: 
        return False
    
    c = 1
    for i in range(1,n+1):
        c = c*i
    return c
    

# Unit test
assert factorial(2)==2
assert factorial(1)==1
assert factorial(0)==1
assert factorial(20)==2432902008176640000
assert factorial(-2)==False

assert factorial('a')==False
assert factorial(1.2)==False
assert factorial([1, 2])==False
assert factorial(None)==False
assert factorial(True)==False

print ("The test is done")