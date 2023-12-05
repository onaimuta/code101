import socket
target = "192.168.100.1"
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((target, port))
if result == 0:
    print("Port {} is open".format(port))

else:
    print("Port {} is closed".format(port))