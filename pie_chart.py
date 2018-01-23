import matplotlib.pyplot as plt

languages = [32, 21, 18, 12]
lang = ['pyhton', 'java', 'cpp', 'C']
shade = ['r','pink','orange','green']

plt.pie(
        languages,
        labels = lang,
        colors = shade,
        startangle = 90,
        shadow = True,
        explode = (.05,0.0,0.0,0.0),
        autopct = ('%1.1f%%'),
       )

plt.title('Scope of languages')
plt.show()
