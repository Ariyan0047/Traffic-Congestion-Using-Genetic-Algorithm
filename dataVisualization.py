import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score


state1 = pd.read_csv("DHANMONDI_DATASETS/states/state1.csv")
time1 = sum(state1.time)
time2 = sum(state1.time2)
state1Time = time1 + time2
print("State 1: ", state1Time)

state2 = pd.read_csv("DHANMONDI_DATASETS/states/state2.csv")
time3 = sum(state2.time)
time4 = sum(state2.time2)
state2Time = time3 + time4
print("State 2: ", state2Time)

state3 = pd.read_csv("DHANMONDI_DATASETS/states/state3.csv")
time5 = sum(state3.time)
time6 = sum(state3.time2)
state3Time = time5 + time6
print("State 3: ", state3Time)

state4 = pd.read_csv("DHANMONDI_DATASETS/states/state4.csv")
time7 = sum(state4.time)
time8 = sum(state4.time2)
state4Time = time7 + time8
print("State 4: ", state4Time)


# y_pred = [149545075]
# y_true = [1414740, 659143, 1019490, 180848]
# print(accuracy_score(y_true, y_pred))
