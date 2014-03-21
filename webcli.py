

import socket
import urllib
import urllib2
import httplib
import time


if __name__=='__main__':

    before = time.time()
    conn = httplib.HTTPConnection("10.235.163.4:8880")
    conn.request("GET", "/mm4.js")
#    conn.request("POST", "/cm/?action=prefetch&force=true", body=None, headers={})

    r1 = conn.getresponse()
    data = r1.read()

    print r1.status
    print r1.reason
    print r1.getheaders()

    conn.close()

    print data

    print '~~~ finish ~~~'

