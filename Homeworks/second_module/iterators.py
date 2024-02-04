# Task 1

# Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters: 'iterable' and 'start', default is 0.
# Tips: see the documentation for the enumerate function
def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1

my_list = ['apple', 'banana', 'cherry']

for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")

 

# Task 2

# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 'start', 'end', and optional step. 
# Tips: See the documentation for 'range' function

def in_range(start, end, step=1):
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step

for number in in_range(1, 10, 2):
    print(number)


# Task 3

# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax.class MyIterable:
    
def __init__(self, start, end, step=1):
    self.start = start
    self.end = end
    self.step = step
    self.current = start

def __iter__(self):
    return self

def __next__(self):
    if (self.step > 0 and self.current < self.end) or (self.step < 0 and self.current > self.end):
        result = self.current
        self.current += self.step
        return result
    else:
        raise StopIteration

def __getitem__(self, index):
    calculated_index = self.start + index * self.step
    if (self.step > 0 and self.start <= calculated_index < self.end) or \
       (self.step < 0 and self.start >= calculated_index > self.end):
        return calculated_index
    else:
        raise IndexError("Index out of range")

my_iterable = MyIterable(1, 10, 2)

for number in my_iterable:
    print(number)

print(my_iterable[0])   
print(my_iterable[1])   
print(my_iterable[2])   
