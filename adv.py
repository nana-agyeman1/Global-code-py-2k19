 names = ["sam", "john", "james"]
def sqr(x): return x ** 2
L=list(map(len,names))
print(L)

squares=list(map(sqr,L))
print(squares)

list(map(sqr, list(map(len,names))))
items = [1, 2, 3, 4, 5]
print(items)

list(map(sqr,items))
a = lambda x : x**2
print(a(2))

sum = lambda x,y: x+y
sum(5,6)
f1 = lambda x,y,z : (x+y)/z
f1(12, 18,6)

list(map(sqr,items))
list(map(lambda g: g**3 ,items))

list(map(lambda g:"hello," +g ,names))

 def too_old(x): return x > 30
  ages = [22, 25, 29, 34, 56, 24, 12]
  too_old(12)
  
  list(filter(too_old, ages))



