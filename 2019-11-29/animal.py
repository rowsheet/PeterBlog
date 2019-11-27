class Animal:

    def __init__(self, **kwargs):
        self.animal_type = kwargs["animal_type"]
        self.scientific_name = kwargs["scientific_name"]
        self.given_name = kwargs["given_name"]
        self.age = kwargs["age"]
        self.greeting = kwargs["greeting"]
        print("Initializing a new %s..." % self.animal_type)

    def print_info(self):
        info = """\
    Animal Type:        %(animal_type)s
    Scientific Name:    %(scientific_name)s
    Given Name:         %(animal_type)s
    Age:                %(age)s
    Greeting:           %(greeting)s
        """ % {
            "animal_type": self.animal_type,
            "scientific_name": self.scientific_name,
            "animal_type": self.animal_type,
            "age": self.age,
            "greeting": self.greeting,
        }
        print(info)

    def greet(self):
        print("%(animal_type)s says:     %(greeting)s" % {
            "animal_type": self.animal_type,
            "greeting": self.greeting,
        })

    def poke(self):
        print("Poking %(animal_type)s..." % {
            "animal_type": self.animal_type,
        })
        self.greet()
