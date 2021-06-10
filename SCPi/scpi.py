import paramiko
from scp import SCPClient
import info.keys as keys

class Connection():
    
    def __init__(self):
        
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(keys.headboard.host, username=keys.headboard.user, 
                         password=keys.headboard.passwd)
        
    def send(self, file):
        scp = SCPClient(self.ssh.get_transport())
        scp.put(file)

#g = Connection()
#g.send(b'C:\Users\Ryan\Documents\message.txt')