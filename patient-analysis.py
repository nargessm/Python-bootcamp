import numpy
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

print(data)

#Print just the first row of data
print(data[0])

#finding dimension of data
print(data.shape)

image=plt.plot(data)

#plotting data
plt.show(image)
