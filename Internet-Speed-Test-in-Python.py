# pip install speedtest-cli

import speedtest
import tkinter as tk
from tkinter import messagebox
#================#
sp = speedtest.Speedtest()
root=tk.Tk()
root.geometry("580x520") ; root.title("Speed Test") ; root.configure(bg="grey") ; font=("Arial",20)
root.resizable(False,False)
#=======================#
def check():
    l.place(x=180,y=420)
    messagebox.showinfo("Confirmation" , "Speed Test")

    d.configure(text=str(sp.download()//10**6) + " Mbps")
    u.configure(text=str(sp.upload()//10**6) + " Mbps")

    servernames =[]
    sp.get_servers(servernames)
    pi = int(sp.results.ping)
    p.configure(text=str(pi) + " Ms")

    best_server = sp.get_best_server()
    lis = []
    for key in best_server.items():
        lis.append(key[1])

    c.configure(text=sp.config['client']['country'])
    s.configure(text=sp.config['client']['isp'])
    h.configure(text=lis[8])
    i.configure(text=sp.config['client']['ip'])
    l.configure(text='Successfull !' , font=font,fg='green');l.place(x=240,y=420)


#=======================#
dspeed = tk.Label(root,text="Download Speed :",bg='grey' , fg="yellow" , font=font) ; dspeed.place(x=10,y=10)
d=tk.Label(root,text="" , bg="grey" , fg ="yellow" , font=font) ; d.place(x=270,y=10)

uspeed=tk.Label(root,text="Upload Speed :",bg='grey', fg="Orange" , font=font) ; uspeed.place(x=10,y=70)
u=tk.Label(root,text="" , bg="grey" , fg ="Orange" , font=font) ; u.place(x=270,y=70)

ping=tk.Label(root,text="Ping :" , bg="grey" , fg="cyan" , font=font) ; ping.place(x=10,y=130)
p=tk.Label(root,text="" , bg="grey" , fg ="cyan" , font=font) ; p.place(x=270,y=130)

country=tk.Label(root,text="Country :" , bg="grey" , fg="pink" , font=font) ; country.place(x=10,y=190)
c = tk.Label(root,text="" , bg="grey" , fg ="pink" , font=font) ; c.place(x=270,y=190)

sponsor=tk.Label(root,text="Sponsor :" , bg="grey" , fg="Chartreuse" , font=font) ; sponsor.place(x=10,y=250)
s = tk.Label(root,text="" , bg="grey" , fg ="Chartreuse" , font=font) ; s.place(x=270,y=250)

host =tk.Label(root,text="Host :" , bg="grey" , fg="gold" , font=font) ; host.place(x=10,y=310)
h = tk.Label(root,text="" , bg="grey" , fg ="gold" , font=font) ; h.place(x=270,y=310)

ip =tk.Label(root,text="Ip :" , bg="grey" , fg="YellowGreen" , font=font) ; ip.place(x=10,y=360)
i = tk.Label(root,text="" , bg="grey" , fg ="YellowGreen" , font=font) ; i.place(x=270,y=360)


l=tk.Label(root,text="Speed Test Internet ...", bg="grey" , fg="white" , font=font)
b=tk.Button(root,text="Start" , command=check ,cursor ='hand2', bg="yellow" , fg="black");b.place(x=30,y=460,width=510,height=50)
root.mainloop()