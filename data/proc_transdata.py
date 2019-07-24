#!/usr/bin/python2.7
#-*- coding:utf8 -*-
import json
from random import randint, sample
import time
from datetime import datetime, timedelta
from hashlib import md5

adm = 'system'


def make_trans(trans_num, owner, user):
    
    users = [owner] + sample(user, trans_num)
    start = int(time.mktime(time.strptime('2018-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")))
    end = int(time.mktime(time.strptime('2019-04-01 00:00:00', "%Y-%m-%d %H:%M:%S")))
    transtimes = [randint(start, end) for _ in range(trans_num+1)]
    transtimes.sort()
    trans = []
    for index in xrange(trans_num):

        one = {}
        one['senderID'] = users[index]
        one['receiverID'] = users[index+1]
        one['transtime'] = datetime.fromtimestamp(transtimes[index]).strftime("%Y-%m-%d %H:%M:%S")
        trans.append(one)
    
    return trans




if __name__ == '__main__':
    
    device = {}
    for one in open('devs.txt'):

        info = json.loads(one.rstrip('\r\n'))
        #device[info['deviceID']] = [info['buytime'], info['endtime']]
        device[info['deviceID']] = info['owner']
    print len(device)
    
    user = []
    for one in open('users.txt'):

        info = json.loads(one.rstrip('\r\n'))
        user.append(info['userID'])
    print len(user)
    
    fw = open('trans.txt', 'w')
    transinfo = []
    idx = 0L
    for deviceID in xrange(80000):
        
        trans_num = randint(0, 100)
        deviceID = 'DEV'+str(deviceID) 
        for item in make_trans(trans_num, device[deviceID], user):
            
            one = {}
            one['deviceID'] = deviceID
            one['senderID'] = item['senderID']
            one['receiverID'] = item['receiverID']
            one['transtime'] = item['transtime']
            #one['transHash'] = md5(json.dumps(one)).hexdigest()
            one['transID'] = idx
            #transinfo.append(one)
            idx += 1
            fw.write('%s\n' % json.dumps(one, ensure_ascii=False))
    fw.close()
    '''
    print len(transinfo)
    transinfo.sort(key = lambda x:x['transID'])
    with open('t_trans.txt', 'w') as f:
        
        for one in transinfo:

            f.write('%s\n' % json.dumps(one, ensure_ascii=False))


    '''   
    print 'done'
    exit(0)
