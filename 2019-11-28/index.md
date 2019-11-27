# 2019-11-28

### Function parameters:

Functions and parameters can be defined an called in three ways.

1. Positional arguments.
2. Names arguments.
3. Key-word arguments (`kwargs`)

### Positional arguments:

Positional arguments are the simplest way to call functions.

File: `positional_arguments.py`

    # positional_arguments.py
    
    def foo(one, two, three):
        print("your params were:")
        print("one: " + one)
        print("two: " + two)
        print("three: " + three)
    if __name__ == "__main__":
	    foo("ONE", "TWO", "THREE")

Run: `positional_arguments.py`    
    
    $ python positional_arguments.py
    your params were:
    one: ONE
    two: TWO
    three: THREE

Note that missing positional arguments will cause an error:

	foo("ONE", "TWO") # <-- This will cause an error!

### Named Arguments:

File: `named_arguments.py`

    # positional_arguments.py
    
    def foo(one=None, two="Default Two Value", three=None):
        print("your params were:")
        # Make sure to type cast what you print in case type
        # parameter is not a string (i.e. None).
        print("one: " + str(one))
        print("two: " + str(two))
        print("three: " + str(three))
    
    
    if __name__ == "__main__":
    
	    # Notice how we pass parameters with variables names.
        print("Calling foo() with all params.")
        foo(one="ONE", two="TWO", three="THREE")
        
        # Notice how we don't need to pass all parameters.
        print("Calling foo() with two missing params.")
        foo(one="ONE")
        
        # Notice how paramters are out-of-order.
        print("Calling foo() with out-of-order params.")
	    foo(three="THREE", one="ONE", two="TWO")

Run: `named_arguments.py`

    $ python named_arguments.py
    Calling foo() with all params.
    your params were:
    one: ONE
    two: TWO
    three: THREE
    Calling foo() with two missing params.
    your params were:
    one: ONE
    two: Default Two Value
    three: None
    Calling foo() with out-of-order params.
    your params were:
    one: ONE
    two: TWO
    three: THREE

Notice that with named arguments, we call a function with parameters in **any order** as all as not pass them at all by specifying **default values**.

In the case above, all the default values were either a string or `None` (Python's version of *NULL*). This is helpful when we might call a function but not require all arguments to be passed; instead of passing `None` for params when we don't need them, we can define `None` at the definition and not pass it when calling the function).

### Key-word Arguments `kwargs`

File: `key-word_arguments.py`

    # positional_arguments.py
    
    def foo(**kwargs):
        print("your params were:")
    
        # `kwargs` is a Dictionary.
        # Note that attempting to fetch a value that might not be provided
        # would result in a key-error, so it's better to use `kwargs.get(key)`
        # instead of kwargs[key].
        one = kwargs.get("one")
        two = kwargs.get("two")
        three= kwargs.get("three")
    
        # Make sure to type cast what you print in case type
        # parameter is not a string (i.e. None).
        print("one: " + str(one))
        print("two: " + str(two))
        print("three: " + str(three))
    
    
    if __name__ == "__main__":
    
        # Notice how we can call foo() but define the key-value arguments
        # in a dictionary outside of the function.
        print("Calling foo() with parameters dictionary.")
        params = {
            "one": "ONE",
            "two": "TWO",
            "three": "THREE",
        }
        foo(**params)
    
        # Notice that normal named-arguments are also valid when defining
        # functions with key-word arguments.
        print("Calling foo() with named arguments.")
        foo(one="ONE", two="TWO")

Run: `key-word_arguments.py`

    $ python key-word_arguments.py
    Calling foo() with parameters dictionary.
    your params were:
    one: ONE
    two: TWO
    three: THREE
    Calling foo() with named arguments.
    your params were:
    one: ONE
    two: TWO
    three: None

Notice that in key-word argument functions, we can pass a `dict` (Python dictionary) of values that we define outside of the function. Also notice that named arguments *still work* for functions with key-word arguments.

Functions that use `**kwargs` have Pros and Cons.

***Pros***: Calling functions may be more readable when parameters may be long, complex, and require being built under conditional.
***Cons***: Reading the function definition is less readable.

In general, you should use `kwargs` when the function you're calling has complex parameters.

### When to use `kwargs` (vs) *named-arguments* (vs) *positional-arguments*.
Another rule of thumb for maintainability would be:

Use **`kwargs`** when:

 - writing functions with **complex, optional arguments** 
 - you want to ***maintain the readability** of the **function call***
 - Example: (building heavily off a function used in many places).

Use **named arguments** when:
 - writing functions with **complex, optional arguments**
 - you want to ***maintain the readability** of the **function definition***
 - Example: (functions that are only used once or twice, i.e. as helper functions)

Use **positional arguments** when:
 -  writing functions with **simple, obvious arguments**
  - writing functions where arguments are **required and always pass**
  - Example: functions like `login(username, password)`.
