import fabric



SERVER="127.0.0.1"
USER="root"
PASS="password"

#Easy usage of Git, Python, SCP and Crontab on Virtual machines/Remote servers

class VirtualFabricServer:
    def __init__(self,server,username,password):
        self.server=server
        self.username=username
        self.password=password
        
    def connect(self):
        self.connection=fabric.Connection(self.server, port=22, user=self.username, connect_kwargs={'password': self.password})

    def install_python(self):
        self.connection.run("sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools")
        
    def install_python_libraries(self,libraries):
        for i, library in enumerate(libraries):
            output=self.connection.run("pip install "+library)



    def git_clone(self):
        #TODO
        pass
    
    def git_pull(self):
        #TODO
        pass
    
    def scp_move(self):
        #TODO
        pass

    def synchronize_folders(self,local_folder,remote_folder,direction="l->r"):
        #TODO
        pass
        
    def manage_crontab(self):
        #TODO
        pass
    
    def run_python_script(self):
        #TODO
        pass
    
    def move_file(self):
        #TODO
        pass
    
    def create_folder(self):
        #TODO
        pass
    
    
    
    

vfs=VirtualFabricServer(SERVER,USER,PASS)
vfs.connect()



