#!/usr/bin/python2.7
#-*- coding:utf8 -*-
import json
from random import randint
import time
from datetime import datetime, timedelta

colors = ['red', 'black', 'white', 'grey']
mems = ['8G', '16G', '32G', '64G', '128']
makes = ['HP','Lenovo','Mac','Acer','Dell','ASUS','SAMSUNG']

def make_time():
    
    start = time.mktime((2013, 1, 1, 0, 0, 0, 0, 0, 0))
    end = time.mktime((2019, 1, 1, 0, 0, 0, 0, 0, 0))
    t = randint(start, end)
    buytime = datetime.fromtimestamp(t)
    endtime = buytime + timedelta(days=365*3)
    return buytime.strftime("%Y-%m-%d %H:%M:%S"), endtime.strftime("%Y-%m-%d %H:%M:%S")




if __name__ == '__main__':
    
    deviceinfo = []
    for index in xrange(80000):
        
        one = {}
        one['deviceID'] = 'DEV'+str(index)
        #one['deviceInfo'] = {'deviceName':'device_'+str(index), 
        one['color'] = colors[randint(0, 3)]
        one['make'] = makes[randint(0,6)]
        one['model'] = str(randint(1111,9999))
        one['owner'] = 'USER'+str(randint(0,70000))

	deviceinfo.append(one)

    print len(deviceinfo)
    with open('devs.txt', 'w') as f:
        
        for one in deviceinfo:

            f.write('%s\n' % json.dumps(one, ensure_ascii=False))



    print 'done'
    exit(0)
