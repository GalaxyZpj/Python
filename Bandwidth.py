import psutil, threading
from time import sleep
from os import system
down_speed = '0'
up_speed = '0'
def net_down_speed():
    while True:
        global down_speed
        global up_speed
        prev_up_data = psutil.net_io_counters(pernic=False, nowrap=True)[0]
        prev_down_data = psutil.net_io_counters(pernic=False, nowrap=True)[1]
        sleep(0.25)
        cur_up_data = psutil.net_io_counters(pernic=False, nowrap=True)[0]
        cur_down_data = psutil.net_io_counters(pernic=False, nowrap=True)[1]
        up_speed = ((cur_up_data - prev_up_data)/0.25)/(1024**2)
        down_speed = ((cur_down_data - prev_down_data)/0.25)/(1024**2)

def data_track():
    global down_speed
    uploaded_data = psutil.net_io_counters(pernic=False, nowrap=True)[0]
    downloaded_data = psutil.net_io_counters(pernic=False, nowrap=True)[1]
    while True:
        system('clear')
        up_data = psutil.net_io_counters(pernic=False, nowrap=True)[0]
        down_data = psutil.net_io_counters(pernic=False, nowrap=True)[1]
        up_data = (up_data - uploaded_data)/(1024**2)
        down_data = (down_data - downloaded_data)/(1024**2)
        print('Uploaded: {0:1.3} MB\nDownloaded: {1:1.3} MB\n'.format(up_data, down_data))
        print('Upload speed: {0:1.3} MB/s\nDownload speed: {1:1.3} MB/s' .format(up_speed, down_speed))
        sleep(0.25)

t1 = threading.Thread(target = net_down_speed)
t2 = threading.Thread(target = data_track)

t1.start()
t2.start()
