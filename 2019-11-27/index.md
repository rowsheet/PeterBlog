# 2019-11-27

# Everything you need to know about Python:

### Entry-points and Imports:

Python files can be used in two ways:

1. As the main file.
2. As a module used by another file.

### As the main file:

**Takeaway:**

Use `if __name__ == "__main__"` if you're running this file directly. Everything inside this condition is the entry-point of the program.

**Notes:**

This is the most basic way to run a python file. Commands anywhere that's not in a function will be run when this file is called.

File: `one.py`

	# one.py
    print("This was called from one.py")
    
    def foo():
        print("Calling foo()")
    
    if __name__ == "__main__":
        print("This was called from one.py, inside __main__")

Run: `one.py`

    $ python one.py
    This was called from one.py
    This was called from one.py, inside __main__

Notice that `Calling foo()` was never printed because `foo()` was never called in the block under `if __name__ == "__main__"`. This block is the if condition that is only true if this file was called directly.

### As a module used by another file.

**Takeaway**:

Import Python code by calling `import foo` for a file *in the same directory* in a file called `foo.py`. [Python sucks at relative imports](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time) (imports from directories above or bellow) so make sure to [install your modules](https://stackoverflow.com/questions/4933224/how-to-install-a-python-library-manually) (either using `python setup.py install` or `pip install [some_module]`) if you want to use them in any way other then helper files in same directory as your entry-point.**

**Notes:**

We can also call Python code as modules. Here's an example of a file called `use_one.py` importing the file `one.py` that's in the same directory. First, we import it as a `module` (that's what it's called in Python), and then we can call methods of that module.

File: `use_one.py`

	# use_one.py
	
    # Import the file `one.py`
    import one
    
    # Call the function `foo()` in the file `one.py`
    one.foo()

Run: `use_one.py`

	$ python use_one.py
    This was called from one.py
    Calling foo()

Notice in this run, `Calling foo()` was printed because `foo()` was called. But we can't just call `foo()` directly. It's not in the global scope of the runtime of `use_one.py`, so we have to call it from the module `one` (file `one.py`).

Also notice that `This was called from one.py` was still called. This was called because when we import `one.py` (by calling `import one`), anything that's not in a function or condition is always called.
