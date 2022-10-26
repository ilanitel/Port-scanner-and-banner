
import socket


'''
PART 2
Port scanner and banner
Use the function from part 1 to create a port scanner/banner grabber.
Port scanner
Create a function that receives an IP address and a list of port numbers as arguments. The function then
attempts to connect to each port on the list and returns a list of ports that have been confirmed as open by
the function.
Banner grabber
Create a banner-grabbing option. The function receives an IP address, and a confirmed open port number
as arguments and returns the “banner” – I.E the reply message of the port sends back to you after a
successful connection/sent message.
Combine
After creating both functions create a third function that allows you to use the “Port scanner” to find the
open ports of an IP address and then test the banner of each one of the open ports.
a. The function returns the port and banner of each open port.
b. Ports that are open but return no message return “unknown” instead of the banner
c. This will all be formatted as one string:
Example:
IP address – 172.18.0.7
Port 21 open 220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------
… 
'''
# This function will find the open ports to one ip address and return a list of that open ports
#determine whether `host` has the `port` open
def scanner(target_ip,port_list):
    open_Ports = []
    for port in port_list:
        # print(type(port))
        # creates a new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        # tries to connect to host using that port(don't need try/except because we use connect_ex)
        result = s.connect_ex((target_ip, int(port)))
        # The result is a response we get from try to connect (it is a number)
        if result == 0:
            # the connection was established, port is open,add the port to list
            open_Ports.append(port)
            s.close()
        else:
            # cannot connect, port is closed ,close the sokete and contiue to the next port on the list
            s.close()
            continue
    return open_Ports

# In this function we want to get information about the target like the service/version of the port that is open / os
def banner_grabber(ip, ports):

    ls_banner = []
    for port in ports:
        # creates a new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(2)
        # tries to connect to host
        s.connect((ip,int(port)))
        banner = s.recv(1024)

        if not banner:
        #print(type(banner))
        #print(banner + 'test1')
            ls_banner.append(('unkown', port))
            s.close()

        else:
            ls_banner.append((banner.decode(), port))
            s.close()
    return ls_banner

def combine():
    ls_ports = [443,22,53,101,80,95]
    ls_tup = []
    ip = '140.82.112.4'

    ls_ports_op=scanner(ip,ls_ports)
    #print(ls_ports)
    ls_tup =banner_grabber('140.82.112.4',ls_ports_op)
   # print(ls_tup)
    for k,v in ls_tup:
        print(f'IP address - {ip}\n')
        print(f'Port {v}\t\t\t\t {k}')

combine()