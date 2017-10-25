# quick_stats.py

import scipy.stats as ss

scores = [100, 100, 100, 100, 92, 90, 88, 78, 76, 69, 67, 65]

headings = ["#Students","Min","Max","Mean","StandDev"]

desc = ss.describe(scores)
data = [desc[0], desc[1][0], desc[1][1], desc[2], (desc[3] ** (1/2))]

for i in range(len(data)):
    print(headings[i] + ": " + "{:.2f}".format((data[i])))