import matplotlib.pyplot as plt

messi = [32,7,68,57,42,78,65,12,15,75,34]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Random figure')

plt.scatter(messi, snig, label='scattering points', marker='x', s=100 )

plt.legend()
plt.show()
