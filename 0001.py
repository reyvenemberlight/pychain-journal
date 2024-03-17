import datetime
import time
import hashlib
import random
import string
import base64
import csv

path = "pg564.txt"
readfile = open(path, 'r')

# get the current date and time
m = hashlib.sha256()

def id_generator(size=210000, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

while True:
    now = str(datetime.datetime.now())
    line=readfile.readline()
    #print(readfile.readline())
    b64 = base64.b64encode(line.encode()).decode()
    #print(b64)
    m.update(b64.encode())
    #print(m.hexdigest())
    #strtest = id_generator().encode("ascii")
    #b64 = base64.b64encode(strtest).decode()
    #print(b64)
    #linetest = "** ll ##"
    #print(linetest)
    #print(m.hexdigest())
    #m.update(now.encode('utf-8'))
    #print(now)
    ##print(type(str(now)))
    #print(f'** {now}, {b64}, {m.hexdigest()}, **\n')
    block=open("block.csv", "a")
    blockline=f'** {now}, {b64}, {m.hexdigest()}, **\n'
    block.write(blockline)
    print(blockline)
    time.sleep(0.01)
