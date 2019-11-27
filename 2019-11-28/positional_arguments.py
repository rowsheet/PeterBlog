# positional_arguments.py

def foo(one, two, three):
    print("your params were:")
    print("one: " + one)
    print("two: " + two)
    print("three: " + three)


if __name__ == "__main__":
    foo("ONE", "TWO", "THREE")
    # Missing possitional arguments will cause an error.
    # foo("ONE", "TWO") # <-- This will cause an error!
