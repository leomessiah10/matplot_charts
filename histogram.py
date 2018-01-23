import matplotlib.pyplot as plt

messi = [32,45,57,79,87,56,88,23,67,90,43,56,43,97,68,57,42,78,65,12,15,75,34]
snig = [0,10,20,30,40,50,60,70,80,90,100]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Random figure')

plt.hist(messi, snig, histtype = 'bar', rwidth = 0.8)

plt.legend()
plt.show()
