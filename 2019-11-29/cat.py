from animal import Animal

class Cat(Animal):

    def __init__(self, given_name=None, age=None):
        super().__init__(**{
            "given_name": given_name,
            "age": age,
            "animal_type": "Cat",
            "scientific_name": "Felis catus",
            "greeting": "Meow..."
        })

    def get_hungry(self): 
        print("> Calling cat.get_hungry()...\n")
        self.greet()
        print("**%s is walking on your keyboard...\n" % self.given_name)
