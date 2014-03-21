
import tornado.httpserver
import tornado.ioloop

##### sample response ####
"""
HTTP/1.1 200 OK
Expires: Sat, 14 Sep 2013 09:49:00 GMT
Date: Fri, 30 Aug 2013 09:49:00 GMT
Server: nginx/1.0.6
Content-Type: text/css
Last-Modified: Thu, 29 Aug 2013 12:39:09 GMT
Transfer-Encoding: chunked
Cache-Control: max-age=1296000
Content-Encoding: gzip
Age: 1
X-Via: 1.1 tg100:9080 (Cdn Cache Server V2.0)
Connection: keep-alive"""


def handle_request(request):

#    response =  \
#             "HTTP/1.1 200 OK\r\n"                              \
#             "Server: Tornado/1.0.6\r\n"                        \
#             "Content-Length: 190\r\n"                        \
#             "Content-Type: text/css\r\n"                       \
#             "Cache-Control: max-age=3600\r\n"                            \
#             "Connection: close\r\n"                            \
#             "\r\n" \
#             "aaaaaaaaaaaaaaaaaaa"
    response = 'HTTP/1.1 400 Bad Request\r\nServer: ATS\r\nContent-Type: text/html\r\nCache-Control: no-cache\r\nConnection: close\r\n\r\n'

    request.write(response)
    request.finish()


if __name__=="__main__":
    http_server = tornado.httpserver.HTTPServer(request_callback=handle_request, no_keep_alive=True)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()

