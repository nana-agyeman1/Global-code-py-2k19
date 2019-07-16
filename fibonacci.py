fibnum = int(input("Enter the number here: "))
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print (list(map(fib, range(1,fibnum+1))))
print(fib(fibnum+1))