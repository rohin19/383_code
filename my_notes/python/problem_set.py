# Q1

# The list comprehension is a notation, compared to list literals,
# that allows you to express the content of a list declaratively.

    # Explain what is List literals: [1, 2, 3], ["ziyi", "yan", "sfu", "python"].
    # Draw a connection between list comprehension and math notation of a set/list:
    # a. Math notation of sets/lists: { x 2 : x ∈ { 1 , 2 , 3 , 4 , 5 } } . 
    # b. Python List Comprehension: [x**2 for x in [1, 2, 3, 4, 5]].
    # Refer to the official docs: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions


# Q2
import math
from time import time


print("Q2: ")

one_to_hund = [x for x in range(100) if x % 5 == 0]
print(one_to_hund)

strings = ["even", "odd", "length", "strings", "are", "fun"]
odd_len_str = [s for s in strings if len(s) % 2 != 0]
print(odd_len_str)

num = [0, 2, -2, 0, 3]
print([x+1 if x < 0 else x-1 for x in num if x != 0])

four_bit = [(w, x, y, z) for w in range(2) for x in range(2) for y in range(2) for z in range(2)]
print(four_bit)

list_a = [1, 2, 3]
list_b = [2, 5, 6]
list_c = [7, 8, 9]
three_tuples = [(a, b, c) for a in list_a for b in list_b for c in list_c if a != b and b != c and a != c]
print(three_tuples)

int_sols = [(a, b, c) for a in range(100) for b in range(100) for c in range(100) if a < b < c if a**2 + b**2 == c**2]
print(int_sols)

# Q3

# The walrus operator is used to eliminate unnecessary computation
# if there are computations happening in the if-condition evaluation, the results ca
# be saved and used in the final outputs:
# high_scores = [(n, get_score(n)) for n in all_names if get_score(n) % 5 != 0]
# high_scores = [(n, score) for n in all_names if (score := get_score(n)) % 5 != 0]

# Q4
print("\nQ4: ")
# a
def my_zip2(A, B):
    return([(A[i], B[i]) for i in range(min(len(A), len(B)))])
# b
A = [1, 2, 3]
B = [4, 5, 6]
dot_product = sum([a*b for a, b in my_zip2(A, B)])
print(dot_product)
# c
def my_zip(*lists):
    if len(lists) < 2:
        raise ValueError("my_zip requires at least 2 list arguments.")
    min_length = min(len(lst) for lst in lists)
    zipped = []
    for i in range(min_length):
        tuple_element = tuple(lst[i] for lst in lists)
        zipped.append(tuple_element)
    return zipped
# for i in my_zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]): print(i)
# for i in zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]): print(i)
# d
def add_lists(*lsts):
    return [sum(row) for row in my_zip(*lsts)]
print(add_lists([1, 2, 3], [4, 5, 6], [1, 1, 1]))

# Q5
print("\nQ5: ")

# loop and enumerate
def make_numbered_list_a(lst):
    lines = []
    for i, str in enumerate(lst):
       lines.append(f"{i+1}. {str}")
    return '\n'.join(lines)
result = make_numbered_list_a(['apple', 'banana', 'cherry'])
print(result)

# list comprehension and enumerate
def make_numbered_list_b(lst):
    lines = [f"{i+1}. {str}" for i, str in enumerate(lst)]
    return '\n'.join(lines)
result = make_numbered_list_b(['apple', 'banana', 'cherry'])
print(result)
# one line
def make_numbered_list_c(lst):
    return '\n'.join(f"{i+1}. {str}" for i, str in enumerate(lst))
result = make_numbered_list_c(['apple', 'banana', 'cherry'])
print(result)

# Q6
print("\nQ6: ")
def get_max(lst):
    max_val = lst[0]
    for i, elem in enumerate(lst):
        if elem > max_val:
            max_val = elem
    return max_val
print(get_max([4, 8, 4, 1]))
print(get_max(['soap', 'cat', 'dog']))

# Q7
# The iterator protocol is a mechanism for stepping through a sequence/stream of data one element at a time
# it defines how objects can be made loopable under the hood
# Iterable - object that can produce an iterator (list, tuple, dict, set, str)
# Iterator - object that tracks where you are in a sequence and hands you the next item
# __iter__() - returns new iterator object on an Iterable, or returns self if the object is already an Iterator
# __next__() - advances the sequence by one and returns next item
# If there is no more data: the next() method will raise a StopIteration exception

