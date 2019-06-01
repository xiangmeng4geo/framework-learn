from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from thrift_learn.python.rpc.service import AddService

if __name__ == '__main__':
    transport = TSocket.TSocket("localhost", 9090)

    transport = TTransport.TBufferedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = AddService.Client(protocol)
    transport.open()
    print(client.add(2, 3))
    transport.close()
