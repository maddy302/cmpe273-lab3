#reference https://twistedmatrix.com/documents/current/core/howto/udp.html
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ClientDatagramprotocol(DatagramProtocol):
    strings = [b"Hello World!",b"Hahah"]
    xData="Hello World!"
    def startProtocol(self):
        self.transport.connect("127.0.0.1",7777)
        # print("enter the data to send")
        # while(1):
        #     self.x = input()
        #     self.sendData()
        self.sendData()
    
    def sendData(self):
        #Static array of data being sent
        # if len(self.strings)>0:
        #     datagram = self.strings.pop(0)
        #     self.transport.write(datagram)

        # else:
        #     reactor.stop()

        #get input dynamically and send
        if self.xData!="":
            self.transport.write(self.xData.encode())
        else:
            #self.transport.write(self.x.encode())
            print("Bye-Bye!!")
            reactor.stop()
        
    def datagramReceived(self, datagram, host):
        print('Ack from server : ', datagram.decode())
        #self.sendData()
        #while(1):
        self.xData = input()
        self.sendData()
        # if(self.xData!="n"):
        #     self.sendData()
        

def main():
    print("Enter the data to send - <Hit enter with no data> to exit")
    protocol = ClientDatagramprotocol()
    reactor.listenUDP(0,protocol)
    reactor.run()

if __name__=='__main__':
    main()