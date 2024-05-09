import numpy as np
import test
import random




a1 = []
a2 = []
def f():
    global a1, a2
    arr = test.get_arr()
    quest = []
    ans = []
    rand_num = random.randint(0, len(arr) - 12)
    for i in range(rand_num, rand_num + 10):
        quest.append(arr[i])
    for j in range(rand_num + 10, rand_num + 12):
        ans.append(arr[j])
    a1.append(quest)
    a2.append(ans)
    return a1, a2
for i in range(100000):
    print(i)
    f()

print(a2)

try:
    data = np.load('my_data.npy')
    targets = np.load('my_targets.npy')
    a1 += data.tolist()
    a2 += targets.tolist()
except:
    pass

print(a1)
train_data = np.array(a1) # Входные данные (1000 примеров, 10 признаков)
train_targets = np.array(a2)  # Целевые значения (1000 примеров, 50 точек графика)
np.save('my_data.npy', train_data)
np.save('my_targets.npy', train_targets)
