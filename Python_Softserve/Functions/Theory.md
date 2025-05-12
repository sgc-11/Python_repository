# Functions Theory

## Python Data Types
1. Immutable (called by value)
    * Numbers
    * Strings
    * Tuples
    
2. Mutable (called by reference)
    * Lists
    * Dictionary
    * Sets

## Regular and Default Parameters

**Regular Parameter**: Provided when the function is called
```python
def greet (name): #-> regular parameter
    print(f"Hello, {name})
```

**Default Parameters**: Assigned in the function definition
```python
def greet (name="friend", lastname="cook"): #-> default parameter
    print(f"Hello, {name})
```
* Default arguments initialized by first usage of function and if they are mutable they may be changed for every next usage.

Example
```python
def add_item(item, items=[]):  # Mutable default parameter (list)
    items.append(item)
    return items

print(add_item("apple"))       # Output: ['apple']
print(add_item("banana"))      # Output: ['apple', 'banana'] ❗
print(add_item("cherry"))      # Output: ['apple', 'banana', 'cherry'] ❗❗
```

Correct way

```python
def add_item(item, items=None):
    if items is None:
        items = []  # New list created each time
    items.append(item)
    return items

print(add_item("apple"))       # Output: ['apple']
print(add_item("banana"))      # Output: ['banana']
```

## Variable-list arguments
* To give any number of (positional) arguments into a function, use the `*` in front of the argument name.

Example (*args: accepts any number of positional arguments like separated by commas)
```python
def greet_all(*names):
    for name in names:
        print(f"Hello,{name}")

greet_all("Alice", "Bob", "Charlie")
```

*names collects all the extra positional arguments into a tuple

* Also, it is possible to give a function any number of keyword arguments. The function must accept an argument that is marked with double-asterisk `**`
* A function can accept both any number of arguments and any number of keyword arguments.

Example (**kwargs: Allows a function to accept any number of keyword arguments like key=value)
```python
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, country="USA")
```

Example using both

```python
def show_all(fixed, *args, **kwargs):
    print("Fixed argument:", fixed)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_all("first", "second", "third", name="Alice", age=25)
```

Output
```python
Fixed argument: first
Positional arguments: ('second', 'third')
Keyword arguments: {'name': 'Alice', 'age': 25}
```

## Lambda function
A lambda function is a small anonymous function.
* Can take any number of arguments, but can only have one expression.
```python
lambda[arguments]: expression
```
* Can be used along with built-in functions like
    * filter()
    * map()
    * reduce()
* It has no name, unless you assign it
* Used for short, simple operations,
* define it in one line
* no return keyword needed

Examples

```python
add = lambda a, b: a + b
print(add(2, 3))
```
```python
square = lambda x : x ** 2
print(square(4))
```
```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x : x * x, numbers))
print(squares)
```

**When to use it?**
* Need a quick function, especially inside functions like `map()`, `filter()`, or `sorted()`.
* For simple logic (just one line)

**Limitations**
* One expression -> no loops, conditionals
* For complex logic, use `def`

## Recursive Functions
Recursion is a way of programming in which a function calls itself one or more times in its body.

Tail recursive means the recursive call is the last thing executed by the function.

Divided in two cases:
1. base case or termination case
2. recursive case

`Use recursion, if and only if on each iteration your task splits into two or more similar tasks.`

**Advantages**
* Clean code
* Complex task broken down into simpler sub-problems 
* Sequence generation is easier with recursion than using some nested iteration.

**Disadvantages of Recursion**
* Logic is hard sometimes
* Recursive calls are expensive in resources (memory and time)
* Hard to debug

## First class functions
**Properties of first class functions**
1. A function is an instance of the Object type
2. You can store the function in a variable
3. You can pass the function as a parameter to another function
4. You can return the function from a function.
5. You can store them in data structures such as hash tables, lists, etc.

## Inner (nested) functions
* Function defined inside another function.
    * Access variables of the enclosing scope.
    * Used so they can be protected from everything happening outside the function. `Encapsulation`

Ejemplo
```python
def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))  # 15
```
* multiplier is an internal function that remmebers `x=3` even after make_multiplier finished. This is called `closure`.

## LEGB rule
Local scope -> Enclosing Scope -> Global Scope -> Built-in

```python
type(0) # Built-in
x = 10 # Global scope
def enclosing ():
    x = 20 # Enclosing Scope
    def inner():
        x = 30 # Inner scope
```

## Closure
* There must be a nested function
* The inner function has to refer to a value that is defined in the enclosing scope
* The enclosing function has to return the nested function

## Factory Functions
* Function that creates another object
* Often used closure or lambda functions

```python
def make_adder (x):
    return lambda y: x + y

add5 = make_adder(5)

print(add5(3))
print(add5(7))
```
* We could create multiple functions with the make_adder

## Decorators
Design pattern that allows user to add new functionality to an existing object without modifying its structure.
* Usually called before the definition of a function you want to decorate

* Takes in a function, adds some functionality and returns it.

**Why use decorators?**
1. Add logging
2. Check permissions
3. Measure performance
4. Cache results
5. Repeat behaviour in many places

Example

```python
def decorator_function (original_function):
    def wrapper_function():
        print("This runs **before** the original function.")
        original_function()
        print("This runs **after** the original function")
    return wrapper_function()
```

Two ways to use the decorator function

1. 
```python
@decorator_function
def say_hello():
    print("Hello")

say_hello()
```

2. 
```python
def say_hello():
    print("Hello")

say_hello = decorator_function(say_hello)

say_hello()
```
## Generators
Generator function contains one or more yield statements
* It returns an object(iterator) but does not start execution immediately.
* Methods like __iter__() and __next__ are implemented automatically. So we can iterate through the items using `next()`.
* Once the function yields, the function is paused and the control is transfered to the caller.
* Local variables and their states are remembered between successive calls.
* When the function termiantes, StopIteration is raised automatically on further calls.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
```

## Generator Expression
Similar to lambda, generator expressions create anonymous generator functions.
* The difference between list comprehension and generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time
* Lazy execution (Produces when it is asked for)
* Memory efficient

**List comprehension**
```python
squares = [x * x for x in range(5)]

print(squares) # Output: [0, 1, 4, 9, 16]
```

**Generator Expression**
```python
squares_gen = (x * x for x in range(5))

print(squares_gen) # Output: <generator object ...>

for num in squares_gen:
    print(num)
```








