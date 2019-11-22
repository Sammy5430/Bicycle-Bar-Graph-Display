import time

# HTML Hello World! example
############################################################################
# def web_page():
#   html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
#   <body><h1>Hello, World!</h1></body></html>"""
#   return html
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
#
# while True:
#   conn, addr = s.accept()
#   print('Got a connection from %s' % str(addr))
#   request = conn.recv(1024)
#   print('Content = %s' % str(request))
#   response = web_page()
#   conn.send(response)
#   conn.close()
############################################################################


# Output Control example
############################################################################
# count = 0
#
# def web_page():
#     if led.value() == 1:
#         gpio_state = "OFF"
#     else:
#         gpio_state = "ON"
#
#     html = """<html>
#     <head>
#     <title>ESP Web Server""" + str(count) + """</title>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <link rel="icon" href="data:,">
#     <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
#         h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
#         border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
#         .button2{background-color: #4286f4;}</style>
#     </head>
#
#     <body>
#     <h1>ESP Web Server</h1>
#         <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
#     <p><a href="/?led=on">
#     <button class="button">ON</button>
#     </a></p>
#     <p><a href="/?led=off">
#     <button class="button button2">OFF</button>
#     </a></p>
#     </body>
#     </html>"""
#     return html
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
#
# while True:
#     conn, addr = s.accept()
#     print('Got a connection from %s' % str(addr))
#     request = conn.recv(1024)
#     request = str(request)
#     print('Content = %s' % request)
#     count += 1
#     led_on = request.find('/?led=on')
#     led_off = request.find('/?led=off')
#     if led_on == 6:
#         print('LED ON')
#         led.value(0)
#     if led_off == 6:
#         print('LED OFF')
#         led.value(1)
#     response = web_page()
#     conn.send('HTTP/1.1 200 OK\n')
#     conn.send('Content-Type: text/html\n')
#     conn.send('Connection: close\n\n')
#     conn.sendall(response)
#     conn.close()

############################################################################

# Data values test
############################################################################
#
# uart_str = 'v = 7 c = 0 p = 8 r = 0 e = 13'
#
# # attempt using uart module
# ################################
# # uart.setup(0,115200,8,0,1,0)
# # uart.on("data", 32,
# # function(data)
# # uart.on("data")
# # end, 0)
# ################################
#
# #attempt using machine.UART
# #############################
# #############################
#
#
# # assuming input comes in the following format from MCU: V = 00 \n C = 00 \n P = 00... etc...
#
#
# def web_page():
#     global uart_str
#     # uart_str = uart.readline()
#     if uart_str is not '':
#         uart_arr = uart_str.split()
#
#         v_UART = uart_arr[uart_arr.index('v') + 2]
#         c_UART = uart_arr[uart_arr.index('c') + 2]
#         p_UART = uart_arr[uart_arr.index('p') + 2]
#         r_UART = uart_arr[uart_arr.index('r') + 2]
#         e_UART = uart_arr[uart_arr.index('e') + 2]
#
#     html = """<html>
#     <head>
#     <title>BBG-Display</title>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <link rel="icon" href="data:,">
#     </head>
#
#     <body>
#     <h1>Bicycle Bar Graph Display</h1>
#     <h2>Measurements</h2>
#     <p>
#     <strong>
#     Voltage: </strong>""" + v_UART + """ V
#     </p>
#     <p>
#     <strong>
#     Current: </strong>""" + c_UART + """ A
#     </p>
#     <p>
#     <strong>
#     Power: </strong>""" + p_UART + """ W
#     </p>
#     <p>
#     <strong>
#     RPM: </strong>""" + r_UART + """ RPM
#     </p>
#     <p>
#     <strong>
#     Energy: </strong>""" + e_UART + """ J
#     </p>
#     </body>
#     </html>"""
#     return html
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
#
# while True:
#
#     (UART(0, 115200).write('m'))            # works with msp to measure
#     (UART(0, 115200).write('t'))          # works with msp to transmit
#     print("\n\npliz work:  " + uart.readline())
#     conn, addr = s.accept()
#     print('Got a connection from %s\n' % str(addr))
#     request = conn.recv(1024)
#     request = str(request)
#     print('Content = %s\n' % request)
#     response = web_page()
#     conn.send(response)
#     # conn.send('HTTP/1.1 200 OK\n')
#     # conn.send('Content-Type: text/html\n')
#     # conn.send('Connection: close\n\n')
#     # conn.sendall(response)
#     conn.close()
##############################################################################################


# Custom webpage attempt
###########################################################################
uart_str = ""
str1 = None
str2 = None
str3 = None
str4 = None
str5 = None

# <meta http-equiv="refresh" content="3">

def web_page():
    html = """<html>
    <head>
    <title>BBG-Display Data</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link rel="icon" href="data:,">

    </head>

    <body>
    <h1>Bicycle Bar Graph Display Data:</h1>
        <p>UART data: <strong>""" + uart_str + """</strong></p>
    <p><a href="/?measure">
    <button class="button">Stop</button>
    </a></p>
    <p><a href="/?transmit">
    <button class="button button2">Auto-Refresh</button>
    </a></p>
    </body>
    </html>"""
    return html


uart = UART(0, 115200, 8, None, 1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# v = 10 c = 3 p = 9 r = 776 e =2


while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr) + "\n\n")
    request = conn.recv(1024)
    request = str(request)
    # print('Content = %s' % request + "\n\n")
    m_btn = request.find('/?measure')
    t_btn = request.find('/?transmit')

    print("find /?measure  " + str(m_btn))
    print("find /?transmit  " + str(t_btn))

    # if m_btn == 6:
    #     # uart.write('m')
    #     uart_str = ""
    # elif t_btn == 6:
    while str1 is None:
        uart.write('v')
        time.sleep(0.05)
        str1 = uart.read()
        time.sleep(0.05)
    while str2 is None:
        uart.write('w')
        time.sleep(0.05)
        str2 = uart.read()
        time.sleep(0.05)
    while str3 is None:
        uart.write('x')
        time.sleep(0.05)
        str3 = uart.read()
        time.sleep(0.05)
    while str4 is None:
        uart.write('y')
        time.sleep(0.05)
        str4 = uart.read()
        time.sleep(0.05)
    while str5 is None:
        uart.write('z')
        time.sleep(0.05)
        str5 = uart.read()
        time.sleep(0.05)
    uart.write('m')
    uart_str = str(str1).strip("b\'") + str(str2).strip("b\'") + str(str3).strip("b\'") + str(str4).strip("b\'") + \
               str(str5).strip("b\'")
    str1 = None
    str2 = None
    str3 = None
    str4 = None
    str5 = None
    print("\ndata read: " + uart_str)
    gc.collect()
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
###########################################################################
