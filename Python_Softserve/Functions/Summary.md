## Summary

1. **Default parameters**:
    * Assign a value using `=`
2. **Regular parameters**:
    * Assign parameters name
3. If default parameters are mutable, they may be changed in every instance.
4. Variable-list arguments
    * *args
    * **kwargs
    * function (fargs, *args, **kwargs)
5. lambda function
    * one line function
    * anonymous function
    * One expression as a result
    * Usually used with map(), filter(), reduce(), etc
6. Recursive functions
    * Use recursion, if and only if on each iteration your task splits into two or more similar tasks.
7. First class functions
    * Ways to use functions
8. Nested Functions
    * Outer function -> Inner function
    * Encapsulation
9. LEGB rule
    * Local scope -> Enclosing Scope -> Global Scope -> Built-in
10. Closure
    * Under a nested function and inner function must refer to a value of the enclosing scope.
11. Factory functions
    * Function that creates another function
    * Follows the closure, LEGB rule.
12. Decorators
    * Takes a functions, changes its behaviour and returns it
    * Do not modify the original function
13. Generators
    * `yield`
        * Used returns an iterator
        * Does not start execution immediately
        * Iterate through items using next()
14. Generator expression
    * Similar to lambda, but for lists
    * Create one item at a time (lazy)
    * Memory efficient
    * Uses `()`, instead of `[]`


