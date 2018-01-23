import matplotlib.pyplot as plt

x, y = [2,4,6,8,10], [3,5,7,9,11]
x2, y2 = [2,4,6,8,10], [4,2,8,5,11]

plt.plot(x, y, label = 'snig')
plt.plot(x2, y2, label = 'messi')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Random figure')

plt.legend()
plt.show()
