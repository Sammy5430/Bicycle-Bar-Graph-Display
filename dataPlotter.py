#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import socket
import time
import os
import re
import sys
import tkinter as tk
import requests as req
from tkinter import ttk, PhotoImage
from matplotlib import animation
from matplotlib.widgets import Button
from datetime import datetime





# Await connection with ESP8266 Module
###############################################################################################################
first_exec = True
connected = False
frame_count = 0
test_counter = 0

while not connected:
    if first_exec:
        tk_window = tk.Tk()
        w = 480  # width for the Tk root
        h = 290  # height for the Tk root
        ws = tk_window.winfo_screenwidth()  # width of the screen
        hs = tk_window.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        tk_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk_window.title('Connecting...')
        tk_window.resizable(width=False, height=False)
        if frame_count < 10:
            index = '00' + str(frame_count)
        elif frame_count < 100:
            index = '0' + str(frame_count)
        else:
            index = str(frame_count)
        load_img = PhotoImage(file='resources/images/loading_frames/frame_' + index + '_delay-0.02s.gif')
        display = ttk.Label(tk_window, image=load_img)
        display.grid(column=0, row=0)
        load_msg = ttk.Label(tk_window, text='Establishing connection with ESP8266 module')
        load_msg.grid(column=0, row=1)
        frame_count += 1
        tk_window.update()
        tk_window.after(5)
        txt = 'Establishing connection with ESP8266 module'
        first_exec = False
    while frame_count <= 200:
        if frame_count < 10:
            index = '00' + str(frame_count)
        elif frame_count < 100:
            index = '0' + str(frame_count)
        else:
            index = str(frame_count)
        load_img = PhotoImage(file='resources/images/loading_frames/frame_' + index + '_delay-0.02s.gif')
        frame_count += 1
        display.configure(image=load_img)
        if frame_count % 51 == 0:
            txt = txt + '.'
        load_msg.configure(text=txt)
        tk_window.update()
        tk_window.after(5)
    frame_count = 0
    txt = 'Establishing connection with ESP8266 module'
    test_counter += 1

    # if connection successful (test up to 5 connections)
    try:
        socket.gethostbyaddr('192.168.4.1')
    except socket.herror:
        try:
            socket.gethostbyaddr('192.168.4.2')
        except socket.herror:
            try:
                socket.gethostbyaddr('192.168.4.3')
            except socket.herror:
                try:
                    socket.gethostbyaddr('192.168.4.4')
                except socket.herror:
                    try:
                        socket.gethostbyaddr('192.168.4.5')
                    except socket.herror:
                        connected = False
    else:
        connected = True
        load_msg.configure(text='Connected')
        while frame_count < 120:
            if frame_count < 10:
                index = '00' + str(frame_count)
            elif frame_count < 100:
                index = '0' + str(frame_count)
            else:
                index = str(frame_count)
            load_img = PhotoImage(file='resources/images/check_frames/frame_' + index + '_delay-0.02s.gif')
            display.configure(image=load_img)
            frame_count += 1
            tk_window.update()
            tk_window.after(8)
###############################################################################################################



resp = req.get('http://192.168.4.1')            # HTTP GET Response
html = resp.text                             # Get content as HTML String
txt = re.sub('<[^<]+?>', '', html)
html_arr = str(txt).split()

esp_v = html_arr[html_arr.index('Voltage:') + 1]
esp_c = html_arr[html_arr.index('Current:') + 1]
esp_p = html_arr[html_arr.index('Power:') + 1]
esp_r = html_arr[html_arr.index('RPM:') + 1]
esp_e = html_arr[html_arr.index('Energy:') + 1]

print('voltage: ' + esp_v + '\n')
print('current: ' + esp_c + '\n')
print('power: ' + esp_p + '\n')
print('rpm: ' + esp_r + '\n')
print('energy: ' + esp_e + '\n')






t_stamp = datetime.now().strftime('%B-%d-%Y %I:%M%p')
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
play = True

# Plot graphs
##############################################################
fig = plt.figure(figsize=(100, 100))
plt.suptitle("Elapsed Time: 00:00:00", fontsize=20)

v_plot = plt.subplot(151)
xv = plt.bar('Volts', v_max, color='#F1C40F')
plt.title('Voltage')

c_plot = plt.subplot(152)
xc = plt.bar('Amperes', c_max, color='#E67E22')
plt.title('Current')

