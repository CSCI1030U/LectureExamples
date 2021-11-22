import matplotlib.pyplot as plt 
import numpy as np

# Line plots
revenue = [17.1, 22.0, 33.5, 11.0, 28.5, 40.0]
expenses = [21.0, 21.0, 25.5, 23.0, 22.0, 26.0]
years = [2015, 2016, 2017, 2018, 2019, 2020]
rev = plt.plot(years, revenue, 'b--')
exp = plt.plot(years, expenses, 'r:')
plt.title('Revenue vs. Expenses (2015-2020)')
plt.xlabel('Year')
plt.ylabel('Expenses/Revenue')
plt.axis([2015, 2020, 0, 40])
# plt.semilogx()
# plt.semilogy()
plt.grid(True)
plt.show()

x_values = np.arange(0.0, 10.0, 0.1)
squares = plt.plot(x_values, x_values ** 2, 'r-')
cubes = plt.plot(x_values, x_values ** 3, 'm-')
plt.setp(cubes, linewidth=2.0, marker='o')
figure = plt.gcf()
figure.set_size_inches(5.0, 8.0)
figure.savefig('plots/squares_and_cubes.png', dpi=400)
plt.show()

# Scatter plots
rev = plt.plot(years, revenue, 'b.')
exp = plt.plot(years, expenses, 'r+')
plt.title('Revenue vs. Expenses (2015-2020)')
plt.xlabel('Year')
plt.ylabel('Expenses/Revenue')
plt.axis([2015, 2020, 0, 40])
# plt.semilogx()
# plt.semilogy()
plt.grid(True)
plt.show()

# Histograms
grades = 65.0 + 15.0 * np.random.randn(10000)
plt.hist(grades, 25, facecolor='r')
plt.show()

# Bar charts
x_values = np.arange(0, 6, 1)
width = 0.3
rev = plt.bar(x_values, revenue, width, color='b')
exp = plt.bar(x_values+width, expenses, width, color='r')
plt.legend((rev[0],exp[0]), ('Revenue', 'Expense'))
plt.show()

# Pie charts

