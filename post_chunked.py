

import sys
import time
import socket

if __name__ == "__main__":

    req = 'POST /pt/ HTTP/1.1\r\n'    \
          'User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5\r\n'  \
          'Host: 10.235.163.4:8080\r\n' \
          'Transfer-Encoding: chunked\r\n\r\n' \

    bs = 'you have got a way'

    address = ('10.235.163.4', 8080)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(address)

    sk.send(req)

    for i in range (0, 30):
        sk.send('%x\r\n' % len(bs))
        sk.send(bs)
        sk.send('\r\n')
#        time.sleep(0.1)

    sk.send('0\r\n\r\n')

    res = sk.recv(4096)

    sk.close()

    print res

