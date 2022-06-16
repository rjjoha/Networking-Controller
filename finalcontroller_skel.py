#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink

class final_topo(Topo):
  def build(self):
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make "h1-eth0" on this assignment to make sure all
    # packets are sent out that "h1-eth0")port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
    # h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='1.1.1.1/24', defaultRoute="h1-eth0")
    # h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='2.2.2.2/24', defaultRoute="h2-eth0")

    h1 = self.addHost('h1',mac='00:00:00:00:00:01', ip='10.1.1.1/24', defaultRoute="h1-eth0")
    h2 = self.addHost('h2',mac='00:00:00:00:00:02', ip='10.1.1.2/24', defaultRoute="h2-eth0")
    h3 = self.addHost('h3',mac='00:00:00:00:00:03', ip='10.1.1.3/24', defaultRoute="h3-eth0")
    h4 = self.addHost('h4',mac='00:00:00:00:00:04', ip='10.1.1.4/24', defaultRoute="h4-eth0")

    d1 = self.addHost('d1',mac='00:00:00:00:00:05', ip='10.2.2.1/24', defaultRoute="d1-eth0")
    d2 = self.addHost('d2',mac='00:00:00:00:00:06', ip='10.2.2.2/24', defaultRoute="d2-eth0")

    ccs1 = self.addHost('ccs1',mac='00:00:00:00:00:07', ip='10.3.3.1/29', defaultRoute="ccs1-eth0")
    ccs2 = self.addHost('ccs2',mac='00:00:00:00:00:08', ip='10.3.3.2/29', defaultRoute="ccs2-eth0")

    # Create a switch. No changes here from Lab1.
    # s1 = self.addSwitch('s1')

    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')
    s5 = self.addSwitch('s5')

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on
    # Host 2. This is representing the physical port on the switch or host that you are
    # connecting to.

    # IMPORTANT NOTES:
    # - One a single device, you can only use each port once! So, on s1, only 1 device can be
    #   plugged in to port1, only one device can be plugged in to port2, etc.
    # - On the "host" side of connections, you must make sure to always match the port you
    #   set as the default route when you created the device above. Usually, this means you
    #   should plug in to port 0 (since you set the default route to h#-eth0)

    # self.addLink(s1,h1, port1=8, port2=0)
    # self.addLink(s1,h2, port1=9, port2=0)

    self.addLink(h1,s1, port1=0, port2=7, bw=3)
    self.addLink(h2,s1, port1=0, port2=1, bw=3)
    self.addLink(h3,s1, port1=0, port2=2, bw=3)
    self.addLink(h4,s1, port1=0, port2=3, bw=3)

    self.addLink(d1,s3, port1=0, port2=1, bw=3)
    self.addLink(d2,s3, port1=0, port2=2, bw=3)

    self.addLink(ccs1,s4, port1=0, port2=2, bw=10)
    self.addLink(ccs2,s5, port1=0, port2=3, bw=3)

    self.addLink(s1,s2, port1=6, port2=2, bw=3)
    self.addLink(s1,s3, port1=4, port2=4, bw=3)
    self.addLink(s1,s5, port1=5, port2=1, bw=3)
    self.addLink(s2,s4, port1=1, port2=3, bw=3)
    self.addLink(s3,s5, port1=3, port2=4, bw=3)
    self.addLink(s4,s5, port1=1, port2=2, bw=3)

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController, link=TCLink)
  net.start()

  # h1, h2, h3, h4, d1, d2, ccs1, ccs2 = net.get('h1', 'h2', 'h3', 'h4', 'd1', 'd2', 'ccs1', 'ccs2')

  CLI(net)

  net.stop()

if __name__ == '__main__':
  configure()
