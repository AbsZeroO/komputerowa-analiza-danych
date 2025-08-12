from matplotlib import pyplot as plt

import kSrednich as KS


WCSS = []
k = []

print("Iteracje: ")

for i in range(2, 11):
    WCSS.append(KS.kSrednichPLT(i, False)[0])
    print("Dla k = " + str(i) + " Iteracji: " + str(KS.kSrednichPLT(i, False)[1]))
    k.append(i)

print(WCSS)

plt.plot(k, WCSS,  linestyle='--', marker='o', color='b')
plt.legend()

KS.kSrednichPLT(3, True)

plt.show()

