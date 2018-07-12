import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

Map = pd.read_csv('map.csv', header=None)
Moves = pd.read_csv('movements.csv', header=None).values[0, :]

max_x, max_y = np.shape(Map)
max_moves = len(Moves)
for i in range(max_x):
    for j in range(max_y):
        start_x, start_y = i, j
        current_x = start_x
        current_y = start_y
        print(current_x, current_y)
        icounter = 0;
        x_path = []
        y_path = []
        for m in Moves:
            if current_y < 0 or current_y > 19 or current_x<0 or current_x>19:
                print('failed / out of map')
                break
            if Map.loc[current_x, current_y] == 1:
                print('failed / not in water')
                break
            x_path.append(current_x)
            y_path.append(current_y)
            icounter += 1
            if m == 'N': current_x -= 1
            elif m == 'S': current_x += 1
            elif m == 'E': current_y += 1
            elif m == 'W': current_y -= 1
        if icounter == max_moves:
            print('possible option with ending points {}, {}'.format(current_x, current_y))
            final_x_path = x_path
            final_y_path = y_path


corresponding_location_on_map = []
for i in range(max_moves):
    corresponding_location_on_map.append(Map.loc[final_x_path[i], final_y_path[i]])

print(Moves)
print(final_x_path)
print(final_y_path)
print(corresponding_location_on_map)


#**** Visualization
plt.ion()
fig = plt.figure()
plt.rcParams['axes.facecolor'] = 'lightblue'

# plot the map
for i in range(max_x):
    for j in range(max_y):
        if Map.loc[i, j] == 1:
            plt.text(j, -1 * i, '1', fontsize=10)


# plot the path
for i in range(max_moves):
    #fig.clf()  # clear the figure
    plt.xlim(-1, 20)
    plt.ylim(-20, 1)
    plt.text(final_y_path[i], -1*final_x_path[i], Moves[i], fontsize=10)
    fig.canvas.draw()
    time.sleep(1)


