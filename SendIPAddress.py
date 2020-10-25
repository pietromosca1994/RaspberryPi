import subprocess
import socket
from Email import Email
import time
from tools_socket import *

IP_address_old=''

to_address='pietromosca1994@gmail.com'
from_address='pietromosca1994@gmail.com'
from_password=''

while 1:
    time.sleep(10)
    
    if IsConnected()==True:
        IP_address_new=GetIPAddress()
        
        if IP_address_new!=IP_address_old:
            ifconfig=subprocess.check_output('ipconfig' ).decode('utf-8')
            
            subject='RaspberryPi IP Address'
            body='IP Address: '+IP_address_new+'\n' \
                'ifconfig: '+ifconfig
           
            mail=Email(subject, body)
            mail.SendMail(to_address, from_address, from_password)
            
            IP_address_old=IP_address_new
        

