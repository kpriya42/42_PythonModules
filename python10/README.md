
# Python 10 : FuncMage – Functional Programming

This module introduces **higher-order functions, decorators, lexical scoping and lambda spell**

- Exercise 0: Lambda Sanctum - Master anonymous functions and lambda expressions
- Exercise 1: Higher Realm - Discover the power of higher-order functions 
(functions can modify, combine, and enhance other functions)
- Exercise 2: Memory Depths - Understand lexical scoping and closures
- Exercise 3: Ancient Library - Explore the functools module’s treasures
- Exercise 4: Master’s Tower - Create powerful decorators and class methods

## Lambda functions/ expressions

Lambda expressions make code more concise because they let you define a small function exactly where you need it, without writing a separate def block.

````bash
#"Does lambda make this easier to read?"
#Syntax
lambda arguments: expression

````

## First-class citizens

Functions are first-class citizens means that functions can be treated like ordinary values. They can be :
- assigned to a variable,
- passed as an argument to another function,
- returned from another function,
- stored inside data structures like lists or dictionaries.

```bash
def greet(name):
    return f"Hello {name}"


message = greet
print(message("Alice"))
```

##  Lexical scoping
Lexical scoping in Python means that where a variable is available is determined by where the code is written/nested in the source code.
Python looks for a variable using the LEGB rule:
```
L = Local
E = Enclosing
G = Global
B = Built-in
```
### Benefits of Lexical Scoping

| Concept    | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| `clarity & predictability`    | Variable scope is determined by the code’s structure rather than its runtime behavior.            |
| `Encapsulation` | Allows inner function to reassign an enclosing variable |
| `Closures` | Made possible by lexical scoping, enables currying, memoization, and event handling. |


## Closure

A closure is the mechanism where an inner function keeps access to variables from an enclosing function even after the outer function has finished. (persisting data)

```bash
# Lexical scoping :
determines where Python looks for variables

# Closure :
allows an inner function to retain access to enclosing variables 
after the outer function has finished
```

## nonlocal
| Concept    | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| Closure    | Inner function remembers enclosing variables            |
| `nonlocal` | Allows inner function to reassign an enclosing variable |

### Why is global forbidden, but nonlocal allowed ?</br>
Minimize the use of global variables to prevent unintended variable shadowing and maintain clean code.

*Variable Shadowing*: Variable shadowing occurs when a variable declared within a nested scope has the same name as a variable in its outer scope, potentially leading to confusion and unintended behavior.


## functools

### reduce
reduce() - Applies a function cumulatively to the elements of an iterable and returns a single final value. 

### partial
A partial function in Python is a new function created from an existing function by pre-filling some of its arguments.
power and elemtn defined - target not defined

### lru_cache

Memoization is a caching strategy for avoiding repeated computation.

An LRU (Least Recently Used) cache is a data structure that stores a limited number of items and deletes the item that has not been used for the longest time when new space is needed

````
@lru_cache(maxsize=128, typed=False)
````

maxsize: Maximum number of function results stored in the cache. The default value is 128. Use None for an unlimited cache size.
typed: If True, arguments of different types are cached separately. For example, f(3) and f(3.0) are treated as different calls.

### signledispatch

A Python decorator that lets you define different versions of the same function depending on the type of its first argument.

It is similar to a limited form of *function overloading*

## Ex 5 - decorator functions

A decorator function is a function that takes another function, adds or changes some behavior, and returns a new function.

````bash
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")

    return wrapper
````
## @staticmethod
The @staticmethod decorator creates methods that don't need self or the class. They work like regular functions but belong to the class.

## fucntools - wraps

@wraps(func)

means:

"This wrapper is standing in for func, so keep func's name and information."