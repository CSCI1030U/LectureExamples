class Printer:
    def __init__(self, is_colour, page_capacity):
        self.is_colour = is_colour 
        self.page_capacity = page_capacity
        self.print_queue = []
    
    def add_job(self, document):
        self.print_queue.append(document)

    def get_print_queue(self):
        return self.print_queue

class InkjetPrinter(Printer):
    def __init__(self, page_capacity, ink_level):
        Printer.__init__(self, True, page_capacity)
        self.ink_level = ink_level
    
    def get_ink_level(self):
        return self.ink_level

flobby = InkjetPrinter(500, 0.5)
flobby.add_job('Test page 1 2 3')
print(flobby.get_ink_level())
print(flobby.print_queue)

''' CSV file example:
100000000, Barb Smith, 68.5, C+
100000001, Rodrigo Alazar, 65.0, C
...
'''

sids = [100000000, 100000001, 100000002, 100000003]
names = ['Barb Smith', 'Rodrigo Alazar', 'Jeff Shaquees', 'Bob Ross']
marks = [68.5, 65.0, 25.0, 100.0]
grades = ['C+', 'C', 'F', 'A+']

with open('grades.csv', 'w') as output_file:
    for i in range(len(sids)):
        output_file.write(f'{sids[i]},{names[i]},{marks[i]},{grades[i]}\n')

with open('grades.csv', 'r') as input_file:
    for line in input_file:
        print(line, end='')

import json 
with open('movies.json', 'r') as input_json:
    movies = json.load(input_json)

print(movies[0]['name'])
with open('movies2.json', 'w') as output_json:
    json.dump(movies, output_json)

x = 8
y = 0
z = x / y  # generates an exception
