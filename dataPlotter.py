import matplotlib.pyplot as plt
import random
from matplotlib import animation

x_axis = ['Voltage', 'Current', 'Power', 'RPM', 'Energy']
nf = 30  #Number of frames
fig = plt.figure(figsize=(15, 7))

plt.subplot(151)
xv = plt.bar('Voltage', 20, color='red')
plt.autoscale(enable=True, axis='y')
plt.title('Voltage (V)')

plt.subplot(152)
xc = plt.bar('Current', 30, color='orange')
plt.autoscale(enable=True, axis='y')
plt.title('Current (A)')

plt.subplot(153)
xp = plt.bar('Power', 40, color='yellow')
plt.autoscale(enable=True, axis='y')
plt.title('Power (W)')

plt.subplot(154)
xe = plt.bar('RPM', 30, color='green')
plt.autoscale(enable=True, axis='y')
plt.title('RPM')

plt.subplot(155)
xr = plt.bar('Energy', 20, color='cyan')
plt.autoscale(enable=True, axis='y')
plt.title('Energy (W/h)')

count = 0


#clear file
#############################################
f = open('testData.txt', 'w')
f.write('')
f.close()
#############################################


#populate file with random data
###################################################################################
counter = 0
f = open('testData.txt', 'a')
while counter < 1000:
    strtext = "" + x_axis[counter % 5] + ", " + str(random.randint(0, 25)) + "\n"
    f.write(strtext)
    counter += 1
f.close()
###################################################################################


def barlist():
    graph_data = open('testData.txt', 'r').read()       #dont need to read the whole file in every iteration
    lines = graph_data.split('\n')
    v_arr = []
    c_arr = []
    p_arr = []
    r_arr = []
    e_arr = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            if x == 'Voltage':
                v_arr.append(float(y))
            elif x == 'Current':
                c_arr.append(float(y))
            elif x == 'Power':
                p_arr.append(float(y))
            elif x == 'RPM':
                r_arr.append(float(y))
            elif x == 'Energy':
                e_arr.append(float(y))
    values = {'Voltage': v_arr,
              'Current': c_arr,
              'Power': p_arr,
              'RPM': r_arr,
              'Energy': e_arr}
    return values


def animate(i):
    global count, xv, xc, xp, xe, xr
    height_vals = barlist()
    xv[0].set_height(height_vals['Voltage'][count])
    xc[0].set_height(height_vals['Current'][count])
    xp[0].set_height(height_vals['Power'][count])
    xr[0].set_height(height_vals['RPM'][count])
    xe[0].set_height(height_vals['Energy'][count])
    count = (count + 1) % (len(height_vals['Energy'])-1)


anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, interval=nf)

plt.show()

