import functools
from functools import reduce


'''def is_even(x): return x % 2 == 0
    
numbers = [1,56,234,87,4,76,24,69,90,135]

#print(list(filter(is_even, numbers)))


#print(list(map(is_even, numbers)))


num = lambda x: x % 2

#print(list(filter(num, numbers)))

#print(list(map(is_even,numbers)))
#print(list(filter(is_even,numbers)))'''


'''#total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
#print(total)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)

print([len(word) for word in words])'''

'''letters = " I love Global code"
words = letters.split()
print([len(word) for word in words])'''

'''numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#f = list(filter(lambda x: x > 0, numbers))
#print(f)
#print(list(filter(positive, numbers)))
print([n for n in numbers if n > 0])'''








'''print([n for n in range(1,50,2)])'''

'''words = ["hello", "my", "name", "is", "sam"]

length = [len(word) for word in words]
word = [word.upper() for word in words]
print(tuple(zip(word, length)))'''


'''import math

def factorial():
     n = int(input("Enter number : "))
     print(math.factorial(n))
     
factorial()'''

'''def factorial():

    n = int(input("Enter number: "))

    factorial = 1
    if n < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,n + 1):
           factorial = factorial*i
       print("The factorial of",n,"is",factorial)

factorial()'''



 



     

