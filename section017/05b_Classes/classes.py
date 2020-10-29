class Assignment:
    # constructor - initialize the object's instance variables
    def __init__(self, name, asmt_topic, weight, due_date):
        # instance variables (variables)
        self.name = name
        self.topic = asmt_topic
        self.weight = weight 
        self.due_date = due_date
        self.score = 0

    # methods (functions)
    def set_score(self, score):
        self.score = score
    
    def __str__(self):
        return f'{self.name} - {self.topic} (weight: {self.weight})'

    def __lt__(self, other):
        return self.weight < other.weight


# this does two things:
# 1. Creates a new instance of Assignment
# 2. Initializes all of the instance variables of that new Assignment instance
asmt1 = Assignment('Assignment 1', 'Functions and classes', 10, 'November 3, 2020')
asmt1.set_score(10)
print(asmt1)

asmt2 = Assignment('Assignment 2', 'Regular expressions', 15, 'November 5, 2020')
if asmt1 < asmt2:
    print('asmt1 is less')
else:
    print('asmt1 is not less')
