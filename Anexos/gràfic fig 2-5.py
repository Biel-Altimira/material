import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns






y = np.array([10, 10, 50, 25, 25, 15 ,70, 65])

x = np.array([1936, 1956, 1964, 1980, 1987, 1993, 2016, 2022])

plt.plot(x, y, "#0f6070", linewidth=3)


plt.xlabel('anys', color="gray")

plt.ylabel('desenvolupament', color="gray")



plt.text(1937, 20, "Etapa inicial", color="gray")

plt.text(1957, 53, "Primer estiu", color="gray")

plt.text(1972, 21, "Primaveres", color="gray")

plt.text(2014, 72, "Actual", color="gray")

plt.text(2019, 59, "Futur", color="gray")

plt.text(1985, 10, "Segon hivern", color="gray")

plt.text(1970, 30, "Primer hivern", color="gray", rotation=-59)






plt.yticks([])


sns.despine()
plt.show()
 
