

import time
import socket

if __name__ == "__main__":

    req = 'GET /large/wangwang.exe HTTP/1.0\r\n'    \
          'User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5\r\n'  \
          'Host: 10.235.163.4:8080\r\n' \
          'Range: bytes=1096890-3096896\r\n' \
          'Accept: */*\r\n\r\n'

    address = ('127.0.0.1', 8080)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(address)

    sk.send(req)

    slen = 0
    fh = open('file.txt', 'wb')

    while True:

        res = sk.recv(1024*4)

        if res:
            slen += len(res)
            fh.write(res)
        else:
            break

        print slen
#        time.sleep(1)

    sk.close()
    fh.close()

    print slen

