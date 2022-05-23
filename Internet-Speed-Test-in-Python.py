import threading
import speedtest
import tkinter as tk
from tkinter import messagebox
#================#
sp = speedtest.Speedtest()
root=tk.Tk()
root.geometry("580x520")
root.title("Speed Test")
root.configure(bg="#1a1a1a")
font=("Arial",20)
root.resizable(False,False)
#=======================#

class Task(threading.Thread):
    def __init__(self, master, task):
        threading.Thread.__init__(self, target=task)

        if not hasattr(master, 'thread_enviar') or not master.thread_enviar.is_alive():
            master.thread_enviar = self
            self.start()

def check_start():
    global l
    l=tk.Label(root,text="Speed Test Internet...", bg="#1a1a1a" , fg="white" , font=font)
    l.place(x=180,y=420)
    d.configure(text='Checking...')
    u.configure(text='Checking...')
    p.configure(text='Checking...')
    c.configure(text='Checking...')
    s.configure(text='Checking...')
    h.configure(text='Checking...')
    i.configure(text='Checking...')
    messagebox.showinfo("Confirmation" , "Speed Test")
    b["state"] = "disabled"

def check():
    check_start()

    d.configure(text=f'{(sp.download()//10**6)} Mbps')
    u.configure(text=f'{sp.upload()//10**6} Mbps')

    servernames =[]
    sp.get_servers(servernames)
    pi = int(sp.results.ping)
    p.configure(text=f"{pi} Ms")

    best_server = sp.get_best_server()
    lis = []
    lis = [key[1] for key in best_server.items()]
    # for key in best_server.items():
    #     lis.append(key[1])

    c.configure(text=sp.config['client']['country'])
    s.configure(text=sp.config['client']['isp'])
    h.configure(text=lis[8])
    i.configure(text=sp.config['client']['ip'])
    l.configure(text='Successfull !' , font=font,fg='green')
    l.place(x=240,y=420)

    b["state"] = "normal"


#=======================#
dspeed = tk.Label(root,text="Download Speed :",bg='#1a1a1a' , fg="yellow" , font=font)
dspeed.place(x=10,y=10)
d=tk.Label(root,text="" , bg="#1a1a1a" , fg ="yellow" , font=font)
d.place(x=270,y=10)

uspeed=tk.Label(root,text="Upload Speed :",bg='#1a1a1a', fg="Orange" , font=font)
uspeed.place(x=10,y=70)
u=tk.Label(root,text="" , bg="#1a1a1a" , fg ="Orange" , font=font)
u.place(x=270,y=70)

ping=tk.Label(root,text="Ping :" , bg="#1a1a1a" , fg="cyan" , font=font)
ping.place(x=10,y=130)
p=tk.Label(root,text="" , bg="#1a1a1a" , fg ="cyan" , font=font)
p.place(x=270,y=130)

country=tk.Label(root,text="Country :" , bg="#1a1a1a" , fg="pink" , font=font)
country.place(x=10,y=190)
c = tk.Label(root,text="" , bg="#1a1a1a" , fg ="pink" , font=font)
c.place(x=270,y=190)

sponsor=tk.Label(root,text="Sponsor :" , bg="#1a1a1a" , fg="Chartreuse" , font=font)
sponsor.place(x=10,y=250)
s = tk.Label(root,text="" , bg="#1a1a1a" , fg ="Chartreuse" , font=font)
s.place(x=270,y=250)

host =tk.Label(root,text="Host :" , bg="#1a1a1a" , fg="gold" , font=font)
host.place(x=10,y=310)
h = tk.Label(root,text="" , bg="#1a1a1a" , fg ="gold" , font=font)
h.place(x=270,y=310)

ip =tk.Label(root,text="IP :" , bg="#1a1a1a" , fg="YellowGreen" , font=font)
ip.place(x=10,y=360)
i = tk.Label(root,text="" , bg="#1a1a1a" , fg ="YellowGreen" , font=font)
i.place(x=270,y=360)


b=tk.Button(root,text="Start" , command=lambda: Task(root, check) ,cursor ='hand2', bg="yellow" , fg="black")
b.place(x=30,y=442,width=520,height=50)
root.mainloop()