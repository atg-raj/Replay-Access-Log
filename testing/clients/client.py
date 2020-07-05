import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('127.0.0.1', 7890))
client.connect(("127.0.0.1",80))


data = """GET / HTTP/1.1\r
Host: 127.0.0.1:80\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36\r
Keep-Alive: 300\r
Connection: keep-alive\r
Accept-Language: en-US,en;q=0.9\r
Accept: */*\r\n\r\n"""

dat1=data.encode()
client.send(dat1)


# f=open('in1.txt','r')
# data2=f.read()
# f.close()
# data2 = data2.replace("\n","\r\n")

# dat2=data2.encode()
# client.send(dat2)


s=client.recv(1000).decode()
print(s)
s=s.split('\r\n\r\n')
s=s[0].split('\n')
print(s)
client.close()



