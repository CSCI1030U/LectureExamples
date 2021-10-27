from pet import Pet

class Dog(Pet):
    def __lt__(self, another_dog):
        return self.get_mass() < another_dog.get_mass()
        # if self.get_mass() < another_dog.get_mass():
        #     return True 
        # else:
        #     return False