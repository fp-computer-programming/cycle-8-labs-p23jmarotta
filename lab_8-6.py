# Creator JM 12/7/22

def factorial(num):
    f = 1 # will be the factorial
    i = 1
    while i < (num + 1):
        f = f * i # multiply itself by the next number
        i += 1
    return f
    

print(factorial(12)) # returns 479001600 = 12!