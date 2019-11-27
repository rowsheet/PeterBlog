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
