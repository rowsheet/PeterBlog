# runtime_saftey.py
def will_run_ok():
    print("This function will run without error.")

def will_generate_error():
    print("This function will generate an error.")
    foo = "I'm a string"
    foo = foo + 1

will_run_ok()
will_generate_error()
