import numpy
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

print(data)

#finding dimension of data
print(data.shape)

image-1=plt.plot(data)

#plotting data
plt.show(image-1)
