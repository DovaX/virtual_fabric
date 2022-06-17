

import dogui.dogui_core as dg
from virtual_fabric_core import VirtualFabricServer
vfs=VirtualFabricServer(SERVER,USER,PASS)
vfs.connect()

c=vfs.connection



gui1=dg.GUI()




def run_ls():
    output=vfs.run("ls")
    print(output)



def cd():
    directory=entry1.text.get()
    vfs.change_directory(directory)


def run():
    command=entry2.text.get()+" "+entry3.text.get()
    vfs.run(command)


def read_file():
    file=entry4.text.get()
    vfs.read_file(file)

def update_file():
    file=entry4.text.get()
    vfs.update_file(file)

def read_crontab():
    #file=entry4.text.get()
    vfs.read_crontab()



dg.Label(gui1.window,"Change directory", 1, 1)
entry1=dg.Entry(gui1.window, 1, 2, width=30,text_input="../var")

dg.Button(gui1.window, "Submit", cd, 1, 3)


dg.Button(gui1.window, "ls", run_ls, 1, 4)



dg.Label(gui1.window,"Run script", 2, 1)
entry2=dg.Entry(gui1.window, 2, 2, width=30,text_input="python3")
entry3=dg.Entry(gui1.window, 2, 3, width=30,text_input="")

dg.Button(gui1.window, "Submit", run, 2, 4)



dg.Label(gui1.window,"Read & Update file", 3, 1)
entry4=dg.Entry(gui1.window, 3, 2, width=30,text_input="")
dg.Button(gui1.window, "Read", read_file, 3, 3)
dg.Button(gui1.window, "Update", update_file, 3, 4)


dg.Button(gui1.window, "Read crontab", read_crontab, 4, 1)












gui1.build_gui()


