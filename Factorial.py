

def factorial_itterative(n):
    result = 1
    for i in range(1,n+1):
        result = result * i

    return result


def factorial_recurssive_head(n):
    if n == 0:
        return 1
    if n < 0:
        return "Factorial of -ve numbers is undefined"

    return n *factorial_recurssive_head(n-1)

def factorial_recurssive_tail(n,result=1):
    if n == 0:
        return result
    if n < 0:
        return "Factorial of -ve numbers is undefined"

    result = result * n
    return factorial_recurssive_tail(n-1,result)




#print(str(factorial_itterative(1000000000)))

print(str(factorial_recurssive_head(24)))
print(str(factorial_recurssive_tail(24)))

