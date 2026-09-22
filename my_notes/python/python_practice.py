# Q1
class FibonacciIterator:
   def __init__(self, limit):
      self.limit = limit
      self.count = 0
      self.a = 0
      self.b = 1

   def __iter__(self):
      return self

   def __next__(self):
    if self.count >= self.limit:
       raise StopIteration
    self.count += 1
    temp = self.a
    self.a = self.b
    self.b = temp + self.b
    return temp

for num in FibonacciIterator(10):
   print(num)

# Q2
def fibonacci_gen(limit):
    a = 0
    b = 1
    for _ in range(limit):
        yield a
        temp = a
        a = b
        b = temp + b
        
for num in fibonacci_gen(20):
    print(num)

# Q3
def make_decor(f):
    def decor(*args, **kwargs):
        print(f'{f.__name__} called with parameters: {args}')
        result = f(*args, **kwargs)
        print(f'{f.__name__} returned: {result}')
        return result
    return decor

def _fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return _fib(n - 1) + _fib(n - 2)

@make_decor
def fib(n):
    return _fib(n)

fib(10)