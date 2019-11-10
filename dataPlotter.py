import matplotlib.pyplot as plt
import random
from matplotlib import animation
import time

start_time = time.time()
x_axis = ['Voltage', 'Current', 'Power', 'RPM', 'Energy']

v_max = 0           # max voltage
c_max = 0           # max current
p_max = 0           # max power
r_max = 0           # max rpm
e_max = 0           # max energy
e_cal = 0           # max energy in calories
e_kwh = 0           # max energy in Kw/h

nf = 100  #Number of frames
count = 0

# Plot graphs
##############################################################
fig = plt.figure(figsize=(100, 100))
plt.suptitle("Elapsed Time: 00:00:00", fontsize=20)

v_plot = plt.subplot(151)
xv = plt.bar('Voltage', v_max, color='red')
plt.title('Volts')

c_plot = plt.subplot(152)
xc = plt.bar('Current', c_max, color='orange')
plt.title('Amperes')

p_plot = plt.subplot(153)
xp = plt.bar('Power', p_max, color='yellow')
plt.title('Watts')

r_plot = plt.subplot(154)
xe = plt.bar('RPM', r_max, color='green')
plt.title('RPM')

e_plot = plt.subplot(155)
xr = plt.bar('Energy', e_max, color='cyan')
plt.title('Joules')
##############################################################

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
    fig.suptitle("Elapsed Time: " + time.strftime("00:%M:%S", time.localtime(time.time() - start_time)), fontsize=20)
    height_vals = barlist()

    xv[0].set_height(height_vals['Voltage'][count])
    if height_vals['Voltage'][count] > v_max:
        v_max = height_vals['Voltage'][count]
        v_plot.axes.set_ylim(top=v_max+7)

    xc[0].set_height(height_vals['Current'][count])
    if height_vals['Current'][count] > c_max:
        c_max = height_vals['Current'][count]
        c_plot.axes.set_ylim(top=c_max+7)

    xp[0].set_height(height_vals['Power'][count])
    if height_vals['Power'][count] > p_max:
        p_max = height_vals['Power'][count]
        p_plot.axes.set_ylim(top=p_max+7)

    xr[0].set_height(height_vals['RPM'][count])
    if height_vals['RPM'][count] > r_max:
        r_max = height_vals['RPM'][count]
        r_plot.axes.set_ylim(top=r_max+7)

    xe[0].set_height(height_vals['Energy'][count])
    if height_vals['Energy'][count] > e_max:
        e_max = height_vals['Energy'][count]
        e_plot.axes.set_ylim(top=e_max+7)

    count = (count + 1) % (len(height_vals['Energy'])-1)


anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, interval=nf)
plt.show()

# Show Summary
###################################################################################################################
fig = plt.figure(figsize=(100, 100))
plt.suptitle("Elapsed Time: " + time.strftime("00:%M:%S", time.localtime(time.time() - start_time)), fontsize=20)

plt.subplot(171)
xv = plt.bar('Voltage', v_max+1, color='red')
plt.title('Volts')
plt.text(0, (v_max+1)/2, ""+str(v_max)+" V", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(172)
xc = plt.bar('Current', c_max+1, color='orange')
plt.title('Amperes')
plt.text(0, (c_max+1)/2, ""+str(c_max)+" A", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(173)
xp = plt.bar('Power', p_max+1, color='yellow')
plt.title('Watts')
plt.text(0, (p_max+1)/2, ""+str(p_max)+" W", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(174)
xe = plt.bar('RPM', r_max+1, color='green')
plt.title('RPM')
plt.text(0, (r_max+1)/2, ""+str(r_max)+" RPM", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(175)
xr = plt.bar('Energy', e_max+1, color='cyan')
plt.title('Joules')
plt.text(0, (e_max+1)/2, ""+str(e_max)+" J", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(176)
e_cal = e_max/4.184
xcal = plt.bar('Calories', e_cal+1, color='cyan')
plt.title('Energy (Cal)')
plt.text(0, (e_cal+1)/2, ""+str(e_cal)[0:str(e_cal).find('.')+3]+" cal", horizontalalignment='center',
         verticalalignment='center', fontsize=18)

plt.subplot(177)
e_kwh = (e_max/pow(3.6, 6)) * 0.22
xkwh = plt.bar('US Dollars', e_kwh+0.05, color='cyan')
plt.title('Energy ($)')
plt.text(0, (e_kwh+0.05)/2, "$ "+str(e_kwh)[0:str(e_kwh).find('.')+3], horizontalalignment='center',
         verticalalignment='center', fontsize=18)

plt.show()
###################################################################################################################
