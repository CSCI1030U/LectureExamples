# practice


# coding exercise 1 (output to CSV format)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]


# coding exercise 2 (output 1/n for all n in the list [5,4,3,2,1,0])


# coding exercise 3 (test class for Student)

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

