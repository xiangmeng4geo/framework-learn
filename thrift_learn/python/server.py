from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TMultiplexedProtocol, TBinaryProtocol

from thrift_learn.python.rpc.service import AddService


class AddServiceHandler(AddService.Iface):
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    handler = AddServiceHandler()
    processor = AddService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", 9090)
    trans_factory = TTransport.TBufferedTransportFactory()
    proto_factory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TThreadPoolServer(processor, transport, trans_factory, proto_factory)
    print("start server")
    server.serve()
