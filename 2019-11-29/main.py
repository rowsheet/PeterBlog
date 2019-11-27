from dog import Dog
from cat import Cat

def log_main_event(msg):
    print("""\
--------------------------------------------------------
%s
--------------------------------------------------------
    """ % msg.upper())

if __name__ == "__main__":

    log_main_event("initialize characters...")

    doggo = Dog(given_name="Doggo",age=4)
    doggo.print_info()
    business_cat = Cat(given_name="Business Cat", age=1000)
    business_cat.print_info()

    log_main_event("make characters do things...")
            
    doggo.mark_territory()
    business_cat.get_hungry()