p_plot = plt.subplot(153)
xp = plt.bar('Watts', p_max, color='#E74C3C')
plt.title('Power')

r_plot = plt.subplot(154)
xe = plt.bar('RPM', r_max, color='#8E44AD')
plt.title('RPM')

e_plot = plt.subplot(155)
xr = plt.bar('Joules', e_max, color='#3498DB')
plt.title('Energy')
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
    v_rand = random.randint(0, 25)
    c_rand = random.randint(0, 15)
    p_rand = v_rand * c_rand
    r_rand = random.randint(0, 200)
    e_rand = (counter + 1) / 2
    strtext = "" + x_axis[counter % 5] + ", " + str(v_rand) + "\n"
    f.write(strtext)
    strtext = "" + x_axis[(counter + 1) % 5] + ", " + str(c_rand) + "\n"
    f.write(strtext)
    strtext = "" + x_axis[(counter + 2) % 5] + ", " + str(p_rand) + "\n"
    f.write(strtext)
    strtext = "" + x_axis[(counter + 3) % 5] + ", " + str(r_rand) + "\n"
    f.write(strtext)
    strtext = "" + x_axis[(counter + 4) % 5] + ", " + str(e_rand) + "\n"
    f.write(strtext)
    counter += 5
f.close()
###################################################################################


def reset(i):
    os.execl(sys.executable, sys.executable, *sys.argv)


def barlist():
    graph_data = open('testData.txt', 'r').read()       # dont need to read the whole file in every iteration
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
    try:
        socket.gethostbyaddr('192.168.4.1')
    except:
        plt.close()
        return
    else:
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
elapsed_time = time.strftime("00:%M:%S", time.localtime(time.time() - start_time))
plt.suptitle("Elapsed Time: " + elapsed_time, fontsize=20)

plt.subplot(171)
xv = plt.bar('Volts', v_max+1, color='#F1C40F')
plt.title('Voltage')
plt.text(0, (v_max+1)/2, ""+str(v_max)+" V", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(172)
xc = plt.bar('Amperes', c_max+1, color='#E67E22')
plt.title('Current')
plt.text(0, (c_max+1)/2, ""+str(c_max)+" A", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(173)
xp = plt.bar('Watts', p_max+1, color='#E74C3C')
plt.title('Power')
plt.text(0, (p_max+1)/2, ""+str(p_max)+" W", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(174)
xe = plt.bar('RPM', r_max+1, color='#8E44AD')
plt.title('RPM')
plt.text(0, (r_max+1)/2, ""+str(r_max)+" RPM", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(175)
xr = plt.bar('Joules', e_max+1, color='#3498DB')
plt.title('Energy')
plt.text(0, (e_max+1)/2, ""+str(e_max)+" J", horizontalalignment='center', verticalalignment='center', fontsize=18)

plt.subplot(176)
e_cal = e_max/4.184
xcal = plt.bar('Calories', e_cal+1, color='#1ABC9C')
plt.title('Energy (Cal)')
plt.text(0, (e_cal+1)/2, ""+str(e_cal)[0:str(e_cal).find('.')+3]+" cal", horizontalalignment='center',
         verticalalignment='center', fontsize=18)

plt.subplot(177)
e_kwh = (e_max/pow(3.6, 6)) * 0.22
xkwh = plt.bar('US Dollars', e_kwh+0.05, color='#2ECC71')
plt.title('Energy ($)')
plt.text(0, (e_kwh+0.05)/2, "$ "+str(e_kwh)[0:str(e_kwh).find('.')+3], horizontalalignment='center',
         verticalalignment='center', fontsize=18)

button_axis = plt.axes([0.4625, 0.025, 0.1, 0.05])
btn_restart = Button(button_axis, 'Restart', color='#AEB6BF', hovercolor='#85929E')
btn_restart.on_clicked(reset)

# add entry to log file
####################################################################################################################
try:
    log = open('resources/files/logfile.csv', 'x')
    log.close()
    log = open('resources/files/logfile.csv', 'w')
    log.write('Timestamp,Elapsed Time,Max Voltage(V),Max Current(A),Max Power(W),Max RPM(RPM),Max Energy(J)\n')
    log.close()
except:
    pass
log = open('resources/files/logfile.csv', 'a')
log.write(t_stamp+','+elapsed_time+','+str(v_max)+','+str(c_max)+','+str(p_max)+','+str(r_max)+','+str(e_max)+'\n')
log.close()
####################################################################################################################

plt.show()
###################################################################################################################
