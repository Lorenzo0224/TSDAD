import matplotlib.pyplot as plt
name_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
num_list = [232, 212, 198, 164,140,136,130,132,138,147]
x = list(range(len(num_list)))
plt.bar(x, num_list, fc='b')
plt.title('delta_t-ratio/Time')  # give plot a title
plt.xlabel('delta_t-ratio')  # make axis labels
plt.ylabel('Avg time(s)')
plt.legend()
plt.show()