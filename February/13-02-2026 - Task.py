import numpy as np

temp_list = [28, 32, 30, 37, 36, 38]
temp_array = np.array(temp_list)

max_temp = np.max(temp_array)
min_temp = np.min(temp_array)
avg_temp = np.mean(temp_array)
last_three = temp_array[-3:]

print("Temperatures:", temp_array)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Average Temperature:", avg_temp)
print("Last 3 days:", last_three)