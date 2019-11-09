import matplotlib.pyplot as plt
import random
from matplotlib import animation
import time


start_time = time.time();
x_axis = ['Voltage', 'Current', 'Power', 'RPM', 'Energy']

v_max = 5           # max voltage
c_max = 5           # max current
p_max = 25          # max power
r_max = 5           # max rpm
e_max = 5           # max energy


nf = 100  #Number of frames



fig = plt.figure(figsize=(15, 7))
plt.suptitle("Elapsed Time", fontsize=20)

v_plot = plt.subplot(151)
xv = plt.bar('Voltage', v_max, color='red')
plt.title('Voltage (V)')

c_plot = plt.subplot(152)
xc = plt.bar('Current', c_max, color='orange')
plt.title('Current (A)')

p_plot = plt.subplot(153)
xp = plt.bar('Power', p_max, color='yellow')
plt.title('Power (W)')

r_plot = plt.subplot(154)
xe = plt.bar('RPM', r_max, color='green')
plt.title('RPM')

e_plot = plt.subplot(155)
xr = plt.bar('Energy', e_max, color='cyan')
plt.title('Energy (J)')

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
    global count, xv, xc, xp, xe, xr, v_max, c_max, p_max, r_max, e_max, v_plot, c_plot, p_plot, r_plot, e_plot
    fig.suptitle("Elapsed Time:" + time.strftime("00:%M:%S", time.localtime(time.time() - start_time)))
    height_vals = barlist()

    xv[0].set_height(height_vals['Voltage'][count])
    if height_vals['Voltage'][count] > v_max:
        v_max = height_vals['Voltage'][count]
        v_plot
        plt.ylim(top=v_max)

    xc[0].set_height(height_vals['Current'][count])


    xp[0].set_height(height_vals['Power'][count])


    xr[0].set_height(height_vals['RPM'][count])


    xe[0].set_height(height_vals['Energy'][count])


    count = (count + 1) % (len(height_vals['Energy'])-1)


anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, interval=nf)

plt.show()

