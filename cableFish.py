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
import scapy.all as scapy
from rich.console import Console
from rich.style import Style

console = Console()

# Styles
darkCyan = Style(color="#0094ab")  # dark cyan color

# Welcome screen
console.print("[#0094ab]          Welcome to CableFish!          [/#0094ab]", style="bold underline")
with console.status("     Loading Application", spinner="shark"):
    time.sleep(5.0)
console.print("        :fish: Successfully Loaded :fish:")

#request = scapy.ARP() 
#print(request.show())

