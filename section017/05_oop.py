class Student:
    def __init__(self, sid, first_name, last_name):
        self.sid = sid 
        self.first_name = first_name
        self.last_name = last_name
        self.registered_date = {
            'year': 2022,
            'month': 9,
            'day': 1,
        }
    
    def set_sid(self, new_sid): # mutator (setter)
        self.sid = new_sid

    def get_sid(self): # accessor (getter)
        return self.sid    

    def __eq__(self, other):
        return self.sid == other.sid and self.first_name == other.first_name and self.last_name == other.last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} (sid: {self.sid})'

student1 = Student('100000001', 'Giselle', 'LeClerc')

student1_copy = Student('100000001', 'Giselle', 'LeClerc')

student1_string = str(student1)
print(f'{student1_string = }')
print(student1 == student1_copy)

class Grad_Student(Student):
    def __init__(self, sid, first_name, last_name):
        super().__init__(sid, first_name, last_name)
        self.supervisor = None
    
    def set_supervisor(self, new_supervisor):
        self.supervisor = new_supervisor

student2 = Grad_Student('100000002', 'Rhonda', 'Brown')
student2.registered_date = {'year': 2023, 'month': 1, 'day': 1}

student2_copy = Grad_Student('100000002', 'Rhonda', 'Brown')

print(f'{str(student2) = }')
print(student2.registered_date)
print(student2 == student2_copy)

# exercise 5.1 (generator)

class Square_Generator:
    def __init__(self, start_num, end_num):
        self.next_num = start_num 
        self.end_num = end_num 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.next_num < self.end_num:
            current_num = self.next_num * self.next_num
            self.next_num += 1
            return current_num
        raise StopIteration()

for square in Square_Generator(5, 10):
    print(f'{square = }')

print(f'{list(Square_Generator(5, 10)) = }')

# exercise 5.2 (Shoe, Product)

class Product:
    def __init__(self, price, description):
        self.price = price 
        self.description = description
    
    def get_price(self):
        return self.price 
    
    def get_description(self):
        return self.description

class Shoe(Product):
    def __init__(self, brand, size, colour, price, description):
        super().__init__(price, description)

        self.brand = brand 
        self.size = size 
        self.colour = colour
    
    def get_brand(self):
        return self.brand 

    def get_size(self):
        return self.size 

    def get_colour(self):
        return self.colour 
    
    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __str__(self):
        return f'{self.brand} (size: {self.size}, colour: {self.colour}, price: {self.price})'

shoe1 = Shoe('Nike', 11, 'White', 189.99, 'Jordan Delta 3')
shoe2 = Shoe('Adidas', 13, 'White', 99.99, 'Grand Court Tennis')

print(f'{str(shoe1) = }')
print(f'{str(shoe2) = }')
print(shoe1 < shoe2)