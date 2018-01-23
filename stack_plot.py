import matplotlib.pyplot as plt

snig = ['monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']
python = [7, 17, 27, 47, 57, 67, 87]
java = [5, 15, 25, 35, 45, 55, 65]
cpp = [1, 2, 3, 4, 5, 6, 7]
c = [2, 4, 6, 8, 10, 12, 14]

plt.plot([],[], label = 'pyhton',color='orange', linewidth = 3)
plt.plot([],[], label = 'java',color='green', linewidth = 3)
plt.plot([],[], label = 'cpp',color='r', linewidth = 3)
plt.plot([],[], label = 'c',color='pink', linewidth = 3)

plt.xlabel('Days of work')
plt.ylabel('Number of hours')
plt.title('Programming work')

plt.stackplot(snig, python,java,cpp,c, colors = ['orange','green','r','pink'])

plt.legend()
plt.show()
