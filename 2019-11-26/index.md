### 2019-11-26

# Everything you need to know about Python:
### Introduction

Python is an dynamically typed, interpreted language, which means it's doesn't use a compiler, but instead "compiles on the fly" using the Python [interpreter](https://en.wikipedia.org/wiki/Interpreter_%28computing%29) (thanks [Grace](https://en.wikipedia.org/wiki/Grace_Hopper)!).

This means that Pythons language (it's abstract syntax tree) is parsed, lexed, and executed at runtime. You don't need to pre-compile, build or directly execute anything like you would in C, Java, or even Rust.

File: `hello.py`

    # hello.py
    print("Hello from python!")
    
Run: `hello.py`

    $ python hello.py
    Hello from python!

### Dynamic Typing

Python is dynamically typed, which means variables can be declared as any variable type (`int`, `bool`, `string`) and even change at runtime (you can assign something to an `int`, and then re-assign something as a `string`). This [differs from languages like C or Java](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages) where once a variable is assigned as a type, it can't be re-assigned to any other type. In languages like Haskell, variables can't even change once their assigned because [variables in Haskell are immutable](https://mmhaskell.com/blog/2017/1/9/immutability-is-awesome)!

File: `dynamic.py`

    # dynamic.py
    
    # Assign the var `foo` to an integer.
    foo = 100
    print("foo (1):")
    print(foo)
    
    # Assign the var `foo` to a string.
    foo = "now I'm a string!"
    print("foo (2):")
    print(foo)

Run: `dynamic.py`

    $ python dynamic.py
    foo (1):
    100
    foo (2):
    now I'm a string!

### Type Saftey

Although Python is dynamically typed, it's not type safe, and misusing types can cause runtime errors. **Run-time errors** differ from **compile-time errors** because they occur after you've already starting *running* the code.

File: `type_saftey.py`

    # type_saftey.py
    foo = "I'm a string!"
    
    print("foo: (1)")
    print(foo)
    
    foo = foo + 1
    print("foo: (2)")
    print(foo)

Run: `type_saftey.py`

    $ python type_saftey.py
    foo: (1)
    I'm a string!
    Traceback (most recent call last):
      File "type_saftey.py", line 7, in <module>
        foo = foo + 1
    TypeError: can only concatenate str (not "int") to str

Notice this python code started running and failed at line 7 (after all the previous lines had already been executed). This differs from a language like Go-lang where a misuse of a variable of a certain type will be caught at *compile time* (before the program is ever run).

File: `type_saftey.go`:

    // type_saftey.go
    package main
    
    import "fmt"
    
    func main() {
    	foo := "I'm a string!"
    
    	fmt.Println("foo (1):")
    	fmt.Println(foo)
    
    	foo += 1
    	fmt.Println("foo (2):")
    	fmt.Println(foo)
    }

Run: `type_saftey.go`

    go run type_saftey.go
    # command-line-arguments
    ./type_saftey.go:12:6: cannot convert 1 (type untyped number) to type string
    ./type_saftey.go:12:6: invalid operation: foo += 1 (mismatched types string and int)

### Run-time Saftey

Python can be dangerous if you're not carful since the rest of your code may run perfectly fine, even though there might be an error that could crash your program, but are unaware of until it's called.

# Notes

### Static Typing

Python differs from *statically typed languages* like C, Java or Go:

File: `not_dynamic.go`

	// not_dynamic.go
    package main
    
    import "fmt"
    
    func main() {
        foo := 100
        fmt.Println("foo (1):")
        fmt.Println(foo)
        foo = "not I'm a string!"
        fmt.Println("foo (2):")
        fmt.Println(foo)
    }

Run: `go run not_dynamic.go`

    go run not_dynamic.go
    # command-line-arguments
    ./not_dynamic.go:10:8: cannot use "not I'm a string!" (type string) as type int in assignment

Trying to run this go-code, we get the error that we `cannot use "not I'm a string!" (type string) as type int in assignment`, meaning that once a variable is assigned as an `int`, it can't be re-assigned as a `string`.

Go-lang is also more strongly typed than a language like C, which is statically typed, but sometimes still allows for variable re-assignments. C has what is known as *weak static typing* and can be dangerous because of reasons like this as well as things like [use-after-free](https://cwe.mitre.org/data/definitions/416.html) vulnerabilities with [real-world consequences](https://en.wikipedia.org/wiki/Shellshock_%28software_bug%29). Before writing public code (code used by other people), you should read about how to write [secure C](http://web.mit.edu/6.s096/www/lecture/lecture03/secure-C.pdf). 

File: `unsafe.c`

    #include <stdio.h>
    
    int main(void) {
        int foo = 100;
        printf("foo (1): %i\n", foo);
        foo = "now I'm a string!";
        printf("foo (1): %i\n", foo);
    }

Run: `unsafe.c`

    $ gcc unsafe.c && ./a.out
    unsafe.c:6:9: warning: incompatible pointer to integer conversion assigning to 'int' from 'char [18]'
          [-Wint-conversion]
        foo = "now I'm a string!";
            ^ ~~~~~~~~~~~~~~~~~~~
    1 warning generated.
    foo (1): 100
    foo (1): 205455259

Here we compile our C code `unsafe.c` with the compiler `gcc` and run the executable file which `gcc` produces. If no other parameters are provided, the executable will be called `a.out` and we'll run it using the `./` command. We can run two commands (one after another) using `&&`, so the above command is actually running `gcc unsafe.c` and then `./a.out`.`

### `./a.out` and `$PATH`

In reality `./a.out` is specifying the binary when we are in the same directory. If we were a another director, but knew that `a.out` was at the the path `/some/example/path`, we could run `/some/example/path/a.out`. Also, if `a.out` was in our `$PATH`, we could just run in from any path since the `bash` variable `$PATH` is where `bash` searches for any binaries we might be running from any directory.
