import fabric
import os


SERVER="127.0.0.1"
USER="root"
PASS="password"

#Easy usage of Git, Python, SCP and Crontab on Virtual machines/Remote servers

class VirtualFabricServer:
    def __init__(self,server,username,password):
        self.server=server
        self.username=username
        self.password=password
        self.working_directory="~"
        
    def connect(self):
        self.connection=fabric.Connection(self.server, port=22, user=self.username, connect_kwargs={'password': self.password})

    def install_python(self):
        self.connection.run("sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools")
        
    def install_python_libraries(self,libraries):
        for i, library in enumerate(libraries):
            output=self.connection.run("pip install "+library)

    def change_directory(self,directory):
        self.working_directory=directory
            
    def run(self,command):        
        with self.connection.cd(self.working_directory):        
            output=self.connection.run(command)
            print(output)
            
            
    def read_file(self,file,directory=None):
        if not directory is None:
            self.working_directory=directory
        
        #Read file
        output=self.connection.get(directory+"/"+file,"./temp_files/"+file)
        os.system("C:/Programy/Notepad++/notepad++.exe ./temp_files/"+file)
        #output=c.put("")
        print(output)
        
            
    def update_file(self,file,directory=None):
        if not directory is None:
            self.working_directory=directory
        
        #Read file
        output=self.connection.put("./temp_files/"+file,directory+"/"+file)
        #os.system("C:/Programy/Notepad++/notepad++.exe ./temp_files/"+file)
        #output=c.put("")
        print(output)
        
    def read_crontab(self):
        self.read_file("root","../var/spool/cron/crontabs")
        
    def update_crontab(self):
        self.update_file("root","../var/spool/cron/crontabs")
        
    def new_cronjob(self):
        with open("./temp_files/root","a+") as f:
            f.write("1 * * * * /usr/bin/env python3 /var/www/slack_community_notifier/slack_community_notifier.py")
        

        
    def git_clone(self,repository):
        """repository ... HTTPS repository url e.g. https://github.com/DovaX/virtual_fabric.git"""
        command="git clone "+repository
        self.connection.run(command)
        
    def git_pull(self):
        command="git pull"
        self.connection.run(command)
        
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



