class Pet:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass 
        self.birth_date = 'May 1, 2021'
    
    def get_name(self):
        return self.name 
    
    def set_name(self, new_name):
        self.name = new_name

    def get_mass(self):
        return self.mass 
    
    def set_mass(self, new_mass):
        self.mass = new_mass
    
    def get_birth_date(self):
        # could add code to convert from numeric date to string
        return self.birth_date