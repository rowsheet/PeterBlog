from animal import Animal

class Dog(Animal):

    def __init__(self, given_name=None, age=None):
        super().__init__(**{
            "given_name": given_name,
            "age": age,
            "animal_type": "Dog",
            "scientific_name": "Canis lupus familiaris",
            "greeting": "Woof!"
        })

    def mark_territory(self):
        print("> Calling dog.mark_territory()...\n")
        self.greet()
        print("**%s is peeing on your lawn...\n" % self.given_name)
