
import numpy as np
import random
import csv

a1 = list(range(1,101))
a2 = list(range(100,201))

#a3 = np.vstack([a1, a2])


with open("unique_macs.csv", "w") as f:

    writer = csv.writer(f)
    writer.writerow(["mac_id", "mac_adr"])

    for i in range(len(a1)):
        writer.writerow( [a1[i], a2[i]] )

a3 = list(np.random.randint(101, size=1000))
a4 = list(np.random.randint(101, size=1000))
a5 = list(np.random.randint(6000, size=1000))

with open("relationships.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["to_id", "from_id", "cnt"])

    for i in range(len(a3)):
        writer.writerow([a3[i], a4[i], a5[i]])


