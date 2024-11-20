#! /usr/bin/env python

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
    console.print("Enter Total Number of Packets to Sniff: ")
    totalNum = int(input())
    
    packets = sniff(count=totalNum)
    
    with console.status("      Sniffing packets", spinner="shark"):
        time.sleep(3.0)
    console.print(":fish: Finished Sniffing :fish:")
    packets.summary()
    
    
    
#function to scan port
def scan_port():
    console.print("stank ass ho")

def mainMenu():
    while True:
        console.print("")

        console.print("                   :fish: :desktop_computer:  [#114159]Select Options:[/#114159] :desktop_computer:  :fish:", style="bold")
        console.print(":fish: [#1dd3ef]Option 1: Sniff Packets [/#1dd3ef]:fish:")
        console.print(":desktop_computer:  [#0094ab]Option 2: Port Scans [/#0094ab]:desktop_computer:")
        console.print(":fish: [#1dd3ef]Option 3: [/#1dd3ef]:fish:")
        console.print(":desktop_computer:  [#0094ab]Option 4: [/#0094ab]:desktop_computer:")
        console.print(":fish: [#1dd3ef]Option 5: [/#1dd3ef]:fish:")
        console.print(":desktop_computer:  [#0094ab]Option 6: Exit [/#0094ab]:desktop_computer:")

        console.print("")
        console.print("[#0094ab]                        Enter Your Choice:                       [/#0094ab]", style="bold underline")

        # General Option Input 
        optionChoice = int(input())

        # Match case to handle user input
        # console.print("Your Choice: ", optionChoice)
        match optionChoice:
            case 1:
                sniff_packets()
            case 2:
                 scan_port()
            case 6:
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
