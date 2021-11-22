import matplotlib.pyplot as plt 
import numpy as np 

# Line plots
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales =    [1.2, 0.7, 2.1, 3.4, 2.3, 4.9]
expenses = [0.5, 1.1, 1.1, 0.8, 1.5, 1.0]
s = plt.plot(months, sales, 'b-')
e = plt.plot(months, expenses, 'r--')
plt.setp(e, linewidth='1.5', marker='o', color='#606060')
plt.title('Sales vs Expenses (Jan-Jun 2021)')
plt.xlabel('Month')
plt.ylabel('Sales/Expenses (million $)')
plt.axis([0, 5, 0, 5])
plt.grid(True)
# plt.semilogy()
# plt.semilogx()
plt.show()

x_values = np.arange(-1, 1.01, 0.1)
plt.plot(x_values, x_values ** 2, 'r-')
plt.plot(x_values, x_values ** 3, 'b-')
figure = plt.gcf()
figure.set_size_inches(8, 5)
figure.savefig('plots/quatratic_and_cubic.png', dpi=200)
plt.show()

# Scatter plots
s = plt.plot(months, sales, 'bo')
e = plt.plot(months, expenses, 'rs')
plt.title('Sales vs Expenses (Jan-Jun 2021)')
plt.xlabel('Month')
plt.ylabel('Sales/Expenses (million $)')
plt.axis([0, 5, 0, 5])
plt.grid(True)
plt.show()

# Histograms
squirrel_tail_lengths = 30 + 3 * np.random.randn(100000)
plt.hist(squirrel_tail_lengths, 100, facecolor='#a06000')
plt.show()

# Bar charts
x_positions = np.arange(6)
bar_width = 0.35
s = plt.bar(x_positions, sales, bar_width, color='b')
e = plt.bar(x_positions + bar_width, expenses, bar_width, color='r')
plt.legend((s[0], e[0]), ('Sales', 'Expenses'))
plt.show()

# Pie charts

labels = ('Biology', 'Forensics', 'Chemistry', 'Computer Science', 'Math', 'Physics')
counts = (84, 38, 68, 240, 21, 18)
colours = ('#E0BBE4', '#957DAD', '#D291BC', 'lightskyblue', '#FEC8D8', '#FFDFD3')
explode = (0, 0, 0, 0.1, 0, 0)
plt.pie(counts, explode=explode, labels=labels, colors=colours, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()