
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.tcpserver import TCPServer


response = 'HTTP/1.1 400 Bad Request\r\nServer: ATS\r\nContent-Type: text/html\r\nCache-Control: no-cache\r\nConnection: close\r\n\r\n'
common_response = 'HTTP/1.1 200 OK\r\nServer: ATS\r\nContent-Type: text/html\r\nCache-Control: no-cache\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'


class RCServer(TCPServer):

    def handle_stream(self, stream, address):
        self._stream = stream
        self._stream.set_close_callback(self.on_close)
        self._read_line()

    def _read_line(self):
        self._stream.read_until('\r\n\r\n', self._handle_read)

    def _handle_read(self, data):
        print data
        self._stream.write(common_response)
        self._stream.close()

    def on_close(self):
        print 'close already'

if __name__=="__main__":
    http_server = RCServer()
    http_server.listen(8888)
    IOLoop.instance().start()

