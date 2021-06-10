import paramiko
from scp import SCPClient

class Connection():
    
    def __init__(self):
        
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect('hostname', username='user', password='password')
        
    def send(self, file):
        scp = SCPClient(self.ssh.get_transport())
        scp.put(file)