# Q8
print("\nQ8: ")
class My_reversed:
    def __init__(self, str):
        self.str = str
        self.index = len(str)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.str[self.index]
        else:
            raise StopIteration
for c in My_reversed('cat'):
    print(c)

# Q9
# Iterable and Iterator are different concepts in Python
# a string is iterable, it contains sequenced data that can be read. It has no 
# state to track where you are. A string is NOT an iterator, it does not have a
# __next__() method, cannot be used to return the next item.

# Q10
print("\nQ10: ")
class My_enumerate:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.lst):
            res = (self.index, self.lst[self.index])
            self.index += 1
            return res
        else:
            raise StopIteration
for i, v in My_enumerate(['a', 'b', 'c']):
    print(i, v)

# Q11
print("\nQ11: ")
def my_range_gen(a, b):
    current = a
    while current < b:
        yield current
        current += 1
def my_zip2_gen(a, b):
    for i in range(len(a)):
        yield a[i], b[i]

# Q12
print("\nQ12: ")
def longer_than_gen(n, lst):
    for s in lst:
        if len(s) > n:
            yield s
pets = ['cat', 'hamster','dog', 'bird']
for s in longer_than_gen(3, pets):
    print(s)

# Q13
print("\nQ13: ")
def lines_of_file_gen(filename):
    with open(filename) as f:
        for i, line in enumerate(f):
            line = line.strip()
            yield i, line

# Q14 
print("\nQ14: ")
def make_bounds_checker(min, max):
    def bounds_checker(x):
        return x > min and x < max
    return bounds_checker

good_score = make_bounds_checker(0, 100)
print(good_score(50)) # True
print(good_score(101)) # False
is_teen = make_bounds_checker(13, 19)
print(is_teen(15)) # True
print(is_teen(12)) # False
print(is_teen(20)) # False

# Q15
# A decorator is a function that takes another function as a input and 
# returns a modified version of that function as an output

# Q16
print("\nQ16: ")
def always_return_str(f):
    def new_f(*args, **kwargs):
        res = f(*args, **kwargs)
        if not isinstance(res, str):
            return str(res)
        return res
    return new_f
@always_return_str
def f(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 2
    elif n == 3:
        return [1, 2, 3]
    else:
        return ''
# isinstance(x, str) returns True if x is a string, and False otherwise
print(f(1), isinstance(f(1), str))
print(f(2), isinstance(f(2), str))
print(f(3), isinstance(f(3), str))
print(f(4), isinstance(f(4), str))

# Q17
print("\nQ17: ")
class LoggedTimer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.start_time = time.time()
        self.file = open(self.filename, 'w')
        self.file.write(f"Started at {self.start_time}\n")
        return self
    def log(self, message):
        if self.file:
            self.file.write(f"{message}\n")
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time.time()
        elapsed = self.stop_time - self.start_time
        self.file.write(f"Stopped at {self.stop_time}\n")
        self.file.write(f"Elapsed: {elapsed:.3f} seconds\n")
        self.file.close()
        print(f"Logged to {self.filename}")
        return False
# with LoggedTimer('timer.log') as t:
#     t.log("Starting sleep ...   ")
#     time.sleep(1)
#     t.log("Done sleeping!")
# print('Done!')

# Q18
print("\nQ18: ")
def classify_grade(score):
    match score:
        case score if score >= 90:
            return 'A'
        case score if score >= 80:
            return 'B'
        case score if score >= 70:
            return 'C'
        case score if score >= 50:
            return 'D'
        case _:
            return 'F'
print(classify_grade(95))   # A
print(classify_grade(80))   # B
print(classify_grade(79))   # C
print(classify_grade(62))   # D
print(classify_grade(48))   # F

# Q19
print("\nQ19: ")
def calculate_area(shape):
    match shape:
        case ("circle", r):
            return math.pi * r ** 2
        case ("rectangle", w, h):
            return w * h
        case ("triangle", b, h):
            return 0.5 * b * h
        case ("square", s):
            return s ** 2
        case _:
            return None
print(calculate_area(("circle", 5)))       # 78.539...
print(calculate_area(("rectangle", 4, 6))) # 24
print(calculate_area(("triangle", 3, 8)))  # 12.0
print(calculate_area(("square", 7)))       # 49
print(calculate_area(("hexagon", 4)))      # Unknown shape

def reverse_enumerate(L):
    i = len(L) - 1
    while i >= 0:
        yield L[i], i
        i -= 1

words = ["cat", "dog", "apple", "bananna"]
for value in reverse_enumerate(words):
    print(value)