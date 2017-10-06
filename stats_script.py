# stats_script.py

import numpy as np
# import matplotlib.pyplot as plt
import scipy.stats as ss

filename = input("Enter the filename to process: ")
output_file = filename[:-4] + "stats.csv"

scores_file = open(filename, 'r')
stats_file = open(output_file, 'w')

stats_file.write("Test,#Students,Min,Max,Mean,StandDev\n")

for line in scores_file:
	values = line.split(',')

	scores = []
	for i in range(1, len(values)):
		scores.append(int(values[i]))

	desc = ss.describe(scores)
	data = [desc[0], desc[1][0], desc[1][1], desc[2], (desc[3] ** (1/2))]

	data_string = values[0] + ","
	for data_point in range(len(data)):
		data_string = data_string + "{:.2f}".format((data[data_point])) + ","

	stats_file.write(data_string[:len(data_string) - 1] + "\n")

scores_file.close()
stats_file.close()