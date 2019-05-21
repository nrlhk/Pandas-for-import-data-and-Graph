import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Open csv data with pandas
data1 = pd.read_csv('datafifa.csv', delimiter = ',')

# 1st breakdown, classify Overall column >= 85 and < 85
data3 = data1[pd.to_numeric(data1.Overall) >= 85]
data4 = data1[pd.to_numeric(data1.Overall) < 85]
print(data3.Age.mean())
# 2nd breakdown, classify Age column <=25 and >25 for graph
x1 = data3.Age[data3.Age <= 25]
y1 = data3.Overall[data3.Age <= 25]
x2 = data4.Age[data4.Age <= 25]
y2 = data4.Overall[data4.Age <= 25]
x3 = data3.Age[data3.Age > 25]
y3 = data3.Overall[data3.Age > 25]
x4 = data4.Age[data4.Age > 25]
y4 = data4.Overall[data4.Age > 25]

# Mean of Age which Overall skills <8 5
data5 = data3.Age.describe()
x5 = [25.10] * 39
y5 = np.arange(85)[46:85]
# print(y5)
# print(data4.Overall.min())


# Plot
plt.plot(x1, y1, 'r.', label='A<=25 and O>= 85')
plt.plot(x2, y2, 'c.', label='A<=25 and O< 85')
plt.plot(x3, y3, 'b.', label='A>25 and O>= 85')
plt.plot(x4, y4, 'y.', label='A>25 and O< 85')
plt.plot(x5, y5, 'g--', label='mean of A with O <85')
plt.title('Age and Overall skills')
plt.xlabel('Age value')
plt.ylabel('Overall value')
plt.savefig('Grafik Age and Overall skills')
plt.legend()

plt.show()