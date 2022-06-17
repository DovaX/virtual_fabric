import fabric



c = fabric.Connection(SERVER, port=22, user=USER, connect_kwargs={'password': PASS})


#c.run("python test.py")


output=c.run("ls")
print(output)



#c.run("sudo apt update")
#c.run("apt upgrade")

#c.run("sudo kill 1062013")
#c.run("sudo dpkg --configure -a")

#c.run("sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools")


output=c.run("python3 test.py")

"""
with c.cd('../var/www'):
    #c.run('ls -la')
    
    output=c.run("pip install scrapy")
    output=c.run("pip install selenium==3.4.1")
    output=c.run("pip install pandas")
    output=c.run("sudo apt-get install firefox-geckodriver")
    #output=c.run("sudo apt-get install chromium-chromedriver")
    
    output=c.run("scrapy runspider file.py")
    
"""

#output=c.cd("../var/www")
#



#.split("\n")
a=output.stdout.encode("utf-8") #\r?
print(a)



import os

#Read file
#with c.cd('../var/www'):
#    c.run('ls -la')
output=c.get("../var/www/file.py","./temp_files/file.py")
os.system("C:/Programy/Notepad++/notepad++.exe ./temp_files/file.py")
    #output=c.put("")
print(output)
    
  
#Send editted file back
"""
with c.cd('../var/www'):
    c.run('ls -la')
    
    #os.system("C:\\Programy\\Notepad++\\notepad++.exe ./temp_files/file.py")
    
    output=c.put("./temp_files/file.py","../var/www/file.py")
    #output=c.put("")
    print(output)
""" 


