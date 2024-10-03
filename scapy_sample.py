from scapy.contrib.mpls import MPLS
from scapy.layers.inet import IP, TCP, ICMP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether
from scapy.all import *


layer2 = Ether(src="00:00:04:03:02:01")
layer2.show()

layer3 = IP(dst="192.168.10.3")
layer3.show()

myipv6 = IPv6()
myipv6.show()

layer4 = TCP()
layer4.show()

load_contrib("mpls")
MPLS().show()
my_mpls = MPLS()

my_frame = layer2/layer3
my_frame.show()

# send=sendp(layer2/my_mpls/layer3/layer4)
#
results = sniff(count=2, prn=lambda x:x.summary)
results.show()
results.summary()

my_packet = results[0]
print(my_packet[Ether])
print(my_packet[Ether].src)
#
# p = sr1(IP(dst="192.168.10.3")/ICMP()/"Naila")
# p.show()
