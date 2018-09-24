#reference https://twistedmatrix.com/documents/current/core/howto/udp.html
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Hello(DatagramProtocol):
    print("listening to localhost:7777")
    def datagramReceived(self, datagram, address):
        print("Datagram from client "+str(address)+" :"+str(datagram.decode()))
        print("Notifying Client with ack!!")
        self.transport.write(datagram, address)

def main():
    reactor.listenUDP(7777, Hello())
    reactor.run()

if __name__ == '__main__':
    main()