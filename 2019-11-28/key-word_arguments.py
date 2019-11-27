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
