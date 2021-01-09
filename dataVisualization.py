import matplotlib.pyplot as plt
import pandas as pd


sample_data = pd.read_csv("DHANMONDI_DATASETS\WorkSheet1.csv")
# plt.plot(sample_data.duration, sample_data.state, 'o')
# print(sample_data)
# plt.show()
labels = sample_data.state
values = sample_data.duration
explode = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
           0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
plt.show()
