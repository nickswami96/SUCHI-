from symbol import *
import socket

ip = input("TARGET IP ::")

print("""

                     (1)To SCAN RANGE OF PORTS
                     (2)TO SCAN SINGLE PORT

""")
ch = int(input("ENTER CHOICE:"))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if ch == 1:
       f = int(input("FROM:")) 
       t = int(input("TO:"))
       
       for x in range(f,t):
        
         RESULT = s.connect_ex((ip, x))
else:
       p = int(input("PORT:"))
       result = s.connect_ex((ip, p))
       
       print("******** INITIATING ATTACK ON",ip,"********" ) 
       

if result == 0 or RESULT == 0:
       print('PORT',p,'OPENED!')
else:
       print('PORT',p,'CLOSED!')


