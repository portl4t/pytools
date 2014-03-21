

import os
import sys
import urllib
import time
import socket


if __name__ == "__main__":

    socket.setdefaulttimeout(180000)

    url = 'http://10.235.163.4:8080/large/wangwang.exe'

    sk = urllib.urlopen(url)

    slen = 0

    fh = open('file.txt', 'wb')
    print time.time()

    while True:
        ss = sk.read(80*1024)
        if ss:
            slen += len(ss)
            print slen
            fh.write(ss)
            time.sleep(1)
        else:
            break;

    sk.close()
    fh.close()
    print time.time()

    print '~~~~ finish ~~~~'

