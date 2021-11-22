import matplotlib.pyplot as plt
import numpy as np

# Line plots
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_revenue = [2.8, 2.2, 3.1, 3.8, 4.1, 3.2]
expenses = [2.0, 3.0, 2.5, 2.0, 2.1, 2.9]

sales_plot = plt.plot(months, sales_revenue, 'b--')
plt.setp(sales_plot, linestyle=':', color='#606060', marker='+')
plt.plot(months, expenses, 'r-')
plt.axis([0, 5, 0, 4.5])
# plt.semilogx()
# plt.semilogy()
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Revenue/Expenses ($millions)')
plt.title('First Half 2021 - Revenue/Expenses Report')
plt.show()

x_values = np.arange(-1, 1.01, 0.05)
plt.plot(x_values, x_values ** 2, 'r-')
plt.plot(x_values, x_values ** 3, 'b-')
plt.plot(x_values, x_values ** 4, 'g-')
plt.show()

# Scatter plots
plt.plot(months, sales_revenue, 'bs')
plt.plot(months, expenses, 'ro')
plt.axis([0, 5, 0, 4.5])
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Revenue/Expenses ($millions)')
plt.title('First Half 2021 - Revenue/Expenses Report')
figure = plt.gcf()
figure.set_size_inches(8.0, 5.0)
figure.savefig('plots/scatter.png', dpi=200)
plt.show()

# Histograms
horse_heights = 250 + 15 * np.random.randn(100000)
plt.hist(horse_heights, 150, color='g')
plt.show()

# Bar charts
x_values = np.arange(6)
bar_width = 0.35
s = plt.bar(x_values, sales_revenue, bar_width, color='b')
e = plt.bar(x_values + bar_width, expenses, bar_width, color='r')
plt.legend((s[0], e[0]), ('Sales', 'Expenses'))
plt.show()

# Pie charts

