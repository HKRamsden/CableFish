#! /usr/bin/env python
#new comment

#to activate virtual environnment:
# % source packet_sniffer/bin/activate

#to run cablefish
# % sudo ./packet_sniffer/bin/python Documents/cableFish.py  

# Standard Imports
import sys
import time

# Specialized imports
from tkinter import *
from scapy.all import *
import scapy.all as scapy
from rich.console import Console
from rich.style import Style

console = Console()

# Styles
darkCyan = Style(color="#0094ab")  # dark cyan color

# Functions

# Function to sniff packets 
def sniff_packets():
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
    console.print("[#1dd3ef]            Enter Total Number of Packets to Sniff: [/#1dd3ef]")
    totalNum = int(input())
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")

    
    with console.status("                               Sniffing packets", spinner="shark"):
        time.sleep(2.0)
        packets = sniff(count=totalNum)
    console.print("[#0094ab]                  :fish: Finished Sniffing :fish:                       [/#0094ab]", style="bold underline")
    #console.print("                        :fish: Finished Sniffing :fish:")
    packets.show()
    
       
#function to scan port
def scan_port():
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")    
    console.print("[#1dd3ef]                    Enter Target IP Address: [/#1dd3ef]")
    IPAddress = input()
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")

    
    console.print("[#1dd3ef]           Enter Ports to Scan, Separate by Spaces: [/#1dd3ef]")
    portString = input()
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")

    portString = portString.split()
    ports = list(map(int, portString))
    #console.print(ports)
    console.print("")
    
    for port in ports:
        packet = IP(dst=IPAddress)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response: 
            if response[TCP].flags == "SA":
                console.print(f"[#0094ab]Port {port} is Open[/#0094ab]")
            elif response[TCP].flags == "RA":
                console.print(f"Port {port} is Closed")
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
    
def trace_route():
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
    console.print("[#1dd3ef]                        Enter Website: [/#1dd3ef]")   
    destination = input()
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")

    console.print("[#1dd3ef]                       Enter Max Hops: [/#1dd3ef]")

    max_hops = int(input())
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")

    
    ttl = 1
    while ttl <= max_hops: 
        # Create the ICMP Echo Request packet with the specified TTL 
        packet = IP(dst=destination, ttl=ttl) / ICMP() 
 
        # Send the packet and record the start time 
        start_time = time.time() 
        reply = sr1(packet, verbose=False, timeout=1) 
 
        if reply is None: 
            # No reply received, print a timeout message 
            print(f"{ttl}. ") 
        elif reply.type == 0: 
            # Echo Reply received, we've reached the destination 
            print(f"{ttl}. {reply.src}  {round((time.time() - start_time) * 1000, 2)} ms") 
            break 
        else: 
            # We've received a Time Exceeded message, continue to the next hop 
            print(f"{ttl}. {reply.src}  {round((time.time() - start_time) * 1000, 2)} ms") 
 
        ttl += 1   
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
 

def network_scan():
    console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
    
    request = scapy.ARP()
    request.pdst = '192.168.1.1/24'
    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request
         
    with console.status("                               Sending Packets", spinner="shark"):

        clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
        console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
        
    for element in clients:  
        console.print(f"[#114159]{element[1].psrc}      {element[1].hwsrc}[/#114159]")  
        console.print("[#0094ab]                                                                [/#0094ab]", style="bold underline")
    

    
def mainMenu():
    while True:
        console.print("")

        console.print("                   :fish: :desktop_computer:  [#114159]Select Options:[/#114159] :desktop_computer:  :fish:", style="bold")
        console.print("                  :fish: [#1dd3ef]Option 1: Sniff Packets [/#1dd3ef]:fish:")
        console.print("                   :desktop_computer:  [#0094ab]Option 2: Port Scans [/#0094ab]:desktop_computer:")
        console.print("                   :fish: [#1dd3ef]Option 3: Network Scan [/#1dd3ef]:fish:")
        console.print("                  :desktop_computer:  [#0094ab]Option 4: Trace Route [/#0094ab]:desktop_computer:")
        console.print("                      :fish: [#1dd3ef]Option 5: Exit [/#1dd3ef]:fish:")


        console.print("")
        console.print("[#0094ab]                       Enter Your Choice:                       [/#0094ab]", style="bold underline")

        # General Option Input 
        optionChoice = int(input())

        # Match case to handle user input
        # console.print("Your Choice: ", optionChoice)
        match optionChoice:
            case 1:
                sniff_packets()
            case 2:
                 scan_port()
            case 3: 
                network_scan()
            case 4: 
                trace_route()
            case 5:
                console.print("exit")
                break
            case _:
                console.print("Try Again")
                
# Initial Menu
console.print("\n[#0094ab]                      Welcome to CableFish!                      [/#0094ab]", style="bold underline")
with console.status("                             Loading Application", spinner="shark"):
    time.sleep(3.0)
console.print("                    :fish: Successfully Loaded :fish:")                
                
# Loop to run menu           
if __name__ == "__main__":
    mainMenu()
