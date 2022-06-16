#!/user/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink

class example_topo(Topo):
  def build(self):
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')
    s5 = self.addSwitch('s5')

    h1 = self.addHost('h1',mac='00:00:00:00:00:01', ip='no ip defined/24')
    h2 = self.addHost('h2',mac='00:00:00:00:00:02', ip='no ip defined/24')
    h3 = self.addHost('h3',mac='00:00:00:00:00:03', ip='no ip defined/24')
    h4 = self.addHost('h4',mac='00:00:00:00:00:04', ip='no ip defined/24')

    d1 = self.addHost('d1',mac='00:00:00:00:00:05', ip='no ip defined/24')
    d2 = self.addHost('d2',mac='00:00:00:00:00:06', ip='no ip defined/24')

    ccs1 = self.addHost('ccs1',mac='00:00:00:00:00:07', ip='10.3.3.1/29')
    ccs2 = self.addHost('ccs2',mac='00:00:00:00:00:08', ip='10.3.3.2/29')

    self.addLink(h1,s1, bw=3)
    self.addLink(h2,s1, bw=3)
    self.addLink(h3,s1, bw=3)
    self.addLink(h4,s1, bw=3)

    self.addLink(d1,s3, bw=3)
    self.addLink(d2,s3, bw=3)

    self.addLink(ccs1,s4, bw=10)
    self.addLink(ccs2,s5, bw=3)

    self.addLink(s1,s2, bw=3)
    self.addLink(s1,s3, bw=3)
    self.addLink(s1,s5, bw=3)
    self.addLink(s2,s4, bw=3)
    self.addLink(s3,s5, bw=3)
    self.addLink(s4,s5, bw=3)

def configure():
  topo = example_topo()
  net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
  net.start()

  h1, h2, h3, h4, d1, d2, ccs1, ccs2 = net.get('h1', 'h2', 'h3', 'h4', 'd1', 'd2', 'ccs1', 'ccs2')

  print("*** enable dhcpclient, and assign ip address ***")
  h1.cmd('sudo dhclient eth0')
  h2.cmd('sudo dhclient eth0')
  h3.cmd('sudo dhclient eth0')
  h4.cmd('sudo dhclient eth0')
  d1.cmd('sudo dhclient eth0')
  d2.cmd('sudo dhclient eth0')

  intf_h1 = net.get('h1').defaultIntf()
  intf_h2 = net.get('h2').defaultIntf()
  intf_h3 = net.get('h3').defaultIntf()
  intf_h4 = net.get('h4').defaultIntf()
  intf_d1 = net.get('d1').defaultIntf()
  intf_d2 = net.get('d2').defaultIntf()

  intf_h1.updateIP()
  intf_h2.updateIP()
  intf_h3.updateIP()
  intf_h4.updateIP()
  intf_d1.updateIP()
  intf_d2.updateIP()

  CLI(net)

  net.stop()

if __name__ == '__main__':
  configure()