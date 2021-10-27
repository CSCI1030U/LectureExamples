class Pet:
    def __init__(self, name, mass):
        self.name = name 
        self.mass = mass 
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_mass(self):
        return self.mass
    
    def set_mass(self, new_mass):
        self.mass = new_mass
    
    def __lt__(self, another_pet):
        return self.get_mass() < another_pet.get_mass()
        # if self.get_mass() < another_pet.get_mass():
        #     return True 
        # else:
        #     return False
